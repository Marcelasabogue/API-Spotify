jdbc_user = dbutils.secrets.get(scope="my-secrets", key="sql-user")
jdbc_password = dbutils.secrets.get(scope="my-secrets", key="sql-password")
blob_key = dbutils.secrets.get(scope="my-secrets", key="blob-key")

# Configurar las propiedades de la conexión
jdbc_hostname = "tb-az-svr-sql01.database.windows.net"
jdbc_database = "TBDatawarehouseDB"
jdbc_url = f"jdbc:sqlserver://{jdbc_hostname}:1433;database={jdbc_database}"
jdbc_properties = {
    "user": jdbc_user,
    "password": jdbc_password,
    "driver": "com.microsoft.sqlserver.jdbc.SQLServerDriver"
}


#Importación de librerias necesarias
%pip install spotipy
import spotipy
import requests
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials
from pyspark.sql.functions import col, expr
import json
import os

from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from delta.tables import DeltaTable

from spotipy.oauth2 import SpotifyClientCredentials
from datetime import datetime
import time
import spotipy
client_credentials_manager = SpotifyClientCredentials(client_id="12345abcs", client_secret="abcd123344")
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager, requests_timeout=30)
current_year = datetime.now().year

# Get tracks in the current year
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
# Autenticación con Spotify
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id="12345abcs",
    client_secret="abcd123344"
))
track_list=[]
for i in range(0,1000,50):
  track_result = sp.search(q = f'year:{current_year}', type="track", limit=50, offset=i, market='CO')
  for row in track_result['tracks']['items']:
      artist_id = row['artists'][0]['id'] 
      track_id = row['id']
      track_name = row['name']
      track_popularity = row['popularity']
      track_release_date = row['album']['release_date']
      track_list.append({'artist_id':artist_id, 'track_id':track_id, 'track_name':track_name, 'track_popularity':track_popularity, 'track_release_date':track_release_date})
track_df = pd.DataFrame.from_dict(track_list)
#display(track_df)

# Get artist from the track
artist_list = []
artist_id_list = track_df['artist_id'].to_list()
artist_id_set = set(artist_id_list)
artist_id_list_unique = list(artist_id_set)

for row in artist_id_list_unique:
  artist_result = sp.artist(row)
  artist_id = artist_result['id']
  artist_name = artist_result['name']
  artist_popularity = artist_result['popularity']
  artist_follower = artist_result['followers']['total']
  if len(artist_result['images']) == 0:
    artist_image = None
  else:
    artist_image = artist_result['images'][0]['url'] 
  artist_list.append({'artist_id':artist_id, 'artist_name': artist_name , 'artist_popularity':artist_popularity, 'artist_follower':artist_follower, 'artist_image':artist_image})

artist_dff = pd.DataFrame.from_dict(artist_list)
#display(artist_dff)

import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from datetime import datetime
import time
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count

# Autenticación con la API de Spotify
client_id = "TU_CLIENT_ID"
client_secret = "TU_CLIENT_SECRET"

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=client_id,
    client_secret=client_secret
))

# Función para obtener las canciones detalladas de una playlist
def get_playlist_tracks_detailed(playlist_id, playlist_type):
    tracks_data = []
    offset = 0
    limit = 100

    while True:
        response = sp.playlist_tracks(playlist_id, offset=offset, limit=limit)
        items = response['items']

        if not items:
            break

        for item in items:
            track = item['track']
            if track is None:
                continue

            track_id = track['id']
            track_name = track['name']
            track_popularity = track['popularity']
            album_name = track['album']['name']
            album_release_date = track['album']['release_date']
            track_added_at = item.get('added_at')

            artist = track['artists'][0]
            artist_id = artist['id']
            artist_name = artist['name']

            try:
                artist_info = sp.artist(artist_id)
                artist_followers = artist_info['followers']['total']
                artist_popularity = artist_info['popularity']
                artist_genres = ", ".join(artist_info['genres'])
                artist_url = artist_info['external_urls']['spotify']
            except:
                artist_followers = None
                artist_popularity = None
                artist_genres = None
                artist_url = None

            # Añadir la columna que indica de qué playlist proviene
            tracks_data.append({
                'extraction_date': datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
                'track_id': track_id,
                'track_name': track_name,
                'track_popularity': track_popularity,
                'album_name': album_name,
                'album_release_date': album_release_date,
                'artist_id': artist_id,
                'artist_name': artist_name,
                'artist_followers': artist_followers,
                'artist_popularity': artist_popularity,
                'artist_genres': artist_genres,
                'artist_url': artist_url,
                'track_added_at': track_added_at,
                'playlist_type': playlist_type  # Añadimos el tipo de playlist
            })

            time.sleep(0.1)  # Pausa para evitar rate limits

        offset += limit

    return pd.DataFrame(tracks_data)

# ID de las playlists que quieres consultar
playlist_id_colombia = "6h6uzoRBXnkjeoEjwiX27R"  # Top 50 Colombia
playlist_id_global = "0sDahzOkMWOmLXfTMf2N4N"  # Top 50 Global

# Obtener la información detallada de ambas playlists
playlist_colombia_df = get_playlist_tracks_detailed(playlist_id_colombia, "Colombia")
playlist_global_df = get_playlist_tracks_detailed(playlist_id_global, "Global")

# Concatenar los dos DataFrames (de Colombia y Global) en uno solo
final_playlist_GlobalCol = pd.concat([playlist_colombia_df, playlist_global_df], ignore_index=True)

# Crear una sesión Spark
#spark = SparkSession.builder.appName("SpotifyArtistsAnalysis").getOrCreate()

# Convertir el DataFrame de pandas a PySpark
#final_playlist_GlobalCol = spark.createDataFrame(final_playlist_df)

# Mostrar el DataFrame de PySpark
#display(final_playlist_GlobalCol)

from pyspark.sql.types import IntegerType

ArtistasTracks = spark.createDataFrame(artist_dff)
TOP100_GlobalCol = spark.createDataFrame(final_playlist_GlobalCol)

ArtistasTracks.write.jdbc(url=jdbc_url, table="spotify_artistasTracks", mode="overwrite", properties=jdbc_properties)
TOP100_GlobalCol.write.jdbc(url=jdbc_url, table="spotify_top100", mode="overwrite", properties=jdbc_properties)






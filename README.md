# 🎵 Spotify Exploration

## 📜 Overview

As part of this project, the Spotify API was integrated to gather relevant information about artists and their performance on the platform. The process initially focused on three key types of data:

- 👉 Tracks of the Year  
- 👉 TOP 100 Artists – Global and Colombia

---

## 🎧 1. Retrieving Information from Tracks of the Year

This section focuses on tracks released in the current year, extracting the most important information about the artists associated with each release.

### Extracted Information:

- 🎤 Artist ID  
- 👩‍🎤 Artist Name  
- 🌟 Artist Popularity  
- 👥 Number of Followers  
- 🎶 Music Genres  
- 📸 Artist Image  
- 🎶 Track ID  
- 🎧 Track Name  
- 🌟 Track Popularity  
- 📅 Track Release Date  
- 📀 Album Name  

---

### 🎤 What Does Artist and Track Popularity Mean?

#### Artist Popularity:
A value assigned by Spotify between **0 and 100**, where 100 represents the highest popularity. This metric is not based solely on total number of streams but also includes:

- 🎶 **Streams**: Number of times the artist's songs have been played  
- 💬 **Engagement**: How often users save, share, or add the songs to playlists  
- ⏳ **Recency**: Recent activity carries more weight  
- 📋 **Playlist Inclusions**: Being featured in popular playlists boosts popularity  

💡 *This popularity score is constantly updated and is a good indicator for marketing and promotional strategies.*

---

#### 🎶 Track Popularity:
Also expressed as a value from **0 to 100**, representing the current relevance and trend of a song. It is calculated based on:

- 🎧 **Streams**: Total number of plays  
- ⏳ **Recency**: Recently played songs are favored  
- 📋 **Playlist Inclusions**: Inclusion in relevant playlists increases popularity  

⚠️ *Note: This metric is not updated in real-time and may reflect data with some delay.*

---

### 📌 Sample Extracted Data (Tracks of the Year)

| track_id              | track_name                            | track_popularity | album_name                            | release_date | artist_id              | artist_name     | artist_popularity | followers   | genres                        | image_url |
|------------------------|----------------------------------------|------------------|----------------------------------------|--------------|-------------------------|------------------|-------------------|-------------|-------------------------------|-----------|
| 3U21A07gAloCc4P7J8rxcn | Shakira: Bzrp Music Sessions, Vol. 53 | 92               | Shakira: Bzrp Music Sessions, Vol. 53 | 2023-01-11   | 0EmeFodog0BfCgMzAIvKQp  | Shakira         | 88                | 33,700,000  | pop, reggaeton, latin pop     | https://i.scdn.co/image/ab6761610000e5eb1b7a13e2dbed1fbfa99b8c35 |
| 0yLdNVWF3Srea0uzk55zFn | Ella Baila Sola                       | 95               | Genesis                                | 2023-04-07   | 12GqGscKJx3aE4t07u7eVZ  | Eslabon Armado  | 85                | 9,200,000   | regional mexican, corridos    | https://i.scdn.co/image/ab6761610000e5eb75b06014fc65a4706714c96b |
| 2LRoIwlKmHjgvigdNGBHNo | La Bebe                               | 90               | La Bebe (Remix)                        | 2023-03-17   | 1SupJlEpv7RS2tPNRaHViT  | Yng Lvcas       | 80                | 4,100,000   | reggaeton, latin trap         | https://i.scdn.co/image/ab6761610000e5ebb6476c81275f2350f63b0400 |

---

## 🌍 2. Retrieving Information from TOP 100 Artists (Global and Colombia)

Data was extracted from unofficial but highly relevant playlists that reflect market trends and are updated weekly.

### Playlists Used:

- 🇨🇴 **Colombia TOP 100** → Playlist ID: `6h6uzoRBXnkjeoEjwiX27R`  
- 🌐 **Global TOP 100** → Playlist ID: `0sDahzOkMWOmLXfTMf2N4N`

---

### 📌 Sample Extracted Data (TOP 100 Global and Colombia)

| track_id              | track_name | track_popularity | album_name               | release_date | playlist_inclusion_date | artist_id              | artist_name   | followers   | artist_popularity | genres                                | artist_url                                                   | playlist_type |
|------------------------|------------|------------------|---------------------------|---------------|--------------------------|--------------------------|----------------|--------------|--------------------|----------------------------------------|---------------------------------------------------------------|----------------|
| 0e7ipj03S05BNilyu5bRzt | Provenza   | 89               | Mañana Será Bonito        | 2023-02-24    | 2025-02-01               | 790FomKkXshlbRYZFtlgla   | Karol G       | 35,200,000  | 92                 | reggaeton, trap latino, pop urbano     | https://open.spotify.com/artist/790FomKkXshlbRYZFtlgla        | Colombia       |
| 3ZFTkvIE7kyPt6Nu3PEa7V | Faded      | 94               | Different World            | 2018-12-14    | 2025-02-05               | 2CIMQHirSU0MQqyYHq0eOx   | Alan Walker   | 21,400,000  | 86                 | EDM, electro house, progressive house  | https://open.spotify.com/artist/2CIMQHirSU0MQqyYHq0eOx        | Global         |
| 6HabM2PUM519iIxv2eZFvi | Flowers    | 95               | Endless Summer Vacation    | 2023-03-10    | 2025-02-05               | 5YGY8feqx7naU7z4HrwZM6   | Miley Cyrus  | 57,300,000  | 93                 | pop, dance pop, contemporary pop       | https://open.spotify.com/artist/5YGY8feqx7naU7z4HrwZM6        | Global         |

---

## 🔄 Data Refresh and API Limitations

- **TOP 100 (Global and Colombia)** data is updated weekly.
- **Tracks of the Year** are obtained using the `/browse/new-releases` endpoint, filtering by album or track release date.

### ⚠️ Spotify API Limitations

- Spotify does **not** provide an official artist ranking based on streams or total plays.
- The analysis is based on **unofficial but representative playlists** to infer popularity and trends.

---

## 🎯 Use and Recommendations

This information is critical for Marketing, Booking, and Event teams to make informed decisions on which artists to contact based on **local and global trends**.

---

## 🔌 BI Database Connection

All the extracted data is stored in **SQL Server** and connected via **DirectQuery** for real-time querying through BI tools:

- `spotify_artistasTracks` → (Tracks of the Year)  
- `spotify_top100` → (TOP 100 Global and Colombia)

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


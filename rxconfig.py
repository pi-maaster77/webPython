import os
import sqlalchemy
import reflex as rx
import fastapi

# comentar las siguientes 2 lineas en el caso de usar docker o variables de entorno
from dotenv import load_dotenv
load_dotenv()


"""
la estructura del archivo `.env` debe de ser la siguiente:

DATABASE = "nombre de la base de datos"
DB_USER = "usuario con el que se accedera a la base de datos"
DB_PASSWORD = "contraseña del usuario"
DB_PORT = (puerto_de_la_base_de_datos)
DB_HOST = "ip de la base de datos"
"""

database = os.getenv("DATABASE")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
port = os.getenv("DB_PORT")
host = os.getenv("DB_HOST")
db = os.getenv("DATABASE")
config = rx.Config(
    app_name="webPython",
    #db_url=f"mysql://{user}:{password}@{host}:{port}/{database}",
)

app = fastapi.FastAPI()

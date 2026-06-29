import pyodbc
from config.settings import settings

def get_connection():
    return pyodbc.connect(settings.connection_string)
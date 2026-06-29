import pandas as pd
from sqlalchemy import create_engine, text
from config.settings import settings

def get_engine():
    """
    Crea un engine de SQLAlchemy usando la cadena de conexión ODBC.
    """
    connection_string = (
        f"mssql+pyodbc://{settings.DB_USER}:{settings.DB_PASSWORD}@"
        f"{settings.DB_SERVER}/{settings.DB_NAME}"
        f"?driver=ODBC+Driver+17+for+SQL+Server"
        f"&Encrypt=yes&TrustServerCertificate=yes"
        f"&Connection Timeout=30"
    )
    engine = create_engine(
        connection_string,
        pool_pre_ping=True,
        connect_args={'timeout': 30}
    )
    return engine

def truncate_table(table_name, engine):
    """
    Elimina todas las filas de la tabla usando DELETE (respeta FK).
    """
    with engine.connect() as conn:
        conn.execute(text(f"DELETE FROM {table_name}"))
        conn.commit()
        print(f"  🗑️ Tabla '{table_name}' limpiada (DELETE)")

def load_dimension(df, model, engine):
    """
    Carga una tabla de dimensión a partir de un DataFrame y un modelo.
    Usa inserción fila por fila (method=None) para evitar errores de sintaxis.
    """
    table_name = model.TABLE_NAME
    column_map = model.COLUMN_MAP
    
    # Seleccionar solo las columnas que están en el mapeo
    df_to_load = df[list(column_map.keys())].copy()
    
    # Renombrar columnas según el mapeo
    df_to_load.rename(columns=column_map, inplace=True)
    
    # Limpiar la tabla antes de insertar
    truncate_table(table_name, engine)
    
    # Insertar los datos fila por fila (más seguro, evita errores de sintaxis)
    with engine.connect() as conn:
        df_to_load.to_sql(
            name=table_name,
            con=conn,
            if_exists='append',
            index=False,
            method=None,  # Insertar fila por fila
            chunksize=100  # Se ignora con method=None, pero lo dejamos
        )
        conn.commit()
    print(f"  ✅ {len(df_to_load)} filas insertadas en '{table_name}'")
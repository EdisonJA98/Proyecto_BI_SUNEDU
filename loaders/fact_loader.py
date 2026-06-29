import pandas as pd
from sqlalchemy import text

def load_fact(df, model, engine, chunksize=1000):
    """
    Carga una tabla de hechos a partir de un DataFrame y un modelo.
    El modelo debe tener TABLE_NAME y COLUMN_MAP.
    """
    table_name = model.TABLE_NAME
    column_map = model.COLUMN_MAP
    
    # Seleccionar solo las columnas que están en el mapeo
    df_to_load = df[list(column_map.keys())].copy()
    
    # Renombrar columnas según el mapeo
    df_to_load.rename(columns=column_map, inplace=True)
    
    # Insertar los datos (no truncamos las tablas de hechos)
    with engine.connect() as conn:
        # Insertar fila por fila (method=None) para evitar límite de parámetros
        df_to_load.to_sql(
            name=table_name,
            con=conn,
            if_exists='append',
            index=False,
            method=None,          # ← Cambio clave: inserta una fila a la vez
            chunksize=chunksize   # ← Se ignora con method=None, pero se mantiene
        )
        conn.commit()
    print(f"  ✅ {len(df_to_load)} filas insertadas en '{table_name}'")
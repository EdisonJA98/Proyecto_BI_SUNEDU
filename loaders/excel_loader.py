import pandas as pd
from config.settings import settings

def load_excel_sheets():
    """
    Lee todas las hojas del archivo Excel y devuelve un diccionario
    con el nombre de la hoja como clave y el DataFrame como valor.
    """
    excel_path = settings.EXCEL_PATH
    print(f"📂 Leyendo archivo Excel: {excel_path}")
    
    # Diccionario para almacenar los DataFrames
    sheets = {}
    
    # Lista de nombres de hojas esperadas (opcional, podemos leer todas)
    expected_sheets = [
        "DIM_Universidades",
        "DIM_Tiempo",
        "DIM_Resultado_Supervision",
        "DIM_Tipo_Denuncia",
        "DIM_Naturaleza_Denunciante",
        "DIM_Rol_Denunciante",
        "DIM_Canal_Recepcion",
        "DIM_Estado_Denuncia",
        "DIM_Gravedad_Denuncia",
        "DIM_Tipo_Sancion",
        "DIM_Gravedad_Sancion",
        "DIM_Estado_Sancion",
        "HECHOS_Denuncias",
        "HECHOS_Supervisiones",
        "HECHOS_Sanciones"
    ]
    
    # Leer todas las hojas del Excel
    excel_file = pd.ExcelFile(excel_path)
    for sheet_name in expected_sheets:
        if sheet_name in excel_file.sheet_names:
            df = excel_file.parse(sheet_name)
            sheets[sheet_name] = df
            print(f"  ✅ Hoja '{sheet_name}' cargada con {len(df)} filas")
        else:
            print(f"  ⚠️ Hoja '{sheet_name}' no encontrada en el archivo")
    
    return sheets
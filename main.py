from config.settings import settings
from database.connection import get_connection
from loaders.excel_loader import load_excel_sheets
from loaders.dim_loader import get_engine, load_dimension
from loaders.fact_loader import load_fact
from utils.logger import get_logger

# Importar todos los modelos
from models import (
    dim_universidad,
    dim_tiempo,
    dim_resultado_supervision,
    dim_tipo_denuncia,
    dim_naturaleza_denunciante,
    dim_rol_denunciante,
    dim_canal_recepcion,
    dim_estado_denuncia,
    dim_gravedad_denuncia,
    dim_tipo_sancion,
    dim_gravedad_sancion,
    dim_estado_sancion,
    hechos_denuncias,
    hechos_supervisiones,
    hechos_sanciones
)

logger = get_logger(__name__)

def main():
    logger.info("🚀 Iniciando proceso de carga de datos")
    
    # 1. Leer el Excel
    sheets = load_excel_sheets()
    
    # 2. Crear el engine de SQLAlchemy
    engine = get_engine()
    
    # 3. Cargar dimensiones (en orden)
    logger.info("📥 Cargando dimensiones...")
    
    # Dimensiones que no dependen de otras
    load_dimension(sheets["DIM_Tiempo"], dim_tiempo, engine)
    load_dimension(sheets["DIM_Universidades"], dim_universidad, engine)
    load_dimension(sheets["DIM_Resultado_Supervision"], dim_resultado_supervision, engine)
    load_dimension(sheets["DIM_Tipo_Denuncia"], dim_tipo_denuncia, engine)
    load_dimension(sheets["DIM_Naturaleza_Denunciante"], dim_naturaleza_denunciante, engine)
    load_dimension(sheets["DIM_Rol_Denunciante"], dim_rol_denunciante, engine)
    load_dimension(sheets["DIM_Canal_Recepcion"], dim_canal_recepcion, engine)
    load_dimension(sheets["DIM_Estado_Denuncia"], dim_estado_denuncia, engine)
    load_dimension(sheets["DIM_Gravedad_Denuncia"], dim_gravedad_denuncia, engine)
    load_dimension(sheets["DIM_Tipo_Sancion"], dim_tipo_sancion, engine)
    load_dimension(sheets["DIM_Gravedad_Sancion"], dim_gravedad_sancion, engine)
    load_dimension(sheets["DIM_Estado_Sancion"], dim_estado_sancion, engine)
    
    # 4. Cargar hechos (en orden)
    logger.info("📥 Cargando hechos...")
    load_fact(sheets["HECHOS_Denuncias"], hechos_denuncias, engine)
    load_fact(sheets["HECHOS_Supervisiones"], hechos_supervisiones, engine)
    load_fact(sheets["HECHOS_Sanciones"], hechos_sanciones, engine)
    
    logger.info("✅ Proceso de carga completado exitosamente")

if __name__ == "__main__":
    main()
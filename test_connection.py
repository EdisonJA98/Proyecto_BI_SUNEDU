"""
Script temporal para probar la conexión a la base de datos usando SQLAlchemy.
Ejecutar con: python test_connection.py
"""

from sqlalchemy import text
from loaders.dim_loader import get_engine

def test_sqlalchemy_connection():
    """
    Prueba la conexión a la base de datos ejecutando una consulta simple.
    """
    print("🔄 Probando conexión con SQLAlchemy...")
    
    try:
        # Obtener el engine
        engine = get_engine()
        
        # Intentar conectar y ejecutar una consulta simple
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1 AS test"))
            row = result.fetchone()
            
            if row and row.test == 1:
                print("✅ Conexión SQLAlchemy exitosa")
                print(f"   Servidor: {engine.url.host}")
                print(f"   Base de datos: {engine.url.database}")
                return True
            else:
                print("❌ La consulta no devolvió el resultado esperado")
                return False
                
    except Exception as e:
        print(f"❌ Error en SQLAlchemy: {e}")
        print("\n📌 Posibles causas:")
        print("   1. Firewall de Azure: agrega tu IP actual en el portal de Azure")
        print("   2. Credenciales incorrectas: verifica .env")
        print("   3. El servidor no está accesible: verifica el nombre del servidor")
        return False

if __name__ == "__main__":
    print("=" * 50)
    print("PRUEBA DE CONEXIÓN SQLALCHEMY")
    print("=" * 50)
    test_sqlalchemy_connection()
    print("=" * 50)
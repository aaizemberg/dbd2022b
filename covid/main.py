from fastapi import FastAPI
import duckdb

def duckdb_connect():
    return duckdb.connect(database=':memory:')

conn = duckdb_connect()

app = FastAPI()

@app.get("/")
def hola():
    return {"Hello": "World"}
    
@app.get("/count")
def count():
    return  { "rows" : conn.execute("SELECT count(*) from read_parquet('data/Covid19Casos.parquet');").fetchone()[0] }
    
@app.get("/edad_fallecidos_x_provincia")
def edad_fallecidos():
    query= """
          select carga_provincia_nombre, avg(edad) 
          from read_parquet('data/Covid19Casos.parquet') 
          where edad < 120 and edad > 0 
            and edad_años_meses = 'Años' 
            and clasificacion_resumen = 'Confirmado' 
            and fallecido = 'SI' 
          group by 1 
          order by 1;
          """
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()


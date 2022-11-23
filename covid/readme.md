# covid

```
# crear un virtualenv

                     |||--- nombre del directorio donde voy a generar este ambiente virtual
$ python.exe -m venv api

# api\Scripts\activate.bat

(api) > pip list
(api) > pip install fastapi
(api) > pip install "uvicorn[standard]"
(api) > pip install duckdb

(api) > cd api

main.py

(api) > uvicorn main:app --reload


Para visualizar archivos en formato .parquet
https://duckdb.org/docs/guides/data_viewers/tad
```

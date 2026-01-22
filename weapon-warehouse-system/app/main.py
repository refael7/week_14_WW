
from fastapi import FastAPI, UploadFile, File, HTTPException
import uvicorn
from models import add_columns_risk_level, add_unknown
import pandas as pd
from db import create_table ,insert_weapons_list
from contextlib import asynccontextmanager



@asynccontextmanager
async def lifespan():
    create_table()
    yield

app = FastAPI(lifespan=lifespan)



@app.post("/upload")
def create_file(file: UploadFile = File(...)):
    if not file:
        raise HTTPException(detail="The file not provided",status_code=400)
    df = pd.read_csv(file.file)
    df = add_columns_risk_level (df)
    df = add_unknown(df)

    print(df)
    return {"status": "success",
            "inserted_records":20
            }



if __name__ == "__main__":
     uvicorn.run("main:app",port=8000,host="localhost" ,reload=True)
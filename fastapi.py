from fastapi import FastAPI

app = FastAPI() # type: ignore

@app.get('/')
def read_root():
    return {"Hello": "World"}
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"Log Analyzer API Running"}

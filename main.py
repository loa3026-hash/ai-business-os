from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "AI Business OS is running"}

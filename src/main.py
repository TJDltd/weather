from fastapi import FastAPI
from fetch_weather import fetch_current_weather

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Homepage"}

@app.get("/current_weather")
async def current_weather(location: str = "?latitude=52.52&longitude=13.41"):
    return {"message": fetch_current_weather(location)}

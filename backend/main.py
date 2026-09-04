from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import httpx

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "Oil Spill FastAPI Backend is Running 🚢"
    }


@app.get("/api/weather")
async def get_weather():

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": 26.8467,
        "longitude": 80.9462,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
        "timezone": "Asia/Kolkata"
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)

    data = response.json()

    return {
        "city": "Lucknow",
        "temperature": data["current"]["temperature_2m"],
        "humidity": data["current"]["relative_humidity_2m"],
        "windSpeed": data["current"]["wind_speed_10m"]
    }
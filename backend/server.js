const express = require("express");
const cors = require("cors");

const app = express();

app.use(cors());
app.use(express.json());

app.get("/", (req, res) => {
    res.send("Backend is Running 🚀");
});

app.get("/api/weather", async (req, res) => {
    try {
        const response = await fetch(
            "https://api.open-meteo.com/v1/forecast?latitude=26.8467&longitude=80.9462&current=temperature_2m,relative_humidity_2m,wind_speed_10m&timezone=Asia%2FKolkata"
        );

        const data = await response.json();

        res.json({
            city: "Lucknow",
            temperature: data.current.temperature_2m,
            humidity: data.current.relative_humidity_2m,
            windSpeed: data.current.wind_speed_10m
        });

    } catch (error) {
        console.log(error);

        res.status(500).json({
            error: "Weather API failed"
        });
    }
});

app.listen(5000, () => {
    console.log("Server running on http://localhost:5000");
});
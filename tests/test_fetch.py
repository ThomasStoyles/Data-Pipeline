import os
import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from fetch_data import fetch_weather

def test_fetch_weather_returns_expected_keys():
    city = "London"
    data = fetch_weather(city)
    # Check top-level keys
    assert "main" in data
    assert "weather" in data
    assert "temp" in data["main"]
    assert isinstance(data["main"]["temp"], (float, int))
    assert isinstance(data["weather"], list)

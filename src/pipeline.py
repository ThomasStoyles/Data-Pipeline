from fetch_data import fetch_weather
from store_data import create_table, store_weather

def main():
    create_table()
    city = "London"  # You can try with more cities later!
    data = fetch_weather(city)
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]
    store_weather(city, temp, humidity, description)
    print(f"Stored weather for {city}: {temp}°C, {humidity}% humidity, {description}")

if __name__ == "__main__":
    main()

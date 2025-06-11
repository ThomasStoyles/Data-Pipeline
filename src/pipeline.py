from fetch_data import fetch_weather
from fetch_crypto import fetch_crypto_price
from store_data import create_weather_table, store_weather, create_crypto_table, store_crypto_price

def main():
    create_weather_table()
    create_crypto_table()
    
    # Weather data
    city = "London"
    weather_data = fetch_weather(city)
    temp = weather_data["main"]["temp"]
    humidity = weather_data["main"]["humidity"]
    description = weather_data["weather"][0]["description"]
    store_weather(city, temp, humidity, description)
    print(f"Stored weather for {city}: {temp}°C, {humidity}% humidity, {description}")

    # Crypto data
    for coin in ["bitcoin", "ethereum"]:
        crypto_data = fetch_crypto_price(coin, "usd")
        price = crypto_data[coin]["usd"]
        store_crypto_price(coin, "usd", price)
        print(f"Stored {coin} price: ${price} USD")

if __name__ == "__main__":
    main()

import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

def get_mysql_connection():
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST"),
        port=int(os.getenv("MYSQL_PORT")),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DB"),
        auth_plugin='mysql_native_password'  # Add this if you get auth errors
    )

def create_weather_table():
    conn = get_mysql_connection()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS weather (
            id INT AUTO_INCREMENT PRIMARY KEY,
            city VARCHAR(255),
            temperature FLOAT,
            humidity INT,
            description VARCHAR(255),
            fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    cur.close()
    conn.close()

def store_weather(city, temp, humidity, description):
    conn = get_mysql_connection()
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO weather (city, temperature, humidity, description)
        VALUES (%s, %s, %s, %s)
    ''', (city, temp, humidity, description))
    conn.commit()
    cur.close()
    conn.close()

def create_crypto_table():
    conn = get_mysql_connection()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS crypto (
            id INT AUTO_INCREMENT PRIMARY KEY,
            coin_id VARCHAR(255),
            currency VARCHAR(10),
            price FLOAT,
            fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    cur.close()
    conn.close()

def store_crypto_price(coin_id, currency, price):
    conn = get_mysql_connection()
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO crypto (coin_id, currency, price)
        VALUES (%s, %s, %s)
    ''', (coin_id, currency, price))
    conn.commit()
    cur.close()
    conn.close()

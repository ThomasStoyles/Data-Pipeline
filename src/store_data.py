import sqlite3

def create_table(db_path='weather.db'):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS weather (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT,
            temperature REAL,
            humidity INTEGER,
            description TEXT,
            fetched_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def store_weather(city, temp, humidity, description, db_path='weather.db'):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''
        INSERT INTO weather (city, temperature, humidity, description)
        VALUES (?, ?, ?, ?)
    ''', (city, temp, humidity, description))
    conn.commit()
    conn.close()

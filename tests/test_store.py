import os
import sqlite3
import tempfile
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from store_data import create_table, store_weather


def test_store_weather_creates_and_inserts():

    with tempfile.TemporaryDirectory() as tmpdirname:
        db_path = os.path.join(tmpdirname, "test_weather.db")
        create_table(db_path)
        store_weather("Testville", 12.3, 45, "clear sky", db_path)


        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        c.execute("SELECT city, temperature, humidity, description FROM weather WHERE city = ?", ("Testville",))
        row = c.fetchone()
        conn.close()
        
        assert row is not None
        assert row[0] == "Testville"
        assert row[1] == 12.3
        assert row[2] == 45
        assert row[3] == "clear sky"
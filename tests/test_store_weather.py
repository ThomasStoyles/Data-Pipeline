import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from store_data import get_mysql_connection, create_weather_table, store_weather

def test_store_weather_inserts_mysql():
    conn = get_mysql_connection()
    cur = conn.cursor()
    create_weather_table()
    # Clean before test
    cur.execute("DELETE FROM weather WHERE city = 'TestCity'")
    conn.commit()
    # Test insert
    store_weather("TestCity", 12.34, 56, "sunny")
    cur.execute("SELECT city, temperature, humidity, description FROM weather WHERE city = 'TestCity'")
    row = cur.fetchone()
    # Clean after test
    cur.execute("DELETE FROM weather WHERE city = 'TestCity'")
    conn.commit()
    cur.close()
    conn.close()
    assert row is not None
    assert row[0] == "TestCity"
    assert abs(row[1] - 12.34) < 0.001
    assert row[2] == 56
    assert row[3] == "sunny"

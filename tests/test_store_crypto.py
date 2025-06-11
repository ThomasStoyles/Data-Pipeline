import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from store_data import get_mysql_connection, create_crypto_table, store_crypto_price

def test_store_crypto_price_inserts_mysql():
    conn = get_mysql_connection()
    cur = conn.cursor()
    create_crypto_table()
    # Clean before test
    cur.execute("DELETE FROM crypto WHERE coin_id = 'testcoin'")
    conn.commit()
    # Test insert
    store_crypto_price("testcoin", "usd", 1000.0)
    cur.execute("SELECT coin_id, currency, price FROM crypto WHERE coin_id = 'testcoin'")
    row = cur.fetchone()
    # Clean after test
    cur.execute("DELETE FROM crypto WHERE coin_id = 'testcoin'")
    conn.commit()
    cur.close()
    conn.close()
    assert row is not None
    assert row[0] == "testcoin"
    assert row[1] == "usd"
    assert row[2] == 1000.0

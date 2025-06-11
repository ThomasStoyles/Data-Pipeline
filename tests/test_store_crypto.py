import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
import sqlite3
import tempfile
from store_data import create_crypto_table, store_crypto_price

def test_store_crypto_price_inserts_correctly():
    with tempfile.TemporaryDirectory() as tmpdirname:
        db_path = os.path.join(tmpdirname, "test_crypto.db")
        create_crypto_table(db_path)
        store_crypto_price("bitcoin", "usd", 12345.67, db_path)

        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        c.execute("SELECT coin_id, currency, price FROM crypto WHERE coin_id = ?", ("bitcoin",))
        row = c.fetchone()
        conn.close()

        assert row is not None
        assert row[0] == "bitcoin"
        assert row[1] == "usd"
        assert row[2] == 12345.67

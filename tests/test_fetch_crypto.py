import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from fetch_crypto import fetch_crypto_price

def test_fetch_crypto_price_bitcoin():
    data = fetch_crypto_price("bitcoin", "usd")
    assert "bitcoin" in data
    assert "usd" in data["bitcoin"]
    assert isinstance(data["bitcoin"]["usd"], (float, int))

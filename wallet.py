from explain import explain_transaction

import os
import requests
from dotenv import load_dotenv

load_dotenv()

ETHERSCAN_API_KEY = os.getenv("ETHERSCAN_API_KEY")

def get_latest_txs(wallet_address, count=5):
    url = "https://api.etherscan.io/api"
    params = {
        "module": "account",
        "action": "txlist",
        "address": wallet_address,
        "startblock": 0,
        "endblock": 99999999,
        "sort": "desc",
        "apikey": ETHERSCAN_API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    if data["status"] != "1":
        raise Exception(f"Etherscan API error: {data['message']}")

    return data["result"][:count]

# ✅ Quick test
if __name__ == "__main__":
    wallet = "0x742d35Cc6634C0532925a3b844Bc454e4438f44e"  # Bitfinex example
    txs = get_latest_txs(wallet)
    for tx in txs:
        from_addr = tx["from"]
        to_addr = tx["to"]
        value = int(tx["value"]) / 1e18
        print(f"From: {from_addr}, To: {to_addr}, Value: {value:.4f} ETH")

        explanation = explain_transaction(tx)
        print(f"\n🧠 AI Explanation:\n{explanation}")
        print("-" * 60)





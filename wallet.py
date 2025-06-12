import os
import requests
from dotenv import load_dotenv
from collections import Counter
from explain import explain_transaction, classify_behavior
from memory import store_summary, find_similar_summaries
from memory import store_summary, find_similar_summaries, has_seen_tag_before

load_dotenv()

ETHERSCAN_API_KEY = os.getenv("ETHERSCAN_API_KEY")

def get_latest_txs(wallet_address, count=3):
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

# ✅ Run the program
if __name__ == "__main__":
    wallet = "0x742d35Cc6634C0532925a3b844Bc454e4438f44e"  # Bitfinex example
    txs = get_latest_txs(wallet)
    tag_counts = Counter()

    for tx in txs:
        from_addr = tx["from"]
        to_addr = tx["to"]
        value = int(tx["value"]) / 1e18
        print(f"From: {from_addr}, To: {to_addr}, Value: {value:.4f} ETH")

        explanation = explain_transaction(tx)
        print(f"\n🧠 AI Explanation:\n{explanation}")

        tag = classify_behavior(explanation)
        print(f"🏷️ Behavior Tag: {tag}")
        tag_counts[tag] += 1

        if not has_seen_tag_before(wallet, tag):
            print(f"🚨 New Behavior Detected: This wallet has never shown behavior '{tag}' before!")


        similar = find_similar_summaries(explanation)
        if similar and similar[0]:
            print("🔁 Similar Past Behaviors Found:")
            for s in similar[0]:
                print(f"– {s}")
        else:
            print("📂 No similar behavior found.")

        store_summary(wallet, explanation, tag=tag)

        print("-" * 60)

    # ✅ Summary table at the end
    print("\n🧾 Behavior Breakdown:")
    for tag, count in tag_counts.items():
        print(f"- {tag}: {count}")
    
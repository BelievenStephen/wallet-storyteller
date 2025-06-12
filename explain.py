import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def explain_transaction(tx):
    from_address = tx["from"]
    to_address = tx["to"]
    value_eth = int(tx["value"]) / 1e18
    gas = tx["gas"]
    input_data = tx["input"]

    prompt = f"""
You are a blockchain analyst. Explain this Ethereum transaction in simple English:

From: {from_address}
To: {to_address}
Amount: {value_eth:.4f} ETH
Gas Used: {gas}
Input Data: {input_data}

Keep it beginner-friendly and concise.
"""

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.5
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error explaining transaction: {e}"


def classify_behavior(explanation):
    """Classify the transaction behavior based on its explanation"""
    prompt = f"""
You are a blockchain analyst. Classify this transaction based on its explanation.

Explanation:
"{explanation}"

Choose one of the following tags that best fits:
- Token Swap
- NFT Mint
- Approval
- Bridge
- Large ETH Transfer
- Deposit to CEX
- Smart Contract Interaction
- Unknown

Respond with only the tag.
"""

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Tagging error: {e}"

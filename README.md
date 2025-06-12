# 🧠 Wallet Storyteller

A mini AI tool that explains and tracks Ethereum wallet behavior using OpenAI, Web3, and ChromaDB.

---

## 🧩 What It Does

**Wallet Storyteller** pulls the last 5 transactions from any Ethereum wallet and explains them in plain English using AI. It also uses vector memory to compare each new transaction to past behavior, helping you detect patterns or unusual activity.

---

## 🔍 Example Output

```bash
From: 0x742...f44e → To: 0x771...5ec
Value: 50000.0000 ETH

🧠 AI Explanation:
This transaction sent 50,000 ETH from one wallet to another with no input data.

🔁 Similar Past Behaviors:
– This transaction sent 50,000 ETH...
– This transaction sent 0 ETH with contract input...
```

------------------------------------------------------------
## 🧠 Stack

- **Python 3.10+**
- **[Web3.py](https://web3py.readthedocs.io/)** – fetch Ethereum transactions via Etherscan API
- **[OpenAI API](https://platform.openai.com/docs)** – GPT-powered natural language summaries
- **[ChromaDB](https://docs.trychroma.com/)** – store and compare summaries using vector embeddings
- **`python-dotenv`** – securely load environment variables

---

## 🚀 How to Run

### 1. Clone the repo

```bash
git clone https://github.com/BelievenStephen/wallet-storyteller.git
cd wallet-storyteller
```

### 2. Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Add your .env file:

```bash
ETHERSCAN_API_KEY=your_key_here
OPENAI_API_KEY=your_key_here
```

### 4. Run it:

```bash
python3 wallet.py
```

---


🛠 More Features Coming Soon

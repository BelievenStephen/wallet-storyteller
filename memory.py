import chromadb
from chromadb.config import Settings


client = chromadb.Client(Settings())

# Create (or get) a collection for wallet summaries
collection = client.get_or_create_collection(name="wallet_history")

def store_summary(wallet_address, explanation):
    """Store a transaction summary for a given wallet"""
    collection.add(
        documents=[explanation],
        ids=[f"{wallet_address}_{hash(explanation)}"]
    )

def find_similar_summaries(explanation, n=3):
    """Find similar past behaviors based on explanation"""
    results = collection.query(
        query_texts=[explanation],
        n_results=n
    )
    return results["documents"]

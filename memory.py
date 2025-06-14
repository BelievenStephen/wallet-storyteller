import chromadb
from chromadb.config import Settings


client = chromadb.Client(Settings())

# Create (or get) a collection for wallet summaries
collection = client.get_or_create_collection(name="wallet_history")

def store_summary(wallet_address, explanation, tag=None):
    metadata = {"tag": tag} if tag else {}
    collection.add(
        documents=[explanation],
        ids=[f"{wallet_address}_{hash(explanation)}"],
        metadatas=[metadata]
    )


def find_similar_summaries(explanation, n=3):
    """Find similar past behaviors based on explanation"""
    results = collection.query(
        query_texts=[explanation],
        n_results=n
    )
    return results["documents"]

def has_seen_tag_before(wallet_address, tag):
    """Check if this wallet has ever used this tag before"""
    results = collection.query(
        query_texts=[tag],
        where={"tag": tag},
        n_results=1
    )
    return len(results["documents"][0]) > 0 if results["documents"] else False

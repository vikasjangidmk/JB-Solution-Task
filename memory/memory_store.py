
import os
import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer

class MemoryStore:
    """Simple vector memory built on ChromaDB for agent recollection across tasks."""
    def __init__(self, persist_dir: str = "./.memory", collection: str = "agent_memory", model_name: str = None):
        os.makedirs(persist_dir, exist_ok=True)
        self.client = chromadb.PersistentClient(path=persist_dir, settings=Settings(anonymized_telemetry=False))
        self.collection = self.client.get_or_create_collection(name=collection, metadata={"hnsw:space": "cosine"})
        self.model = SentenceTransformer(model_name or os.getenv("EMBEDDING_MODEL","sentence-transformers/all-MiniLM-L6-v2"))
    
    def embed(self, texts):
        return self.model.encode(texts, normalize_embeddings=True).tolist()
    
    def add(self, text: str, metadata: dict=None, doc_id: str=None):
        embeddings = self.embed([text])
        self.collection.add(documents=[text], embeddings=embeddings, ids=[doc_id or str(hash(text))], metadatas=[metadata or {}])
    
    def query(self, query: str, k: int = 5):
        emb = self.embed([query])
        res = self.collection.query(query_embeddings=emb, n_results=k)
        out = []
        for doc, meta, dist in zip(res.get("documents",[[]])[0], res.get("metadatas",[[]])[0], res.get("distances",[[]])[0]):
            out.append({"text": doc, "metadata": meta, "similarity": 1 - dist if dist is not None else None})
        return out

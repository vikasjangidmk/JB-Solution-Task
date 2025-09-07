from crewai.tools import BaseTool
from typing import Optional
from memory.memory_store import MemoryStore

_store = MemoryStore()


class WriteMemoryTool(BaseTool):
    name: str = "write_memory"
    description: str = "Store an important fact, URL, or insight for later retrieval."

    def _run(self, text: str, topic: Optional[str] = None) -> str:
        """Save text into persistent memory with an optional topic tag."""
        _store.add(text, metadata={"topic": topic or "general"})
        return "✅ Saved to memory."


class ReadMemoryTool(BaseTool):
    name: str = "read_memory"
    description: str = "Retrieve the most relevant memories for a given query."

    def _run(self, query: str, k: int = 5) -> str:
        """Fetch top-k relevant memories based on semantic similarity."""
        results = _store.query(query, k=k)
        if not results:
            return "⚠️ No relevant memory found."
        return "\n".join([f"- {r['text']} (meta={r['metadata']})" for r in results])

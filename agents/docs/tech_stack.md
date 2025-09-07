
# Tech Stack Justification

- **CrewAI**: Lightweight multi-agent orchestration with task handoff.
- **crewai-tools (SerperDevTool)**: Reliable Google-like web search; we also add a **DuckDuckGo fallback** to avoid hard failures.
- **ChromaDB + sentence-transformers**: Simple, local, and fast **vector memory** for cross-task recall.
- **Loguru**: Clean logging with rotation for traceability of autonomous steps.
- **Streamlit**: Minimal UI to run jobs, inspect **final reports**, **memory**, and **logs**.
- **Python-dotenv**: Configuration via `.env` as standard practice.

> Models (example)
- Research: `groq/llama-3.1-70b-versatile` (strong reasoning)
- Analysis/Writer: `groq/llama-3.1-8b-instant` (fast, cost-effective)

> Swappable
- Swap Groq with OpenAI (`openai/gpt-4o-mini`) by changing env vars.
- Replace Chroma with Pinecone by implementing the same `MemoryStore` interface.

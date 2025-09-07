import os, json, requests
from crewai.tools import BaseTool
from crewai_tools import SerperDevTool


class SafeSerperTool(SerperDevTool):
    """Wrapper that reads SERPER_API_KEY from env and gracefully fails."""
    def __init__(self):
        api_key = os.getenv("SERPER_API_KEY", "")
        super().__init__(serper_api_key=api_key)


class DuckDuckGoTool(BaseTool):
    name: str = "duckduckgo_search"
    description: str = (
        "Lightweight web search using DuckDuckGo HTML (fallback when Serper is unavailable)."
    )

    def _run(self, query: str, max_results: int = 5) -> str:
        url = "https://duckduckgo.com/html/"
        resp = requests.post(url, data={"q": query}, timeout=20)
        if resp.status_code != 200:
            return "Search failed."

        items = []
        for line in resp.text.splitlines():
            if 'result__a' in line and 'href="' in line:
                href = line.split('href="')[1].split('"')[0]
                title = line.split('>')[1].split('<')[0]
                items.append({"title": title, "link": href})
                if len(items) >= max_results:
                    break

        return json.dumps(items, ensure_ascii=False, indent=2)

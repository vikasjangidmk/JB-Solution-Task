import os
from crewai import Agent, LLM
from tools.memory_tools import WriteMemoryTool, ReadMemoryTool
from tools.web_tools import SafeSerperTool, DuckDuckGoTool

# LLM configurations - Agent specific config
model = os.getenv("RESEARCH_AGENT_LLM", "openai/gpt-4o")
temperature = float(os.getenv("RESEARCH_AGENT_TEMPERATURE", "0.2"))

llm = LLM(
    model=model,
    temperature=temperature
)

research_specialist_agent = Agent(
    role="Research Specialist",
    goal="Gather comprehensive and accurate information on given topics from multiple sources",
    backstory=(
        "You are an expert research specialist with years of experience in information gathering "
        "and fact-checking. You have a keen eye for reliable sources and can quickly identify the "
        "most relevant and up-to-date information on any topic."
    ),
    llm=llm,
    tools=[
        SafeSerperTool(),     # primary web search
        DuckDuckGoTool(),     # backup search
        WriteMemoryTool(),    # save useful findings
        ReadMemoryTool(),     # recall past knowledge
    ],
    verbose=True,
)

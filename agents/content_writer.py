import os
from crewai import Agent, LLM
from crewai_tools import FileWriterTool
from tools.memory_tools import WriteMemoryTool, ReadMemoryTool  


# LLM configurations - Agent specific config
model = os.getenv("WRITER_AGENT_LLM","openai/gpt-4o")
temperature = float(os.getenv("WRITER_AGENT_TEMPERATURE","0.2"))

llm = LLM(
    model=model,
    temperature=temperature
)

content_writer_agent = Agent(
    role="Content Writer",
    goal="Create comprehensive, well-structured reports and summaries",
    backstory=(
        "You are a professional content writer with expertise in creating "
        "clear, engaging, and well-structured documents. You can transform complex "
        "information into accessible and compelling content."
    ),
    llm=llm,
    tools=[FileWriterTool(), WriteMemoryTool(), ReadMemoryTool()],
    verbose=True,
)

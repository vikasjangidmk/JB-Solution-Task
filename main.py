from dotenv import load_dotenv
from loguru import logger
from datetime import datetime
import sys
from crew import research_crew

load_dotenv()

logger.add("logs/run_{time}.log", rotation="1 MB", retention=10)

def run(topic: str):
    logger.info(f"Starting run for topic: {topic}")
    result = research_crew.kickoff(inputs={"topic": topic})
    logger.success("Run completed.")
    print("-" * 50)
    print(result)
    print("-" * 50)
    sys.exit(0)   # ✅ ensures program stops after one run

if __name__ == "__main__":
    topic = "Top React Native libraries in 2025"
    run(topic)

from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv

load_dotenv()

finance_agent = Agent(
    name="Finance Agent",
    model=Groq(id="meta-llama/llama-4-scout-17b-16e-instruct"),
    instructions=[
        "Provide:",
        "1. Analyst recommendation summary",
        "2. Latest news headlines",
        "3. Include approximate sources",
        "4. Format financial data in tables if useful"
    ],
    markdown=True,
    stream=False
)

if __name__ == "__main__":
    finance_agent.print_response(
        "Summarize analyst recommendation and latest news for NVDA",
        stream=False
    )
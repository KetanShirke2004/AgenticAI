from phi.agent import Agent
from phi.model.groq import Groq
from phi.playground import Playground, serve_playground_app
from dotenv import load_dotenv

load_dotenv()

# -----------------------------------
# Finance Agent
# -----------------------------------
finance_agent = Agent(
    name="Finance Agent",
    model=Groq(id="meta-llama/llama-4-scout-17b-16e-instruct"),
    instructions=[
        "When asked about stocks:",
        "1. Provide analyst recommendation summary",
        "2. Provide latest news headlines",
        "3. Include approximate sources",
        "4. Format financial data in tables when useful"
    ],
    markdown=True,
    stream=False  # ✅ Keep this
)

# -----------------------------------
# Playground Setup (NO stream param)
# -----------------------------------
app = Playground(agents=[finance_agent]).get_app()

# -----------------------------------
# Run Server
# -----------------------------------
if __name__ == "__main__":
    serve_playground_app("playground:app", reload=False)
import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, LLM
from crewai.tools import tool

load_dotenv()

# 1. Use your working LLM block from main.py (Option A or B)
llm = LLM(
      model=f"openai/{os.environ['AZURE_DEPLOYMENT']}",
        api_key=os.environ["AZURE_API_KEY"],
        base_url=os.environ["AZURE_API_BASE"],
        api="responses",
)

# 2. Tool (fake data for now)
# Why: Provides a simple poll-data lookup so the assistant can answer questions with real-looking data instead of guessing.
# How: Accepts a poll ID, checks a local dictionary for that key, and returns the result as a string so the CrewAI tool contract stays consistent.
@tool("Get poll results")
def get_poll_results(poll_id: str) -> str:
    """Return vote counts for a poll. Input: poll_id, e.g. 'p1'."""
    fake_db = {"p1": {"Chai": 120, "Coffee": 80}}
    return str(fake_db.get(poll_id, "poll not found"))

# 3. Agent
assistant = Agent(
    role="Poll Assistant",
    goal="Chat helpfully about polls and use the tool for real data",
    backstory="A friendly assistant. Never invent poll numbers; use the tool.",
    tools=[get_poll_results],
    llm=llm,
)

# 4. One task, reused every turn
task = Task(
    description=(
        "Conversation so far:\n{history}\n\n"
        "User's new message: {message}\n\n"
        "Reply to the new message. Use the tool when poll data is needed."
    ),
    expected_output="A short, friendly reply",
    agent=assistant,
)

formated_task = Task(
    description=(
        "Turn the output into Modi's style"
    ),
    expected_output="A short, friendly reply in Modi    's style",
    agent=assistant,
    context=[task]
)

crew = Crew(agents=[assistant], tasks=[formated_task])

# 5. Chat loop
# Why: Keeps the conversation alive so the agent can respond to repeated user messages while remembering recent context.
# How: Reads each input, trims and filters empty/exit commands, builds a short recent-history summary, calls the CrewAI workflow with that context, and stores the latest exchange before printing the answer.
def chat():
    history = []
    print("Poll assistant ready. Type 'exit' to quit. Try: who is winning poll p1?")
    while True:
        user = input("\nYou: ").strip()
        if user.lower() in {"exit", "quit"}:
            break
        if not user:
            continue

        recent = "\n".join(history[-6:]) or "(none)"   # last 3 exchanges
        reply = crew.kickoff(inputs={"history": recent, "message": user}).raw

        history += [f"User: {user}", f"Assistant: {reply}"]
        print(f"\nBot: {reply}")

if __name__ == "__main__":
    chat()
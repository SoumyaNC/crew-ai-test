import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM

load_dotenv()  # loads .env from the current directory

# 1. LLM
# llm = LLM(
#     model=f"azure/{os.environ['AZURE_DEPLOYMENT']}",
#     api_key=os.environ["AZURE_API_KEY"],
#     base_url=os.environ["AZURE_API_BASE"],
#     api_version=os.getenv("AZURE_API_VERSION", "2024-08-01-preview"),
# )

llm = LLM(
    model=f"openai/{os.environ['AZURE_DEPLOYMENT']}",
    api_key=os.environ["AZURE_API_KEY"],
    base_url=os.environ["AZURE_API_BASE"],
    api="responses",
)

# 2. Agents
researcher = Agent(
    role="Researcher",
    goal="Find 3 key facts about the given topic",
    backstory="A concise analyst who values accuracy.",
    llm=llm,
)

writer = Agent(
    role="Writer",
    goal="Turn facts into a short, clear paragraph",
    backstory="A technical writer who hates fluff.",
    llm=llm,
)

# 3. Tasks
research_task = Task(
    description="Research the topic: {topic}",
    expected_output="A bullet list of 3 facts",
    agent=researcher,
)

write_task = Task(
    description="Write a 3-sentence summary using the research",
    expected_output="One short paragraph",
    agent=writer,
    context=[research_task],
)

# 4. Crew
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, write_task],
    process=Process.sequential,
)

if __name__ == "__main__":
    result = crew.kickoff(inputs={"topic": "community polling platforms"})
    print(result.raw)
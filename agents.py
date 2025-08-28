from swarms import Agent, InteractiveGroupChat, round_robin_speaker
from dotenv import load_dotenv

# Load the environment variables
load_dotenv()


overview_agent = Agent(
    agent_name="Overview Agent",
    agent_description="Your job is to provide an overview of the user's query.",
    system_prompt="You are a helpful assistant that answers the user's query comprehensively in bullet points.",
    model_name="gpt-4.1",
)

pros_cons_agent = Agent(
    agent_name="Pros & Cons Agent",
    agent_description="Your job is to provide the user with the pros and cons of their query.",
    system_prompt="You are a helpful assistant that answers the user's query comprehensively in bullet points.",
    model_name="gpt-4.1",
)

practical_agent = Agent(
    agent_name="Practical Agent",
    agent_description="Your job is to provide a technical, economical, environmental, and socially feasibility report on the user's query.",
    system_prompt="You are a helpful assistant that answers the user's query comprehensively in bullet points, keeping the other agents' viewpoints in mind.",
    model_name="gpt-4.1",
)

expert_agent = Agent(
    agent_name="Expert Agent",
    agent_description="Your job is to provide an expert opinion on the user's query, keeping other agents' viewpoints in view.",
    system_prompt="You are an expert in the user's query's field that answers the user's query comprehensively in bullet points.",
    model_name="gpt-4.1",
)

workflow = InteractiveGroupChat(
    name="The Council",
    agents=[overview_agent, pros_cons_agent, practical_agent, expert_agent],
    interactive=True,
    speaker_function=round_robin_speaker
)

# history = workflow.run("I'm having thoughts of building a Formula 1 car.")
# print(history)
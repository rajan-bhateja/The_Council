from swarms import Agent, InteractiveGroupChat, round_robin_speaker
from dotenv import load_dotenv

# Load the environment variables
load_dotenv()

model_name = "gpt-4o-mini"

overview_agent = Agent(
    agent_name="Overview",
    agent_description="Your job is to provide an overview of the user's query.",
    system_prompt="""Summarize the user’s query in clear, simple bullet points.
                    Highlight the main aspects and provide a detailed understanding of the overall idea.
                    Don't mention the completion of your task and the remaining tasks.
                    Be direct and user-friendly without describing your role.""",
    model_name=model_name,
)

pros_cons_agent = Agent(
    agent_name="Pros & Cons",
    agent_description="Your job is to provide the user with the pros and cons of their query.",
    system_prompt="""List the advantages and disadvantages of the user’s query in bullet points.
                    Keep it balanced, comprehensive, and practical.
                    Avoid repeating the overview.
                    Do not mention that you are ‘weighing pros and cons’—just present them naturally.
                    Do not mention the remaining tasks.""",
    model_name=model_name,
)

practical_agent = Agent(
    agent_name="Practical",
    agent_description="Your job is to provide a technical, economical, environmental, and socially feasibility report on the user's query.",
    system_prompt="""Evaluate the feasibility of the user’s query from technical, economic, environmental, and social perspectives.
                    Use bullet points and focus on actionable insights.
                    Do not mention that you are considering other agents—just provide a grounded assessment.
                    Do not mention that the completion of your task and the remaining tasks.""",
    model_name=model_name,
)

expert_agent = Agent(
    agent_name="Expert",
    agent_description="Your job is to provide an expert opinion on the user's query, keeping other agents' viewpoints in view.",
    system_prompt="""Provide an expert-level opinion on the user’s query.
                    Offer advanced insights, best practices, and recommendations in bullet points.
                    Do not mention that you are an expert—just explain the most important technical details and next steps clearly.
                    Do not mention the tasks done by other agents and the remaining tasks.""",
    model_name=model_name,
)

arbitrator_agent = Agent(
    agent_name="Arbitrator",
    agent_description="Your job is to provide a final recommendation on the user's query based on other agents' viewpoints.",
    system_prompt="""Read the responses from the other agents and provide a final, clear, and natural conclusion.
                    Summarize the key insights, highlight any trade-offs, and give the user a simple, actionable recommendation.
                    Do not describe your role, do not mention other agents, and avoid formal phrases like ‘I have synthesized’.
                    Speak directly to the user as if you’re giving them the best next step.""",
    model_name=model_name,
)

workflow = InteractiveGroupChat(
    name="The Council",
    agents=[overview_agent, pros_cons_agent, practical_agent, expert_agent, arbitrator_agent],
    interactive=True,
    speaker_function=round_robin_speaker
)

# history = workflow.run("I'm having thoughts of building a Formula 1 car.")
# print(history)
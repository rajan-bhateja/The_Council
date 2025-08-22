from swarms import Agent, ConcurrentWorkflow
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_mistralai import ChatMistralAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

# Load the environment variables
load_dotenv()

# Define different LLMs
openai_llm = ChatOpenAI(model="gpt-5o-mini")
gemini_llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
groq_llm = ChatGroq(model="moonshotai/kimi-k2-instruct")
mistral_llm = ChatMistralAI(model="mistral-large-latest")
hf_llm = ChatHuggingFace(llm=HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V3",
    task="text-generation",
    provider="auto",
))

openai_agent = Agent(
    agent_name="OpenAI Agent",
    agent_description="",
    system_prompt="You are a helpful assistant that answers the user's query concisely in bullet points."
)

gemini_agent = Agent(
    agent_name="Gemini Agent",
    agent_description="",
    system_prompt="You are a helpful assistant that answers the user's query concisely in bullet points."
)

mistral_agent = Agent(
    agent_name="Mistral Agent",
    agent_description="",
    system_prompt="You are a helpful assistant that answers the user's query concisely in bullet points."
)

groq_agent = Agent(
    agent_name="Groq Agent",
    agent_description="",
    system_prompt="You are a helpful assistant that answers the user's query concisely in bullet points."
)

hf_agent = Agent(
    agent_name="HF Agent",
    agent_description="",
    system_prompt="You are a helpful assistant that answers the user's query concisely in bullet points."
)

workflow = ConcurrentWorkflow(
    name="The Council",
    agents=[openai_agent, gemini_agent, mistral_agent, groq_agent, hf_agent],
    show_dashboard=True
)
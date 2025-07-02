from agents import Agent,AsyncOpenAI, OpenAIChatCompletionsModel, Runner, set_tracing_disabled
from dotenv import load_dotenv
import os

def agent(chat_history):
    load_dotenv()

    gemini_api_key = os.getenv("GEMINI_API_KEY")

    client = AsyncOpenAI(
api_key=gemini_api_key,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    )

    set_tracing_disabled(disabled=True)

    agent = Agent(
        name="Chatbot",
        instructions = (
    "You are Muhammad Sharjeel Asif chatting with your friend casually on WhatsApp. The chat is in a mix of Urdu and English. Read the full conversation and identify the name of the friend you're replying to from the chat history. Respond informally and naturally as if you are continuing the conversation. Don't repeat what has already been said. Only reply with the next appropriate message from Sharjeel based on the last message. Do not explain, summarize, or analyze — just continue the chat like a real person would. Use the friend's name if appropriate, based on the context in the conversation. it should be some how respectful. If the friend name is mommy or pappa, be respectful as they my parents."
),
        model=OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=client),
    )

    result = Runner.run_sync(
            agent,
            chat_history,
    )

    return result.final_output
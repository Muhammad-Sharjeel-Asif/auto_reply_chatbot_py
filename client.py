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


def is_last_message_from_friend(chat_history: str, your_name: str) -> bool:
    # Clean and split lines
    lines = [line.strip() for line in chat_history.strip().split("\n") if line.strip()]
    
    for line in reversed(lines):
        if "]" in line and ":" in line:
            try:
                # Extract name part: [time, date] Name: Message
                name_part = line.split("]")[1].split(":")[0].strip()
                # Compare ignoring case
                if name_part.lower() != your_name.lower():
                    return True
                else:
                    return False
            except Exception:
                continue  # Skip malformed line
    return False
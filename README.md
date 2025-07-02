# 🤖 Auto-Reply Chatbot for WhatsApp Desktop

An intelligent auto-reply chatbot that simulates natural, respectful conversations in **Urdu + English** using **Gemini AI**.  
This Python-based assistant reads your WhatsApp Desktop chat window, understands the latest messages, and responds like a human — automatically.

---

## 🧠 Features

- 🪄 **Automated WhatsApp Replies**  
  Auto-copies chat messages from the screen and replies directly in the input field.

- 💬 **AI-Powered Conversations**  
  Integrates Gemini (`gemini-2.0-flash`) to generate fluent, human-like responses.

- 🧠 **Context-Aware Understanding**  
  Reads entire conversation history and replies naturally based on context and speaker.

- 🎯 **Mixed Urdu-English Support**  
  Trained for casual, bilingual (Urdu-English) chatting — respectful and personalized.

- 💻 **GUI Automation with PyAutoGUI**  
  Simulates user interaction (mouse/keyboard) to control WhatsApp Desktop seamlessly.

---

## 🛠️ Tech Stack

- Python 3.x
- [PyAutoGUI](https://pypi.org/project/PyAutoGUI/)
- [Pyperclip](https://pypi.org/project/pyperclip/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [OpenAI SDK](https://platform.openai.com/)
- Gemini (via OpenAI SDK + custom base URL)

---

## ⚙️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Muhammad-Sharjeel-Asif/auto_reply_chatbot_py.git
cd auto_reply_chatbot_py

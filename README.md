# Telegram Bot 'eKömek' with KazLLM API

This is a Telegram bot built with **Aiogram** that integrates with the **KazLLM API** for natural language responses in Kazakh, Russian, and English. The bot also supports **Soyle API** for handling voice messages.

Link to bot:[@ekomek_bot](https://t.me/ekomek_bot)

## Legal Expertise

The 'eKömek' bot serves as a virtual expert on the legislation of the Republic of Kazakhstan. Its purpose is to provide general legal recommendations to users in Kazakh, Russian, and English languages. All responses are based on the current laws of the Republic of Kazakhstan. When responding, the bot cites relevant codes, laws, and articles, quoting their content when necessary.

If a user’s question is unclear or lacks sufficient detail, the bot requests clarification. If the bot does not have enough information for an accurate response, it will advise the user to consult a professional lawyer.

The responses are neutral, accurate, and follow the legal terminology accepted in the Republic of Kazakhstan. Please note that the information provided by the bot is for reference purposes only and does not replace full legal consultation.

## Features

- 🗣️ **Voice Recognition Integration Soyle App:** Processes and converts voice messages to text.
- 💬 **KazLLM Integration:** Generates responses using KazLLM API.
- 🌐 **Multilingual Support:** Supports Kazakh, Russian, Englsih languages.
- ⚙️ **Easy Configuration:** Uses environment variables for settings.

## Installation

### Prerequisites

- Python 3.9+
- Install dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Setup

Create a `.env` file with your API keys:

```env
TOKEN=<Your Telegram Bot Token>
API_RESPONSE=<Your KazLLM API Key>
API_SOYLE=<Your Soyle API Key>
```

## Usage

Run the bot:

```bash
python e_app.py
```

The bot supports text and voice commands and replies using the KazLLM API.

## Project Structure

```plaintext
├── e_app.py
├── .env
├── config.py
├── README.md
├── requirements.txt
├── modules
│  ├── path
│      ├── logo.png
│      ├── descriptionpicture.jpg
│      ├── logo2.jpg
│      ├── soyle_app.ico
│  ├── bot.py
│  ├── callbacks.py
│  ├── commands.py
│  ├── functions.py
├── api_issai
│   ├── .env
│   ├── add_context.py
│   ├── get_context.py
│   ├── assistant_id.py
│   ├── soyle_tts.py
│   ├── transcription.py
│   ├── interactions.py
```

## To-Do List

- [x] Initialize Telegram bot with Aiogram.
- [x] Set up environment variables for API keys.
- [x] Integrate KazLLM API for responses.
- [x] Add voice message handling.
- [x] Implement language switching command.
- [x] Add unit tests for API calls.
- [ ] Implement file_prompt method to handle file-based instructions.

## License

This project is licensed under the MIT License.

## Contact

For questions or suggestions, please contact:

- https://t.me/aasy1zhaan
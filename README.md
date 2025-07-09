# PII_Identification

A command-line tool for identifying and anonymizing Personally Identifiable Information (PII) in user input using Microsoft Presidio and interacting with LLMs via the Groq API. The project is currently configured for English only and supports custom recognizers for blood types, MAC addresses, medications, and Turkish ID numbers (TCKN).

## Features

- **PII Detection & Anonymization:** Uses Presidio Analyzer and Anonymizer to detect and anonymize PII in user messages.
- **Custom Recognizers:** Extend PII detection with custom recognizers for blood types, MAC addresses, medications, and TCKN.
- **LLM Chat:** Sends anonymized (or original) user messages to a selected LLM model via the Groq API.
- **Command System:** Supports commands for clearing chat history, listing/selecting models, and help.

## Setup

1. **Clone the repository:**
    ```sh
    git clone https://github.com/sbsahan/PII_Identification
    ```

2. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```
    *(Requires Python 3.11+)*

3. **Configure API Keys:**
    - Edit `config.py` and set your Groq API key.

4. **Run the application:**
    ```sh
    python main.py
    ```

## Usage

- **Type your message** and press Enter. The tool will analyze and anonymize PII before sending it to the LLM.
- **If PII is detected**, you can choose to send the original or anonymized message, or cancel sending.
- **Commands:**
    - `!exit` — Exit the chat.
    - `!clear` — Clear chat history.
    - `!models` — List and select available LLM models.
    - `!help` — Show available commands.

## File Structure

- `main.py` — Main application loop and chat logic.
- `config.py` — Configuration for API keys, deny lists, and patterns.
- `commands.py` — Command handling functions.
- `identifiers/` — Custom recognizer classes for PII types.

## Customization

- **Add new recognizers:** Place new recognizer classes in the `identifiers/` folder and register them in `main.py`.
- **Update deny lists or patterns:** Edit `config.py` as needed.

## License

This project is for educational and research purposes. Review and comply with the licenses of Presidio, Groq, and any other dependencies you use.

---

*Created with Python, Presidio, and Groq.*

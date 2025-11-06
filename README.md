# A Context-Aware Conversational Agent

This project is a context-aware conversational agent built using **LangChain**, **OpenRouter**, and **Django**.

## Features
- Detects if user input contains context.
- Searches external sources if context is missing.
- Checks relevance and splits context/question.
- Web UI using Django.

## Run
```bash
pip install -r requirements.txt
python manage.py runserver

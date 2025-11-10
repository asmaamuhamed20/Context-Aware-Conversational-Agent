# Contextia

**Contextia** is an intelligent open-source AI assistant that understands context and provides thoughtful, accurate responses.  
It combines a **FastAPI backend** (built with LangChain & Python) and a **Next.js frontend** for an interactive chat interface.

---

## 🚀 Features
- Context-aware reasoning powered by LangChain  
- FastAPI backend for reliable API responses  
- Next.js frontend with modern UI  
- Integration between frontend and backend via REST  
- Built as part of the **Empowering Energy AI Internship Program**  

---

## 🧠 Tech Stack
- **Backend:** Python, FastAPI, LangChain  
- **Frontend:** React, Next.js  
- **Language Model:** OpenRouter / OpenAI compatible LLMs  

---

## ⚙️ Setup

### Backend
```bash
cd "A Context-Aware Conversational Agent"
source venv/bin/activate
uvicorn agent.agent_runner:app --reload

## Frontend
cd Frontend
npm install
npm run dev
Then open the app at http://localhost:3000.



# AI-Powered Customer Conversation Intelligence Platform

An end-to-end AI platform that analyzes customer conversations using speech transcription, speaker diarization, AI-driven conversation analysis, compliance detection, and interactive dashboards.

---

# Overview

FitNova AI Sales Call Intelligence is a prototype demonstrating how AI can automate the analysis of customer sales conversations.

The application accepts an uploaded audio recording, generates a transcript using Groq Whisper, performs speaker diarization using PyAnnote, redacts sensitive information, evaluates the conversation through an AI workflow, stores structured insights, and presents everything through a modern React dashboard.

This project demonstrates a complete AI pipeline from audio upload to business insights.

---

# Features

- Upload sales call recordings
- Automatic speech-to-text transcription
- Real speaker diarization using PyAnnote
- Advisor / Customer speaker mapping
- PII redaction
- AI-powered sales quality evaluation
- Compliance issue detection
- AI-generated executive summary
- AI-generated recommendations
- Interactive dashboard
- Audio playback
- Conversation timeline
- SQLite database storage
- REST API backend

---

# Tech Stack

## Frontend

- React
- TypeScript
- Vite
- Tailwind CSS
- Axios
- React Router
- Recharts

---

## Backend

- FastAPI
- Python
- SQLAlchemy
- SQLite
- Pydantic

---

## AI Components

- Groq Whisper Large v3
- PyAnnote.audio 3.3
- Hugging Face
- LangGraph
- LLM-powered evaluation pipeline

---

# Project Architecture

```
                 Upload Audio
                      │
                      ▼
             Groq Whisper Large v3
               Speech Transcription
                      │
                      ▼
          PyAnnote Speaker Diarization
                      │
                      ▼
        Advisor / Customer Mapping
                      │
                      ▼
              PII Redaction
                      │
                      ▼
          LangGraph AI Workflow
        ├── Quality Evaluation
        ├── Compliance Analysis
        ├── Call Summary
        └── Recommendations
                      │
                      ▼
              SQLite Database
                      │
                      ▼
             React Dashboard
```

---

# Project Structure

```
fitnova-intelligence/

├── backend/
│
│   ├── app/
│   │
│   ├── agents/
│   ├── api/
│   ├── core/
│   ├── database/
│   ├── schemas/
│   ├── services/
│   │
│   ├── requirements.txt
│   └── seed.py
│
├── frontend/
│
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── vite.config.ts
│
└── README.md
```

---

# Installation

## Backend

Navigate to backend

```bash
cd backend
```

Create virtual environment

```bash
python -m venv venv
```

Activate

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env`

```env
GROQ_API_KEY=your_groq_api_key

GROQ_MODEL=whisper-large-v3

HF_TOKEN=your_huggingface_token
```

Initialize database

```bash
python seed.py
```

Run backend

```bash
uvicorn app.main:app --reload
```

Backend runs on

```
http://localhost:8000
```

---

## Frontend

Navigate to frontend

```bash
cd frontend
```

Install dependencies

```bash
npm install
```

Run frontend

```bash
npm run dev
```

Frontend runs on

```
http://localhost:5173
```

---

# Environment Variables

| Variable | Description |
|-----------|-------------|
| GROQ_API_KEY | Groq API key |
| GROQ_MODEL | Whisper model |
| HF_TOKEN | HuggingFace token for PyAnnote |

---

# End-to-End Workflow

The application processes every uploaded recording through the following pipeline.

1. Upload audio
2. Transcribe using Groq Whisper Large v3
3. Perform speaker diarization using PyAnnote
4. Map speakers to Advisor and Customer
5. Redact sensitive information
6. AI quality evaluation
7. Compliance analysis
8. Generate executive summary
9. Generate recommendations
10. Store structured output in SQLite
11. Display results in dashboard

---

# AI Analysis

The AI workflow evaluates conversations across multiple dimensions.

- Discovery
- Rapport
- Product Knowledge
- Objection Handling
- Closing
- Compliance
- Customer Experience

The system produces:

- Overall Quality Score
- Category Scores
- Executive Summary
- Recommendations
- Compliance Flags

---

# Implemented Components

The following components are fully implemented.

- Audio upload
- Audio playback
- Groq Whisper transcription
- PyAnnote speaker diarization
- Advisor/Customer speaker mapping
- Timestamp alignment
- PII redaction
- AI call evaluation
- Compliance detection
- Executive summaries
- Recommendations
- SQLite persistence
- Interactive dashboard
- REST APIs
- Render backend deployment
- Vercel frontend deployment

---

# Design Decisions

## FastAPI

Selected for its speed, automatic API documentation, and simplicity.

## React + Vite

Provides a fast development workflow and responsive UI.

## Groq Whisper

Offers high-quality speech transcription with very low latency.

## PyAnnote

Chosen for accurate speaker diarization and timestamp alignment.

## SQLite

Used to simplify deployment while keeping the prototype lightweight.

## LangGraph

Provides a structured AI workflow for conversation evaluation.

---

# Trade-offs

To keep the project lightweight and easy to deploy, the following design choices were made.

- SQLite instead of PostgreSQL
- Groq Whisper instead of local Whisper inference
- Prompt-driven evaluation instead of custom ML models
- Heuristic Advisor/Customer mapping on top of PyAnnote diarization

These choices reduce infrastructure complexity while demonstrating the complete AI pipeline.

---

# Known Limitations

- Speaker role mapping may occasionally assign Advisor and Customer incorrectly.
- Very noisy recordings can reduce diarization accuracy.
- AI evaluation quality depends on transcription accuracy.
- Only uploaded recordings are supported.
- Live call processing is not implemented.

---

# Future Improvements

Potential enhancements include:

- Real-time call analysis
- CRM integration
- Multi-language transcription
- Team performance analytics
- Authentication
- PostgreSQL
- Vector database
- Semantic search
- RAG over previous conversations
- Better speaker role classification

---

# Deployment

## Frontend

https://fitnova-intelligence-nine.vercel.app/

---

## Director Dashboard

https://fitnova-intelligence-nine.vercel.app/director

---

## Backend API

https://fitnova-backend-h4uh.onrender.com

---

# Author

## Gowtham K

GitHub

https://github.com/kgowtham590-spec

---

# License

This project was developed as an internship prototype for educational and demonstration purposes.

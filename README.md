# AI Document Assistant

A document question-answering assistant with source citations.

## Current Progress

The project can successfully call the Gemini API from Python.

## Setup

Install the Gemini Python SDK:

```bash
python -m pip install -U google-genai
```

Create an environment variable named:

```text
GEMINI_API_KEY
```

Run the program:

```bash
python first_call.py
```

## Security

The Gemini API key is stored as a GitHub Codespaces Secret.

The real API key is never written in the source code or committed to this repository.

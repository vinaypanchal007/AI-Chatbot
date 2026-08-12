# Archive & Answer — Vue frontend

A Vue 3 + Vite frontend for the FastAPI RAG chatbot backend in the "AI Chatbot"
project. It talks to the existing `POST /chat` endpoint exactly as defined in
`app/routes/chat_route.py`:

- sends `message` (required) and `file` (optional) as `multipart/form-data`
- renders `{ mode: "General Chat", response }` for plain chat
- renders `{ mode: "RAG", response, sources }` for document-grounded answers,
  showing each source as an expandable citation card

## 1. Run the backend

From the FastAPI project root (with its existing virtualenv/dependencies):

```bash
uvicorn app.main:app --reload
```

This serves the API at `http://127.0.0.1:8000` by default.

### Enable CORS (required)

The backend currently has no CORS configuration, so a browser-based frontend
running on a different port (Vite's `5173`) will be blocked. Add this to
`app/main.py`:

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## 2. Run this frontend

```bash
npm install
cp .env.example .env   # adjust VITE_API_BASE_URL if the backend isn't on :8000
npm run dev
```

Open the printed local URL (default `http://localhost:5173`).

## 3. Build for production

```bash
npm run build
```

Outputs static files to `dist/`, which you can serve with any static host or
point FastAPI's `StaticFiles` at.

## Project structure

```
src/
  api.js                 fetch wrapper for POST /chat
  App.vue                page shell, chat state, scrolling
  style.css              design tokens (colors, type) and global resets
  components/
    Sidebar.vue           session ledger: mode, attached doc, message count
    MessageBubble.vue      chat bubble + expandable source/citation cards
    ComposerBar.vue        message input + file attach control
```

## Notes

- File types accepted by the attach button match what the backend's
  `document_processor.py` supports: PDF, DOCX, TXT, and images (OCR via
  `pytesseract`). Adjust the `accept` attribute in `ComposerBar.vue` if that
  changes.
- Uploading a new file re-indexes the vector store per the backend's
  `rag_chat` pipeline (each upload embeds and stores that document's chunks),
  so the "Document" field in the sidebar just reflects the most recently
  attached file for display purposes.
- `sources` in the API response can be plain strings or objects depending on
  `retriever.py`; `MessageBubble.vue` handles both.

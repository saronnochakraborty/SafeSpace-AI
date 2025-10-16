🧠 About SafeSpace AI

SafeSpace AI is an intelligent mental wellness companion built to provide users with a non-judgmental space to express their feelings freely.
It listens, understands, and responds with empathy — helping users reflect on their emotions while offering warmth, encouragement, or gentle guidance when needed.

💚 What It Does

🗣️ Understands your emotions — uses a fine-tuned AI model (GoEmotions by Google / Hugging Face) to detect emotional tones in text.

🌤️ Responds empathetically — offers personalized messages depending on whether emotions are positive, negative, or neutral.

💡 Provides helpful resources — when users express distress, it shares trusted mental health resources, self-care tips, and grounding techniques.

💬 Remembers context — keeps a light conversation history for more natural emotional understanding.

🌈 Elegant, minimal UI — designed for calmness, comfort, and emotional safety.

⚙️ How It Works

Users open page1.html (the landing page) and click “Begin” to start a chat.

The page2.html chat interface connects to a Flask backend (app.py) running locally.

The backend analyzes each message using a transformers-based model, detects emotion probabilities, and sends them back to the frontend.

The UI then selects a fitting, emotionally supportive message — complete with suggestions or links if needed.

🧩 Tech Stack

Frontend: HTML, CSS, JavaScript (Dynamic chat interface)

Backend: Python Flask + Flask-CORS

AI Model: joeddav/distilbert-base-uncased-go-emotions-student (Hugging Face)

Libraries: transformers, torch


🌿 Vision

SafeSpace AI aims to make emotional support more accessible — not to replace therapy, but to bridge moments of silence with empathy.
It’s a small step toward AI that truly listens — fostering connection, calmness, and care through technology.

🌿 SafeSpace AI  
   *Your Safe Space for Mental Wellness*

SafeSpace AI is an intelligent mental wellness companion that offers users a calm and judgment-free environment to express their thoughts.  
It listens, understands, and responds with empathy — helping you reflect on your emotions while providing encouragement, grounding advice, or gentle guidance when needed.

💡 Features

- 🧠 **Emotion Detection** – Analyzes text input using a fine-tuned emotion recognition model.  
- 💬 **Empathetic Responses** – Replies according to your emotional state:  
  - 🌞 *Positive:* Encouraging and celebratory messages.  
  - 🌧️ *Negative:* Comforting messages with helpful self-care suggestions.  
  - 🌤️ *Neutral:* Calm reflections and light motivational prompts.  
- 🔗 **Trusted Resources** – Provides verified mental health links when support is needed.  
- 🌈 **Minimal, Soothing Interface** – A clean chat-style UI designed to promote calm and focus.  
- 🧩 **Local & Private** – Everything runs locally on your computer for complete privacy.

⚙️ How It Works

1. **Backend (Flask Server)**  
   - Runs the AI model (`joeddav/distilbert-base-uncased-go-emotions-student`) from Hugging Face.  
   - Detects emotional tones from user messages with high accuracy.  

2. **Frontend (HTML + JS Interface)**  
   - `page1.html` – landing page introducing the app.  
   - `page2.html` – chat interface that connects to the Flask API and displays responses.  

3. **Interaction Flow**  
   - Type a message expressing how you feel.  
   - The backend analyzes it and identifies one or more emotions.  
   - SafeSpace AI replies with empathy, offering encouragement or helpful resources.

🧠 Tech Stack

| Layer | Technology |
|-------|-------------|
| **Frontend** | HTML, CSS, JavaScript |
| **Backend** | Python Flask, Flask-CORS |
| **AI Model** | DistilBERT – GoEmotions (Student Model) |
| **Libraries** | `transformers`, `torch` |

🚀 Getting Started

1. **Install dependencies**
   ```bash
   pip install flask flask-cors torch transformers
   ```

2. **Run the Flask server**
   ```bash
   python app.py
   ```

3. **Open the interface**
   - Launch `DelhiTechFest.html` in your browser.
   - Click **Begin** to start chatting on the `page2.html` page.

4. **Start sharing**  
   Type how you feel — SafeSpace AI will listen, understand, and respond with care.

❤️ Purpose & Vision

SafeSpace AI is not a replacement for therapy or professional help —  
it’s a digital space for **emotional reflection and understanding**, built to remind you that your feelings matter.  
It bridges the gap between silence and empathy, showing how AI can be gentle, supportive, and kind.

🕊️ Disclaimer
This project is intended for emotional wellness support and awareness only.  
It does not provide clinical or professional mental-health treatment.  
If you are in crisis or need immediate help, please reach out to your local helpline or mental-health professional.

# 🎵 MoodMuse – Emotion-Based Music Recommendation App

MoodMuse is an AI-powered application that recommends music based on your emotions. Simply type how you're feeling, and MoodMuse detects the emotion behind your words and curates a playlist that matches your mood — all in real-time using the Spotify API.

## 🌟 Features

- 🔍 **Emotion Detection**: Uses NLP to analyze and classify emotions from user text input.
- 🎧 **Spotify Integration**: Recommends real-time tracks through the Spotify API.
- 🎨 **Clean UI**: Simple frontend for entering mood and displaying song suggestions.
- 📈 **Scalable Design**: Future-ready for voice input, mood history, and more.

## 🧠 How It Works

1. User inputs a sentence (e.g., "I'm feeling super anxious today").
2. The app detects the underlying emotion (e.g., *sad*, *calm*, *angry*, etc.).
3. It maps the emotion to a mood tag and uses Spotify’s API to fetch matching tracks.
4. The recommended songs are displayed for listening instantly.

## 🛠️ Tech Stack

| Layer         | Tools/Libraries                             |
|---------------|---------------------------------------------|
| Backend       | Python, Flask                               |
| NLP Model     | HuggingFace Transformers / TextBlob / LSTM  |
| API Integration | Spotify Web API                            |
| Frontend      | HTML, CSS, JavaScript (optional: React)     |
| Deployment    | Render / Heroku / Vercel (planned)          |

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Spotify Developer Account (for API keys)
- `pip install -r requirements.txt`

### Setup

```bash
git clone https://github.com/yourusername/emotion-music-rec-ai.git
cd emotion-music-rec-ai
cp .env.example .env  # Add your Spotify API keys
python app.py

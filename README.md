# VIRTUAL-ASSISTANT-AADI
# 🎙️ AADI — Your Voice-First AI Assistant

<p align="center">
  <b>A futuristic, browser-based voice assistant that listens for a wake word,<br/>answers questions, does advanced math, plays any song, and opens the web — hands-free.</b>
</p>

<p align="center">
  <img alt="status" src="https://img.shields.io/badge/status-active-2FE3FF?style=for-the-badge">
  <img alt="platform" src="https://img.shields.io/badge/platform-web%20browser-0A0E17?style=for-the-badge">
  <img alt="license" src="https://img.shields.io/badge/license-MIT-FFB454?style=for-the-badge">
</p>

---

## 🚀 What is AADI?

**AADI** is a personal AI voice assistant that runs **entirely in your browser** — no server, no backend, no API keys, no cost. Just say **"Aadi"**, and it wakes up, listens to your command, and responds — just like Alexa or Google Assistant.

Built as a solo project, AADI combines the **Web Speech API** (for real-time speech recognition and text-to-speech) with a set of free public APIs to deliver a genuinely useful, hands-free assistant — deployable for free and usable by anyone, anywhere.

## ✨ Features

| Category | What it does |
|---|---|
| 🎧 **Hands-free wake word** | Say **"Aadi"** anytime — it responds **"Yes boss"** and starts listening for your command |
| 🌐 **Open websites** | "Open YouTube", "Open Google", "Open Instagram", "Open WhatsApp", and more |
| 🎵 **Play any song** | "Play Kesariya" — instantly redirects to YouTube. Works for **Hindi, English, Punjabi, Bollywood** — literally any song, any language |
| 🧮 **Advanced calculator** | Square, cube, square root, cube root, factorial, percentage, powers, sin/cos/tan, log, natural log — like a full scientific calculator |
| 📖 **Wikipedia lookup** | "Who is Elon Musk?" / "What is quantum computing?" |
| 🔍 **Google search** | "Search best laptops 2026" |
| 🌦️ **Live weather** | "Weather in Prayagraj" — real-time, no API key needed |
| 😂 **Jokes** | "Tell me a joke" |
| 🕐 **Time & date** | "What's the time?" / "What's today's date?" |
| ⚠️ **Smart error handling** | Tells you clearly if there's a network/connection issue, or if it simply didn't understand you — never just hangs silently |

## 🖥️ Tech Stack

- **HTML5 / CSS3 / Vanilla JavaScript** — no frameworks, no build step
- **Web Speech API** — `SpeechRecognition` (STT) + `SpeechSynthesis` (TTS), both native to the browser
- **Free public APIs** (no keys required):
  - [Open-Meteo](https://open-meteo.com/) — weather
  - [Wikipedia REST API](https://en.wikipedia.org/api/rest_v1/) — knowledge lookups
  - [Official Joke API](https://official-joke-api.appspot.com/) — jokes

Because everything runs client-side, **each user's microphone audio stays in their own browser** — nothing is ever uploaded to a server.

## 🌍 Live Demo

> Deployed for free on GitHub Pages:
> **`https://<your-github-username>.github.io/<repo-name>/`**
>
> *(Replace with your actual link once deployed — see below)*

## 🛠️ Getting Started

### Option 1 — Run locally (fastest way to test)

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
python run app.py
```

This starts a local server and opens AADI in your default browser at `http://localhost:8000`. Other devices on the same WiFi can access it too, via the network URL printed in the terminal.

### Option 2 — Deploy for free on GitHub Pages (public, works for anyone)

1. Push this repo to GitHub (make sure it's **Public**)
2. Go to **Settings → Pages**
3. Under **Source**, select **Deploy from a branch** → branch `main`, folder `/ (root)`
4. Save, and wait 1–2 minutes
5. Your live URL will appear at the top of the Pages settings — share it with anyone!

> ⚠️ Microphone access requires **HTTPS** (or `localhost`). GitHub Pages serves over HTTPS automatically, so mic permissions work correctly for every visitor.

## 🎤 How to Use

1. Open the app in **Google Chrome or Microsoft Edge** (best Web Speech API support)
2. Toggle **"🎧 Hands-free — say 'Aadi'"** to enable wake-word mode, or just tap the orb to speak once
3. Allow microphone access when prompted
4. Say **"Aadi"** → wait for **"Yes boss"** → speak your command

### Example commands

```
"Aadi"  →  "Yes boss."
"Open YouTube"
"Play Tum Hi Ho"
"What's the time?"
"Square root of 144"
"Factorial of 6"
"20 percent of 450"
"2 power 10"
"Who is APJ Abdul Kalam?"
"Weather in Lucknow"
"Tell me a joke"
```

## 🌐 Browser Compatibility

| Browser | Support |
|---|---|
| Chrome (Desktop/Android) | ✅ Full support |
| Microsoft Edge | ✅ Full support |
| Safari | ⚠️ Limited / inconsistent |
| Firefox | ❌ Web Speech API not supported |

## 📌 Roadmap / Future Scope

- [ ] Add multi-turn conversational context (remember previous command)
- [ ] Add regional language support (Hindi/Punjabi command parsing, not just song search)
- [ ] Local notes with persistent storage
- [ ] Smart home / IoT integration
- [ ] Custom wake-word sensitivity tuning

## 🤝 Contributing

This is a personal learning project, but suggestions and pull requests are always welcome — feel free to open an issue or fork it.

## 📄 License

This project is open-sourced under the **MIT License** — free to use, modify, and share.

## 👤 Author

**Aditya Srivastava**
B.Tech (AI/ML) student · Building projects in AI, ML, and full-stack development
🔗 GitHub: [@Aaditya-Srivastava09](https://github.com/Aaditya-Srivastava09)

---

<p align="center"><i>Built with curiosity, late-night debugging, and a lot of "why is this hanging" moments. 🚀</i></p>

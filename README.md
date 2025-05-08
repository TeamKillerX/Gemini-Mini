# Gemini Mini Bot

**Gemini Mini** is a lightweight, modular Pyrogram-based Telegram bot powered by Google Gemini AI.  
It supports multi-turn conversations, image generation, translations, and more — all designed to be fast and efficient.

---

## ✨ Features

- [ ] Multi-turn chat streaming (`chatstream`)
- [ ] Google Gemini AI integration
- [ ] Image editing & generation (`--edit-images`, `--stream-images`)
- [ ] Optional MongoDB chat history
- [x] Regex support for better input parsing
- [ ] Callback button control system
- [ ] Translate with AI (Paid)
- [ ] Frozen account support & data privacy

---

## 🚀 VPS Setup

```bash
# Clone the repo
git clone https://github.com/TeamKillerX/Gemini-Mini.git
cd Gemini-Mini

pip install -r requirements.txt

# add .env
API_ID=your_api_id
API_HASH=your_api_hash
BOT_TOKEN=your_bot_token
MONGO_URL=your_mongo_uri
````

Start the bot:

```bash
python3 -m GeminiMini
```

---

## 🧠 Tutorial Commands

- Available via [`@GeminiAIDev_Bot`](https://t.me/GeminiAIDev_Bot)

```text
--edit-images <caption>         # Edit uploaded photo
--stream-images <caption>       # Live image gen stream
(enabled|disabled):chatstream   # Toggle live conversation mode
--deletemydata --reason <text>  # Request data deletion
```

---

## 🤝 Credits

* **TeamKillerX** — main developer and project lead
* **Google AI Developers** — for Gemini API and AI tools
* **[Pyrogram, kurigram]** — Telegram MTProto API framework
* **MongoDB** — async NoSQL database used for optional features

---

## 📌 Notes

* **Gemini Mini is Open Source**, but different from `@GeminiAIDev_Bot`, which is private and feature-rich.
* Some APIs require payment or quota (e.g. Gemini Image, Translate).
* Optional features can be removed or customized to reduce load.

---

## License

MIT License

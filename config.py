import os
from dotenv import load_dotenv

load_dotenv()
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
MONGO_URL = os.getenv("MONGO_URL")

if not all([API_ID, API_HASH, BOT_TOKEN, GOOGLE_API_KEY, MONGO_URL]):
    raise ValueError("404 Error variables all.")
    exit(1)

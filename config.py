import os
from os import getenv

API_ID = int(os.environ.get("29467268", ""))  # Replace "123456" with your actual api_id or use .env
API_HASH = os.environ.get("314e5ae9ce4f78ef127a5a04a5c97649", "")
BOT_TOKEN = os.environ.get("", "")

OWNER_ID = int(os.environ.get("6579568737", ""))  # Your Telegram user ID
SUDO_USERS = list(map(int, os.environ.get("6579568737", "").split()))  # Space-separated user IDs

MONGO_URL = os.environ.get("mongodb+srv://yicaje5667:FA6CC7yxWCgyBt9q@cluster0.xv7sf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", "")##your mongo url eg: withmongodb+srv://xxxxxxx:xxxxxxx@clusterX.xxxx.mongodb.net/?retryWrites=true&w=majority
CHANNEL_ID = int(os.environ.get("-2836794655", "-"))  # Telegram channel ID (with -100 prefix)

PREMIUM_LOGS = os.environ.get("6579568737", "")  # Optional here you'll get all logs

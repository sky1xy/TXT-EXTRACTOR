import os
from os import getenv

API_ID = int(os.environ.get("24684505", ""))  # Replace "123456" with your actual api_id or use .env
API_HASH = os.environ.get("c4aade88dbad511f7cc60ee4b69970d1", "")
BOT_TOKEN = os.environ.get("7646492610:AAGbs5Q7z6dpoeckZCoOrIQl7Goa_X94mSI", "")

OWNER_ID = int(os.environ.get("5424499713", ""))  # Your Telegram user ID
SUDO_USERS = list(map(int, os.environ.get("5424499713", "").split()))  # Space-separated user IDs

MONGO_URL = os.environ.get("mongodb+srv://yicaje5667:FA6CC7yxWCgyBt9q@cluster0.xv7sf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", "")##your mongo url eg: withmongodb+srv://xxxxxxx:xxxxxxx@clusterX.xxxx.mongodb.net/?retryWrites=true&w=majority
CHANNEL_ID = int(os.environ.get("-1002656878420", "-"))  # Telegram channel ID (with -100 prefix)

PREMIUM_LOGS = os.environ.get("5424499713", "")  # Optional here you'll get all logs

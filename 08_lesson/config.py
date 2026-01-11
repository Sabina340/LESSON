import os

BASE_URL = "https://ru.yougile.com/api-v2"

API_TOKEN = os.getenv("YOUGILE_TOKEN")

HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

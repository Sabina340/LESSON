import os

BASE_URL = "https://ru.yougile.com/api-v2"

API_TOKEN = os.getenv("YOUGILE_TOKEN")

HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

# ===== Test data =====
VALID_PROJECT_TITLE = "New Project"
UPDATED_PROJECT_TITLE = "Updated Project"
EMPTY_PROJECT_TITLE = ""
INVALID_PROJECT_ID = 99999999

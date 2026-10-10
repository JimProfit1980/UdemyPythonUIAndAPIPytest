import json
from pathlib import Path

# credentials.json is git-ignored. Locally you keep your own copy (see credentials.example.json);
# in GitHub Actions it is written from the CREDENTIALS_JSON repository secret.
CREDENTIALS_FILE = Path(__file__).parent.parent / "data" / "credentials.json"


def load_credentials():
    with open(CREDENTIALS_FILE, "r") as f:
        return json.load(f)["user_credentials"]


def primary_user():
    return load_credentials()[0]

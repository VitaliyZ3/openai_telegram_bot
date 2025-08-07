from pathlib import Path
import os

from dotenv import load_dotenv

# env
BASE_DIR = Path(__file__).parent.parent
PATH_TO_ENV = BASE_DIR / ".env"
load_dotenv(PATH_TO_ENV)

PATH_TO_RESOURCES = BASE_DIR / "src" / "resources"


# keys
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
TG_BOT_API_KEY = os.environ["TG_BOT_API_KEY"]
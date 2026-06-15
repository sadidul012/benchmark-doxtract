import os
from dotenv import load_dotenv

# Load key-value pairs from the .env file into os.environ
load_dotenv()

# Access them just like standard system variables
DOXTRACT_API_URL = os.getenv("DOXTRACT_API_URL")
DOXTRACT_API_KEY = os.getenv("DOXTRACT_API_KEY")
DOXTRACT_API_SECRET = os.getenv("DOXTRACT_API_SECRET")

from dotenv import load_dotenv
import os

load_dotenv()

# Database
DATABASE_URL = os.getenv("DATABASE_URL")

# JWT Authentication
SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "this_is_a_super_secret_key_change_it"
)

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 60
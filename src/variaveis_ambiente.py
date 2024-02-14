import os

from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()

load_dotenv(dotenv_path)

ERP_KEY = os.getenv("ERP_KEY")

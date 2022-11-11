# --------------- EXTERNAL PACKAGES ---------------
from dotenv import load_dotenv, find_dotenv

# --------------- BUILT-IN PACKAGES ---------------
import os

load_dotenv()

XLSX_PATH = os.getenv('XLSX_PATH')
SHEET_NAME = os.getenv('SHEET_NAME')
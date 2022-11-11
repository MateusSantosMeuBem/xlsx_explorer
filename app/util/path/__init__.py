# --------------- EXTERNAL PACKAGES ---------------
from dotenv import load_dotenv, find_dotenv

# --------------- BUILT-IN PACKAGES ---------------
import os

load_dotenv()

XLSX_PATH = os.getenv('XLSX_PATH')
SHEET_NAME = os.getenv('XLSX_SHEET_NAME')
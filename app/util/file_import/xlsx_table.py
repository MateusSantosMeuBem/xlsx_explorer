# ---------- External packages ----------
from dotenv import load_dotenv
import pandas as pd

# TYPES
from pandas.core.frame import DataFrame

# --------------- BUILT-IN PACKAGES ---------------


# ---------- Personal packages ----------
from util.path import (
    XLSX_PATH,
    SHEET_NAME
)


def table_data() -> DataFrame:
    return pd.read_excel(
        io=XLSX_PATH,
        sheet_name=SHEET_NAME,
    )
# ---------- BUILT-IN PACKAGES ----------
import json


# ---------- EXTERNAL PACKAGES ----------
from pandas.core.frame import (
    DataFrame
)

# ---------- PERSONAL PACKAGES ----------
from util.file_import.xlsx_table import (
    table_data
)

def get_row(
    row_index: int = 0
) -> str:
    try:
        return table_data()\
        .loc[row_index]\
        .to_json(
            force_ascii=False,
            date_format='iso'
        )

    except Exception:
        return '{}'
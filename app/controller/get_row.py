# ---------- PERSONAL PACKAGES ----------
from controller import (
    app
)
from util.get_row import (
    get_row
)

@app.route('/row/<row_index>', methods = ['GET'])
def getRow(
    row_index: int
):  
    return str(get_row(int(row_index)))
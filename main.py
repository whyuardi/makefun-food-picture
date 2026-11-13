import base64
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.b64")
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(OUT, "entry.png")

os.makedirs(OUT, exist_ok=True)
with open(SRC, "r", encoding="ascii") as f:
    data = base64.b64decode("".join(f.read().split()))
if not data.startswith(b"\xff\xd8\xff"):
    raise ValueError("decoded entry is not a JPEG image")
with open(DST, "wb") as f:
    f.write(data)

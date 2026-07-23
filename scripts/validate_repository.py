#!/usr/bin/env python3
import csv
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
layout = json.loads((root / "layouts/tikl-26/v1/layout.json").read_text())
physical = "QWERTYUIOPASDFGHJKLZXCVBNM"
outputs = "JBLDFQUOYKRNTSCIEAHWPMGVZX"
assert "".join(layout["mapping"][key] for key in physical) == outputs
assert set(layout["mapping"].values()) == set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
with (root / "layouts/tikl-26/v1/layout.csv").open() as handle:
    rows = list(csv.DictReader(handle))
assert len(rows) == 26
assert {row["physical_qwerty_key"]: row["tikl_output"] for row in rows} == layout["mapping"]
for path in root.rglob("*.json"):
    json.loads(path.read_text())
print("PASS: mapping is bijective, CSV agrees, and JSON parses")

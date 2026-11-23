import json
import base64
import os

print("Building PULSE Complete Executive Showcase Suite...")

# 1. Load Initial Data
with open("/Users/raksh/.gemini/antigravity/scratch/pulse-showcase/initial_data.json", "r") as f:
    master_data = json.load(f)

# 2. Load DSM Logo as Base64
with open("/Users/raksh/.gemini/antigravity/scratch/pulse-showcase/dsm-logo.png", "rb") as f:
    dsm_logo_b64 = base64.b64encode(f.read()).decode("utf-8")

data_json_str = json.dumps(master_data)

print(f"Data & Logo ready: {len(master_data['employees'])} employees, {len(dsm_logo_b64)} b64 chars.")

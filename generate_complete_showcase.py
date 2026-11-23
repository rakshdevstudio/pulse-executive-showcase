import json
import base64
import os

print("Assembling complete PULSE Executive Showcase...")

with open("/Users/raksh/.gemini/antigravity/scratch/pulse-showcase/initial_data.json", "r") as f:
    master_data = json.load(f)

with open("/Users/raksh/.gemini/antigravity/scratch/pulse-showcase/dsm-logo.png", "rb") as f:
    dsm_logo_b64 = base64.b64encode(f.read()).decode("utf-8")

data_json_str = json.dumps(master_data)

# Write builder parts
print(f"Loaded master data: {len(master_data['employees'])} employees, {len(master_data['biometricPunches'])} punches.")

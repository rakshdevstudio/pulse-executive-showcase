import json
import base64
import os

from parts_css import CSS_CONTENT
from parts_story import get_story_html
from parts_product_views import get_product_views_html
from parts_js import JS_CONTENT

print("Assembling PULSE Executive Showcase...")

# 1. Load Data
with open("/Users/raksh/.gemini/antigravity/scratch/pulse-showcase/initial_data.json", "r") as f:
    master_data = json.load(f)

# 2. Load Logo
with open("/Users/raksh/.gemini/antigravity/scratch/pulse-showcase/dsm-logo.png", "rb") as f:
    dsm_logo_b64 = base64.b64encode(f.read()).decode("utf-8")

data_json_str = json.dumps(master_data)

story_html = get_story_html(dsm_logo_b64)
product_html = get_product_views_html(dsm_logo_b64)
js_code = JS_CONTENT.replace("__INITIAL_DATA_PLACEHOLDER__", data_json_str)

full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>PULSE — Workforce Operations & Performance Intelligence</title>
  <style>
{CSS_CONTENT}
  </style>
</head>
<body>

{story_html}

{product_html}

  <script>
{js_code}
  </script>
</body>
</html>
"""

# Write to deliverables
files_to_write = [
    "/Users/raksh/.gemini/antigravity/scratch/pulse-showcase/pulse-executive-showcase.html",
    "/Users/raksh/.gemini/antigravity/scratch/pulse-showcase/index.html"
]

for file_path in files_to_write:
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"Generated: {file_path} ({os.path.getsize(file_path):,} bytes)")

print("ASSEMBLY COMPLETE!")

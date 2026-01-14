import requests
import json

base = "https://leprechaun-generator.vercel.app"

print("Testing API endpoints:")

# Test health endpoint
try:
    resp = requests.get(f"{base}/api/health", timeout=5)
    print(f"Health API: {resp.status_code} - {resp.text}")
except Exception as e:
    print(f"Health API Error: {e}")

# Test name generation
try:
    resp = requests.get(f"{base}/api/generate", timeout=5)
    if resp.status_code == 200:
        data = resp.json()
        print(f"Generate API: {data.get('name', 'No name')}")
    else:
        print(f"Generate API: {resp.status_code} - {resp.text}")
except Exception as e:
    print(f"Generate API Error: {e}")

# Test PDF generation
try:
    resp = requests.get(f"{base}/api/pdf?name=Test%20Leprechaun", timeout=10)
    print(f"PDF API: {resp.status_code} - Content-Type: {resp.headers.get('Content-Type', 'None')}")
    if resp.status_code == 200:
        print(f"PDF size: {len(resp.content)} bytes")
except Exception as e:
    print(f"PDF API Error: {e}")

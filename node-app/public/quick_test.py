import requests
import json

try:
    # Test generate endpoint
    resp = requests.get("https://leprechaun-generator.vercel.app/api/generate", timeout=10)
    if resp.status_code == 200:
        data = resp.json()
        print(f"✅ Generate API: {data.get('name', 'ERROR')}")
    else:
        print(f"❌ Generate API: Status {resp.status_code}")
    
    # Test health endpoint
    resp = requests.get("https://leprechaun-generator.vercel.app/health", timeout=10)
    if resp.status_code == 200:
        data = resp.json()
        print(f"✅ Health API: {data.get('status', 'ERROR')}")
    else:
        print(f"❌ Health API: Status {resp.status_code}")
    
    # Test website
    resp = requests.get("https://leprechaun-generator.vercel.app", timeout=10)
    print(f"✅ Website: Status {resp.status_code}")
    
    # Check for key content
    if "Leprechaun Name Generator" in resp.text:
        print("✅ Title found in page")
    if "generateName" in resp.text:
        print("✅ JavaScript functions found")
    if "<section" in resp.text:
        section_count = resp.text.count("<section")
        print(f"✅ {section_count} sections found")
        
except Exception as e:
    print(f"❌ Test failed: {e}")

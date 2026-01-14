import requests
import json

try:
    print("Testing live website at https://leprechaun-generator.vercel.app")
    resp = requests.get("https://leprechaun-generator.vercel.app", timeout=10)
    print(f"Status Code: {resp.status_code}")
    print(f"Content Length: {len(resp.text)} bytes")
    
    # Check for key elements
    if "Leprechaun Name Generator" in resp.text:
        print("✅ Title found")
    else:
        print("❌ Title NOT found")
        
    if "generateName" in resp.text:
        print("✅ JavaScript functions found")
    else:
        print("❌ JavaScript functions NOT found")
        
    if "<section" in resp.text:
        sections = resp.text.count("<section")
        print(f"✅ {sections} sections found")
    else:
        print("❌ No sections found")
        
    # Save live version for comparison
    with open("/tmp/live_version.html", "w") as f:
        f.write(resp.text)
        
except Exception as e:
    print(f"Error: {e}")

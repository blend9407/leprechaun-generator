import requests
import time

url = "https://leprechaun-generator.vercel.app"
print(f"Testing {url}")

try:
    resp = requests.get(url, timeout=10)
    print(f"Status Code: {resp.status_code}")
    print(f"Content Length: {len(resp.text)} bytes")
    
    # Check for new UI elements
    checks = {
        "Hero Section": "<section.*hero" in resp.text,
        "Generator Section": "<section.*generator" in resp.text,
        "Features Section": "<section.*features" in resp.text,
        "Templates Section": "<section.*templates" in resp.text,
        "Multiple Buttons": resp.text.count("<button") > 2,
        "JavaScript Functions": "generateName" in resp.text,
        "Tailwind CSS": "tailwindcss" in resp.text,
    }
    
    print("\nUI Elements Check:")
    for element, found in checks.items():
        status = "✅" if found else "❌"
        print(f"{status} {element}")
    
    # Count sections
    sections = resp.text.count("<section")
    print(f"\nTotal sections found: {sections}")
    
    if sections >= 4:
        print("✅ Elegant UI successfully deployed!")
    else:
        print("❌ Old UI still showing")
        
except Exception as e:
    print(f"Error: {e}")

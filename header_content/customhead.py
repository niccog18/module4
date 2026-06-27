# Working with Headers in Python
# Step 1: Send custom headers
import requests

# Send a request with custom headers
response = requests.get(
    "https://jsonplaceholder.typicode.com/posts/1",
    headers={
        "Accept": "application/json",       # We want JSON back
        "X-Custom-Header": "module-4-demo", # A custom header
    }
)

# See all headers we sent
print("=== Headers We Sent ===")
for key, value in response.request.headers.items():
    print(f"  {key}: {value}")

# You should see:
# === Headers We Sent ===
  # User-Agent: python-requests/2.31.0
  # Accept-Encoding: gzip, deflate
  # Accept: application/json
  # Connection: keep-alive
  # X-Custom-Header: module-4-demo

# The requests library added several default headers alongside yours. It automatically sets User-Agent, Accept-Encoding (for compressed responses), and Connection.

# Step 2: Read response headers
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts")

print("=== Response Headers ===")
for key, value in response.headers.items():
    print(f"  {key}: {value}")

# Access specific headers
print(f"\nContent-Type: {response.headers['Content-Type']}")
print(f"Content-Length: {response.headers.get('Content-Length', 'Not specified')}")

# Step 3: Content-Type determines how you parse the response
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

content_type = response.headers.get("Content-Type", "")

if "application/json" in content_type:
    # Safe to parse as JSON
    data = response.json()
    print(f"Got JSON: {data['title'][:40]}...")
elif "text/html" in content_type:
    # It's HTML — treat as text
    print(f"Got HTML: {response.text[:100]}...")
else:
    # Unknown format
    print(f"Unknown Content-Type: {content_type}")
    print(f"Raw content: {response.text[:100]}...")

# Step 4: Headers for POST requests — Content-Type matters
import requests
import json

# Method 1: Using json= (recommended — sets Content-Type automatically)
response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json={"title": "Auto Content-Type", "body": "Easy way", "userId": 1}
)
print(f"Method 1 Content-Type: {response.request.headers['Content-Type']}")

# Method 2: Using data= with manual headers (more control)
response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    data=json.dumps({"title": "Manual Content-Type", "body": "Hard way", "userId": 1}),
    headers={"Content-Type": "application/json"}
)
print(f"Method 2 Content-Type: {response.request.headers['Content-Type']}")

# You should see:
# Method 1 Content-Type: application/json
# Method 2 Content-Type: application/json

# Both methods work, but json= is cleaner. It serializes the dictionary to JSON and sets the Content-Type header for you in one step.
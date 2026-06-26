# Step 1: Inspect the full request
import requests

# Make a POST request so we have both request and response data
response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json={"title": "Lifecycle Demo", "body": "Testing the full cycle", "userId": 1},
    headers={"X-Custom-Header": "learning-apis"}
)

# Inspect what WE sent (the request)
print("=== REQUEST ===")
print(f"Method: {response.request.method}")
print(f"URL:    {response.request.url}")
print(f"\nRequest Headers:")
for key, value in response.request.headers.items():
    print(f"  {key}: {value}")
print(f"\nRequest Body: {response.request.body}")

# You should see something like:
# === REQUEST ===
# Method: POST
# URL:    https://jsonplaceholder.typicode.com/posts

# Request Headers:
  # User-Agent: python-requests/2.31.0
  # Accept-Encoding: gzip, deflate
  # Accept: */*
  # Connection: keep-alive
  # X-Custom-Header: learning-apis
  # Content-Length: 68
  # Content-Type: application/json

# Request Body: b'{"title": "Lifecycle Demo", "body": "Testing the full cycle", "userId": 1}'

# Notice: the requests library automatically added headers for you, Content-Type, User-Agent, Accept-Encoding. You only specified X-Custom-Header.

# Step 2: Inspect the full response
# Inspect what the SERVER sent back (the response)
print("\n=== RESPONSE ===")
print(f"Status: {response.status_code} {response.reason}")
print(f"\nResponse Headers:")
for key, value in response.headers.items():
    print(f"  {key}: {value}")
print(f"\nResponse Body:")
import json
print(json.dumps(response.json(), indent=2))

# Step 3: Measure timing
import requests

# The response object tracks how long the request took
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(f"Total time: {response.elapsed.total_seconds():.3f} seconds")
print(f"That's {response.elapsed.total_seconds() * 1000:.0f} milliseconds")

# The entire lifecycle, DNS, connection, request, processing, response, typically takes 50–500ms for a well-designed API. When you're building AI applications that chain multiple API calls, these milliseconds add up. Understanding timing helps you design efficient systems.
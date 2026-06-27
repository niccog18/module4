# Authentication in Practice

# Let's see each authentication pattern in real Python code.

# Step 1: API Key authentication
import requests
import os

# In real code, NEVER hardcode keys — use environment variables
# For this demo, we'll use a placeholder
API_KEY = os.environ.get("DEMO_API_KEY", "demo-key-for-learning")

# Pattern 1: API key in query parameter
response = requests.get(
    "https://httpbin.org/get",
    params={"api_key": API_KEY}
)
data = response.json()
print("=== API Key in Query Parameter ===")
print(f"URL sent: {data['url']}")
# Note: the key is visible in the URL! Less secure.
print()

# Pattern 2: API key in header (preferred)
response = requests.get(
    "https://httpbin.org/get",
    headers={"X-API-Key": API_KEY}
)
data = response.json()
print("=== API Key in Header ===")
print(f"X-API-Key header: {data['headers'].get('X-Api-Key', 'Not found')}")
# The key is in the headers, not the URL. More secure.

# Step 2: Bearer token authentication (JWT pattern)
import requests

# Simulate the JWT flow using httpbin.org

# Step 1: "Login" — in a real app, you'd POST credentials and get a token back
# We'll simulate having received a token
fake_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIn0.dozjgNryP4J3jVmNHl0w5N_XgL0n3I9PlFUP0THsR8U"

# Step 2: Use the token in subsequent requests
response = requests.get(
    "https://httpbin.org/get",
    headers={"Authorization": f"Bearer {fake_token}"}
)
data = response.json()

print("=== Bearer Token Authentication ===")
auth_header = data['headers'].get('Authorization', 'Not found')
print(f"Authorization header: {auth_header[:50]}...")
print()

# This is exactly how you'll authenticate with your FastAPI backends in Module 5

# Step 3: Handling authentication errors
import requests

def make_authenticated_request(url, token=None):
    """Make a request and handle auth-related errors."""
    headers = {}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        print(f"  ✓ Success: got {len(response.text)} bytes")
    elif response.status_code == 401:
        print(f"  ✗ 401 Unauthorized: token missing or invalid")
        print(f"    → Check: Is the token included? Is it expired?")
    elif response.status_code == 403:
        print(f"  ✗ 403 Forbidden: authenticated but not authorized")
        print(f"    → Check: Does this user have the right permissions?")
    else:
        print(f"  ? Status {response.status_code}: {response.reason}")

# Test scenarios
print("Request without token:")
make_authenticated_request("https://httpbin.org/status/401")

print("\nRequest with valid token:")
make_authenticated_request("https://httpbin.org/get", token="my-token")

print("\nRequest to forbidden resource:")
make_authenticated_request("https://httpbin.org/status/403", token="my-token")

# Step 4: Environment variables for API keys
import os

# The RIGHT way to handle API keys in your code
# First, create a .env file (NEVER commit this to Git):
#   OPENAI_API_KEY=sk-abc123...
#   DATABASE_URL=sqlite:///app.db

# Then load it (in a real project, use python-dotenv):
api_key = os.environ.get("OPENAI_API_KEY")

if api_key:
    print(f"API key loaded: {api_key[:8]}...")  # Only show first 8 chars!
else:
    print("No API key found in environment")
    print("Set it with: export OPENAI_API_KEY=your-key-here")

# NEVER do this:
# api_key = "sk-abc123def456"  ← Hardcoded! Will end up in Git!

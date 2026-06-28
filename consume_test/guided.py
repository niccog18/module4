# Building an API Client in Python

# Since Postman and curl can't be demonstrated in a Python file, let's build a structured Python API client that mirrors the organizational approach of a Postman collection.

# Step 1: A reusable API client class
import requests
import json

class APIClient:
    """A simple API client — similar to how you'd organize a Postman collection."""
    
    def __init__(self, base_url, headers=None):
        self.base_url = base_url.rstrip("/")
        self.default_headers = headers or {}
    
    def _request(self, method, path, **kwargs):
        """Make a request and return a formatted result."""
        url = f"{self.base_url}{path}"
        
        # Merge default headers with any request-specific headers
        headers = {**self.default_headers, **kwargs.pop("headers", {})}
        
        response = requests.request(method, url, headers=headers, **kwargs)
        
        return {
            "status": response.status_code,
            "reason": response.reason,
            "time_ms": response.elapsed.total_seconds() * 1000,
            "data": response.json() if response.text else None,
            "headers": dict(response.headers),
        }
    
    def get(self, path, **kwargs):
        return self._request("GET", path, **kwargs)
    
    def post(self, path, **kwargs):
        return self._request("POST", path, **kwargs)
    
    def put(self, path, **kwargs):
        return self._request("PUT", path, **kwargs)
    
    def patch(self, path, **kwargs):
        return self._request("PATCH", path, **kwargs)
    
    def delete(self, path, **kwargs):
        return self._request("DELETE", path, **kwargs)

# Create a client for JSONPlaceholder
api = APIClient("https://jsonplaceholder.typicode.com")

# Now use it — clean and organized
print("=== GET /users/1 ===")
result = api.get("/users/1")
print(f"Status: {result['status']} ({result['time_ms']:.0f}ms)")
print(f"Name: {result['data']['name']}")

# Step 2: Use the client for a full CRUD flow
# CREATE
print("\n=== POST /posts ===")
result = api.post("/posts", json={
    "title": "My Test Post",
    "body": "Testing with our API client",
    "userId": 1
})
print(f"Status: {result['status']} — Created post #{result['data']['id']}")

# READ
print("\n=== GET /posts/1 ===")
result = api.get("/posts/1")
print(f"Status: {result['status']} — Title: {result['data']['title'][:40]}...")

# UPDATE
print("\n=== PATCH /posts/1 ===")
result = api.patch("/posts/1", json={"title": "Updated Title"})
print(f"Status: {result['status']} — New title: {result['data']['title']}")

# DELETE
print("\n=== DELETE /posts/1 ===")
result = api.delete("/posts/1")
print(f"Status: {result['status']}")

# Step 3: Consuming a second API (showing portability)
# Create a client for httpbin.org — same pattern, different API
httpbin = APIClient("https://httpbin.org")

print("\n=== httpbin.org — Echo test ===")
result = httpbin.post("/post", json={"message": "Hello from our client!"})
print(f"Status: {result['status']}")
print(f"Server saw our data: {result['data']['json']}")

# The API client class mirrors what Postman does: it organizes your base URL and default headers, then provides clean methods for each HTTP verb. The difference is that this client lives in your codebase and can be used in your application.

# Step 4: Equivalent curl commands (for reference)

# Here are the same calls written as curl commands. You can run these in your terminal:
# Print the equivalent curl commands for reference
# print("\n=== Equivalent curl Commands ===")
# print()
# print('# GET a user')
# print('curl -s https://jsonplaceholder.typicode.com/users/1 | python -m json.tool')
# print()
# print('# POST a new post')
# print('curl -X POST https://jsonplaceholder.typicode.com/posts \\\\')
# print('  -H "Content-Type: application/json" \\\\')
# print('  -d \\'{\\'"title": "My Test Post", "body": "Testing", "userId": 1}\\'\\'')
# print()
# print('# PATCH (update) a post')
# print('curl -X PATCH https://jsonplaceholder.typicode.com/posts/1 \\\\')
# print('  -H "Content-Type: application/json" \\\\')
# print('  -d \\'{\\'"title": "Updated Title"}\\'\\'')
# print()
# print('# DELETE a post')
# print('curl -X DELETE https://jsonplaceholder.typicode.com/posts/1')
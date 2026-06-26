# Triggering and Interpreting Status Codes

# Let's intentionally trigger different status codes to see how they work in practice.
# Step 1: Success codes
import requests

# 200 OK — successful GET
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(f"GET existing post:  {response.status_code} ({response.reason})")

# 201 Created — successful POST
new_post = {"title": "Test", "body": "Test body", "userId": 1}
response = requests.post("https://jsonplaceholder.typicode.com/posts", json=new_post)
print(f"POST new post:      {response.status_code} ({response.reason})")

# You should see:
# GET existing post:  200 (OK)
# POST new post:      201 (Created)

# Step 2: Client errors
import requests

# 404 Not Found — resource doesn't exist
response = requests.get("https://jsonplaceholder.typicode.com/posts/99999")
print(f"GET nonexistent:    {response.status_code} ({response.reason})")

# 404 — wrong endpoint entirely
response = requests.get("https://jsonplaceholder.typicode.com/dinosaurs")
print(f"GET bad endpoint:   {response.status_code} ({response.reason})")

# You should see:
# GET nonexistent:    404 (Not Found)
# GET bad endpoint:   404 (Not Found)

#Step 3: Build a status code interpreter
import requests

def describe_status(code):
    """Returns a human-readable description of a status code."""
    descriptions = {
        200: "OK — Request succeeded",
        201: "Created — New resource created successfully",
        204: "No Content — Success, but nothing to return",
        301: "Moved Permanently — Resource has a new URL",
        400: "Bad Request — Your request has an error",
        401: "Unauthorized — Authentication required",
        403: "Forbidden — You don't have permission",
        404: "Not Found — Resource doesn't exist",
        405: "Method Not Allowed — Wrong HTTP method for this resource",
        422: "Unprocessable Entity — Data validation failed",
        429: "Too Many Requests — Rate limit exceeded",
        500: "Internal Server Error — Server broke",
        502: "Bad Gateway — Upstream server error",
        503: "Service Unavailable — Server is down",
    }
    
    # Fall back to category description
    category = code // 100  # Integer division gives first digit
    category_desc = {
        1: "Informational",
        2: "Success",
        3: "Redirection",
        4: "Client Error",
        5: "Server Error"
    }
    
    return descriptions.get(code, f"{category_desc.get(category, 'Unknown')} ({code})")

# Test it
test_codes = [200, 201, 301, 400, 401, 403, 404, 422, 500, 503]
for code in test_codes:
    print(f"  {code}: {describe_status(code)}")

# You should see:
# 200: OK — Request succeeded
# 201: Created — New resource created successfully
# 301: Moved Permanently — Resource has a new URL
# 400: Bad Request — Your request has an error
# 401: Unauthorized — Authentication required
# 403: Forbidden — You don't have permission
# 404: Not Found — Resource doesn't exist
# 422: Unprocessable Entity — Data validation failed
# 500: Internal Server Error — Server broke
# 503: Service Unavailable — Server is down

# Step 4: Check status codes programmatically
import requests

def safe_api_call(url):
    """Make an API call and handle the response based on status code."""
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        print(f"  ⚠ Resource not found: {url}")
        return None
    elif response.status_code >= 500:
        print(f"  ❌ Server error ({response.status_code}): try again later")
        return None
    else:
        print(f"  ❌ Error {response.status_code}: {response.reason}")
        return None

# Test with a valid URL
print("Fetching post 1:")
post = safe_api_call("https://jsonplaceholder.typicode.com/posts/1")
if post:
    print(f"  ✓ Got: {post['title'][:40]}...")

# Test with an invalid URL
print("\nFetching post 99999:")
post = safe_api_call("https://jsonplaceholder.typicode.com/posts/99999")

# This pattern, checking the status code before processing the response, is essential for writing reliable code that consumes APIs.
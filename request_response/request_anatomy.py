import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def print_request_anatomy(response):
    """Print the full anatomy of a request and response."""

    request = response.request

    print("=" * 40)

    # Request Information
    print("REQUEST")
    print("-" * 40)
    print(f"Method: {request.method}")
    print(f"URL: {request.url}")

    print("\nRequest Headers:")
    for key, value in request.headers.items():
        print(f"{key}: {value}")

    print("\nRequest Body:")
    if request.body:
        print(request.body)
    else:
        print("None")
    
    # Response Information
    print("\nRESPONSE")
    print("-" * 40)
    print(f"Status Code: {response.status_code}")
    print(f"Reason: {response.reason}")

    print("\nKey Response Headers:")
    print(
        f"Content-Type: "
        f"{response.headers.get('Content-Type', 'Not Available')}"
    )
    print(
        f"Content-Length: "
        f"{response.headers.get('Content-Length', 'Not Available')}"
    )

    print("\nResponse Body:")
    print(response.text)

    elapsed_time = response.elapsed.total_seconds() * 1000
    print(f"\nElapsed Time: {elapsed_time:.2f} ms")

    print("=" * 40)
    print()

# A GET request for a specific user from JSONPlaceholder
print("GET REQUEST - Retrieve User\n")

get_response = requests.get(
    f"{BASE_URL}/users/1"
)

print_request_anatomy(get_response)

# A POST request creating a new post
print("POST REQUEST - Create New Post\n")

new_post = {
    "title": "My First API Post",
    "body": "Learning how HTTP requests work.",
    "userId": 1
}

post_response = requests.post(
    f"{BASE_URL}/posts",
    json=new_post
)

print_request_anatomy(post_response)

# A PATCH request updating a post's title
print("PATCH REQUEST - Update Post Title\n")

updated_title = {
    "title": "Updated API Post Title"
}

patch_response = requests.patch(
    f"{BASE_URL}/posts/1",
    json=updated_title
)

print_request_anatomy(patch_response)
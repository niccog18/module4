# API Call on the browser:
# https://jsonplaceholder.typicode.com/posts/1
# https://jsonplaceholder.typicode.com/posts        ← All posts (100)
# https://jsonplaceholder.typicode.com/posts/1       ← Post #1
# https://jsonplaceholder.typicode.com/users         ← All users
# https://jsonplaceholder.typicode.com/users/3       ← User #3
# https://jsonplaceholder.typicode.com/posts?userId=2  ← Posts by user #2

# Step 1: Make the call from Python
import requests

# --- GET a single post ---
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

print(f"Status Code: {response.status_code}")  # 200 = success
print(f"Content Type: {response.headers['Content-Type']}")
print()

post = response.json()
print(f"Post Title: {post['title']}")
print(f"Post Body: {post['body'][:80]}...")
print(f"Author (userId): {post['userId']}")

# Step 2: Get a list of resources
response = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params={"userId": 1}
)

posts = response.json()
print(f"\nUser 1 has {len(posts)} posts:")
for post in posts[:3]:
    print(f"  [{post['id']}] {post['title'][:50]}...")

# Step 3: Simulate creating a resource (POST request)
new_post = {
    "title": "My First API Post",
    "body": "This was created by sending a POST request!",
    "userId": 1,
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=new_post
)

print(f"\nCreate Status: {response.status_code}")  # 201 = Created
created = response.json()
print(f"Created post with id: {created['id']}")
print(f"Title: {created['title']}")

# Note: JSONPlaceholder is a fake API, it simulates creation but doesn't actually save data.
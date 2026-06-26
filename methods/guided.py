# Using Every HTTP Method with Python

# Let's use all five core methods against JSONPlaceholder. This API accepts POST, PUT, PATCH, and DELETE requests for testing, but doesn't actually persist changes, it simulates the responses. Perfect for learning.

# Step 1: GET - Read data
import requests
import json

# GET a specific post
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(f"GET /posts/1")
print(f"Status: {response.status_code}")
post = response.json()
print(f"Title: {post['title'][:50]}...")
print()

# You should see:
# GET /posts/1
# Status: 200
# Title: sunt aut facere repellat provident occaecati exc...


# Step 2: POST - Create a new resource
# POST creates a new resource — we send data in the request body
new_post = {
    "title": "My First API Post",
    "body": "This post was created using Python and the requests library!",
    "userId": 1
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=new_post  # 'json=' automatically sets Content-Type to application/json
)

print(f"POST /posts")
print(f"Status: {response.status_code}")  # 201 = Created
created = response.json()
print(f"Created post with ID: {created['id']}")
print(f"Title: {created['title']}")
print()

# You should see:
# POST /posts
# Status: 201
# Created post with ID: 101
# Title: My First API Post

# Notice the status code is 201 (Created), not 200 (OK). REST APIs use specific status codes, you'll learn more in the next lesson.

# Step 3: PUT - Replace a resource entirely
# PUT replaces the entire resource — send ALL fields
updated_post = {
    "id": 1,
    "title": "Completely New Title",
    "body": "This body has been entirely replaced.",
    "userId": 1
}

response = requests.put(
    "https://jsonplaceholder.typicode.com/posts/1",
    json=updated_post
)

print(f"PUT /posts/1")
print(f"Status: {response.status_code}")
result = response.json()
print(f"Updated title: {result['title']}")
print()

# You should see:
# PUT /posts/1
# Status: 200
# Updated title: Completely New Title

# Step 4: PATCH - Update part of a resource
# PATCH sends only the fields that changed
partial_update = {
    "title": "Only the Title Changed"
}

response = requests.patch(
    "https://jsonplaceholder.typicode.com/posts/1",
    json=partial_update
)

print(f"PATCH /posts/1")
print(f"Status: {response.status_code}")
result = response.json()
print(f"Updated title: {result['title']}")
print(f"Body unchanged: {result['body'][:40]}...")  # Original body preserved
print()

# You should see:
# PATCH /posts/1
# Status: 200
# Updated title: Only the Title Changed
# Body unchanged: quia et suscipit\\nsuscipit recusandae con...

# The key difference from PUT: we only sent the title, and the body was preserved. With PUT, omitting the body would have replaced it with null.

# Step 5: DELETE - Remove a resource
# DELETE removes a resource
response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")

print(f"DELETE /posts/1")
print(f"Status: {response.status_code}")
print()

#You should see:
# DELETE /posts/1
# Status: 200

# Summary: All five methods at a glance
# The complete CRUD cycle:
print("=== HTTP Methods Summary ===")
print("GET    /posts/1    → Read    → 200 OK")
print("POST   /posts      → Create  → 201 Created")
print("PUT    /posts/1    → Replace → 200 OK")
print("PATCH  /posts/1    → Update  → 200 OK")
print("DELETE /posts/1    → Delete  → 200 OK")

# Every REST API in the world follows this same pattern. The resource changes, the data changes, but the methods stay the same.
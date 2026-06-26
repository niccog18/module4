# Analyzing a Real API's Design

# Let's examine how JSONPlaceholder structures its API and see if it follows REST conventions. Then we'll explore how query parameters work for filtering.
# Step 1: Map out the resource structure
import requests

# Discover the available resources
# JSONPlaceholder has: /posts, /comments, /albums, /photos, /todos, /users
resources = ["posts", "comments", "albums", "photos", "todos", "users"]

print("=== JSONPlaceholder Resource Map ===\n")
for resource in resources:
    response = requests.get(f"https://jsonplaceholder.typicode.com/{resource}")
    data = response.json()
    print(f"/{resource} — {len(data)} items")

# Step 2: Navigate nested resources
import requests

# Get a specific user
response = requests.get("https://jsonplaceholder.typicode.com/users/1")
user = response.json()
print(f"User: {user['name']}\n")

# Get that user's posts (nested resource)
response = requests.get("https://jsonplaceholder.typicode.com/users/1/posts")
posts = response.json()
print(f"User 1 has {len(posts)} posts")
print(f"First post: {posts[0]['title'][:50]}...\n")

# Get that user's todos (nested resource)
response = requests.get("https://jsonplaceholder.typicode.com/users/1/todos")
todos = response.json()
completed = sum(1 for t in todos if t['completed'])
print(f"User 1 has {len(todos)} todos ({completed} completed)")

# The nesting pattern is consistent: /users/1/posts, /users/1/todos. Once you know the pattern for one nested resource, you can predict the others.

# Step 3: Filter with query parameters
import requests

# Get all posts by user 3 using a query parameter
# This is an alternative to /users/3/posts
response = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params={"userId": 3}  # requests converts this to ?userId=3
)
posts = response.json()
print(f"Posts by user 3: {len(posts)}")
print(f"  First: {posts[0]['title'][:40]}...")
print()

# Get all completed todos for user 1
response = requests.get(
    "https://jsonplaceholder.typicode.com/todos",
    params={"userId": 1, "completed": "true"}
)
todos = response.json()
print(f"Completed todos for user 1: {len(todos)}")
for todo in todos[:3]:
    print(f"  ✓ {todo['title']}")

# Notice how requests.get() takes a params dictionary and converts it to query parameters in the URL. params={"userId": 3, "completed": "true"} becomes ?userId=3&completed=true. This is cleaner than building the URL string manually.

# Step 4: Good vs. bad URI design

# Here's a comparison to cement the patterns:
# What JSONPlaceholder does (good REST design):
# GET /posts              ← all posts
# GET /posts/1            ← specific post
# GET /posts?userId=3     ← filtered posts
# GET /posts/1/comments   ← nested resource

# What a poorly designed API might do (avoid this):
# GET /getAllPosts              ← verb in URI
# GET /getPost?id=1            ← verb, query param for ID
# GET /getPostsByUser?userId=3 ← verb, action in URI
# GET /post/1/getComments      ← singular noun, verb

# The REST way: nouns in the URI, verbs come from HTTP methods
print("REST design principles observed:")
print("  ✓ Plural nouns for collections (/posts, /users)")
print("  ✓ IDs for specific resources (/posts/1)")
print("  ✓ Query params for filtering (?userId=3)")
print("  ✓ Nesting for relationships (/posts/1/comments)")
print("  ✓ No verbs in URIs")

# These conventions aren't arbitrary rules, they make APIs predictable. When every API follows the same patterns, developers spend less time reading documentation and more time building.
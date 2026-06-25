# API Explorer
import requests

# Using the requests library and the JSONPlaceholder API (https://jsonplaceholder.typicode.com):

# GET all users and print each user's name and email
response = requests.get("https://jsonplaceholder.typicode.com/users")
users = response.json()

print("\n=== Users ===")
print(f"Status Code: {response.status_code}")
print (f"Number of Users: {len(users)}")
for user in users:
    print(f"Name: {user['name']}, Email: {user['email']}")
    
# GET all posts by user #3 (use query parameters)
params = {"userId": 3}
response = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params=params
)
posts = response.json()

print("\n=== Posts by User #3 ===")
print(f"Status Code: {response.status_code}")
print(f"Number of posts: {len(posts)}")


# GET all comments on post #1 (endpoint: /posts/1/comments)
response = requests.get(
    "https://jsonplaceholder.typicode.com/posts/1/comments"
)
comments = response.json()

print("\n=== Comments on Post #1 ===")
print(f"Status Code: {response.status_code}")
print(f"Number of comments: {len(comments)}")

# POST a new post (simulated) and print the response
new_post = {
    "title": "My New Post",
    "body": "This is a test post.",
    "userId": 1
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=new_post
)

created_post = response.json()

print("\n=== Create New Post ===")
print(f"Status Code: {response.status_code}")
print("Response:")
print(created_post)

# For each request, print the status code and the number of items returned (for list endpoints)

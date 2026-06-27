# Reading Real API Documentation

# Let's practice reading documentation by working with a real API, the GitHub REST API.

# Step 1: Find the right endpoint from documentation
import requests

# GitHub's API documentation tells us:
# Endpoint: GET /users/{username}
# Base URL: <https://api.github.com>
# Authentication: Optional for public data
# Rate limit: 60 requests/hour (unauthenticated)

# Let's use it
response = requests.get(
    "https://api.github.com/users/octocat",
    headers={"Accept": "application/vnd.github.v3+json"}  # Docs say to include this
)

user = response.json()
print(f"Name: {user['name']}")
print(f"Public repos: {user['public_repos']}")
print(f"Followers: {user['followers']}")
print(f"Account created: {user['created_at']}")

# Step 2: Use query parameters from the docs
import requests

# GitHub docs for "List repositories for a user":
# GET /users/{username}/repos
# Query params: type, sort, direction, per_page, page

response = requests.get(
    "https://api.github.com/users/octocat/repos",
    params={
        "sort": "updated",    # Sort by most recently updated
        "per_page": 5,        # Only get 5 results
        "direction": "desc"   # Newest first
    },
    headers={"Accept": "application/vnd.github.v3+json"}
)

repos = response.json()
print(f"Showing {len(repos)} most recently updated repos:\n")
for repo in repos:
    print(f"  {repo['name']}")
    print(f"    Language: {repo.get('language', 'Not specified')}")
    print(f"    Stars: {repo['stargazers_count']}")
    print(f"    Updated: {repo['updated_at'][:10]}")
    print()

# Step 3: Check rate limits via headers
import requests

# The docs tell us rate limit info is in response headers
response = requests.get(
    "https://api.github.com/users/octocat",
    headers={"Accept": "application/vnd.github.v3+json"}
)

print("=== GitHub API Rate Limits ===")
print(f"Limit:     {response.headers.get('X-RateLimit-Limit', 'N/A')}")
print(f"Remaining: {response.headers.get('X-RateLimit-Remaining', 'N/A')}")
print(f"Reset:     {response.headers.get('X-RateLimit-Reset', 'N/A')}")

# Convert the reset timestamp to a readable time
import datetime
reset_timestamp = response.headers.get('X-RateLimit-Reset')
if reset_timestamp:
    reset_time = datetime.datetime.fromtimestamp(int(reset_timestamp))
    print(f"Resets at:  {reset_time.strftime('%H:%M:%S')}")

# Every piece of information we used, the endpoint path, the query parameters, the Accept header, the rate limit headers, came from the documentation. This is how professional developers work: read the docs first, code second.
import requests

BASE_URL = "https://api.github.com"

# Fetches the 3 most-starred repositories for the user "google" (hint: use sort and per_page parameters)
def main():
    # Endpoint for Google's repositories
    url = f"{BASE_URL}/users/google/repos"

    # Query parameters
    params = {
        "sort": "stars",
        "per_page": 3
    }

    # Send the GET request
    response = requests.get(url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        repos = response.json()

        print("Top 3 Google Repositories:\n")

# For each repo, prints the name, description, star count, and primary language
        for repo in repos:
            print(f"Name: {repo['name']}")
            print(f"Description: {repo['description']}")
            print(f"Stars: {repo['stargazers_count']}")
            print(f"Primary Language: {repo['language']}")
            print("-" * 40)

        # Print the remaining rate limit
        remaining = response.headers.get("X-RateLimit-Remaining")
        print(f"\nRemaining Rate Limit: {remaining}")

    else:
        print(f"Request failed with status code {response.status_code}")


if __name__ == "__main__":
    main()

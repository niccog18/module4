import requests

BASE_URL = "https://api.github.com"

def create_auth_headers(api_key, auth_type):
    """
    Create authentication headers.

    Args:
        api_key (str): API key or token.
        auth_type (str): Either "bearer" or "api-key".

    Returns:
        dict: Headers dictionary.
    """
    if auth_type.lower() == "bearer":
        return {"Authorization": f"Bearer {api_key}"}

    elif auth_type.lower() == "api-key":
        return {"X-API-Key": api_key}

    else:
        raise ValueError("auth_type must be 'bearer' or 'api-key'")
    
def main():    
# Making an unauthenticated request to https://api.github.com/user and printing the status code (you should get 401)
    response = requests.get(f"{BASE_URL}/user")
    print(f"GET /user status code: {response.status_code}")

# Making an unauthenticated request to https://api.github.com/users/octocat and printing the status code (this public endpoint should return 200)
    response = requests.get(f"{BASE_URL}/users/octocat")
    print(f"GET /users/octocat status code: {response.status_code}")
    
# A function called create_auth_headers() that takes an API key and an auth type ("bearer" or "api-key") and returns the correct headers dictionary
    bearer_headers = create_auth_headers("your_token_here", "bearer")
    api_key_headers = create_auth_headers("your_api_key_here", "api-key")

    print("\nBearer headers:")
    print(bearer_headers)

    print("\nAPI Key headers:")
    print(api_key_headers)


if __name__ == "__main__":
    main()
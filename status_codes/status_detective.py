import requests

def status_report(method, url, data=None):
# Success Codes and Client Errors
    if method == "GET":
        response = requests.get(url)

    elif method == "POST":
        response = requests.post(url, json=data)

    elif method == "DELETE":
        response = requests.delete(url)

    else:
        return f"{method} is not a supported method.\n"

    if 200 <= response.status_code < 300:
        category = "Success"
    elif 400 <= response.status_code < 500:
        category = "Client Error"
    elif 500 <= response.status_code < 600:
        category = "Server Error"
    else:
        category = "Other"

    # Code Interpreter
    descriptions = {
        200: "Request succeeded — resource returned",
        201: "Resource created successfully",
        204: "Request succeeded — no content returned",
        404: "Resource not found"
    }

    description = descriptions.get(
        response.status_code,
        "Status code received"
    )

    # Return formatted report
    return (
        f"{method} {url.replace('https://jsonplaceholder.typicode.com', '')}\n"
        f"  Status: {response.status_code} ({category})\n"
        f"  Description: {description}\n"
    )


# GET /posts/1
print(status_report(
    "GET",
    "https://jsonplaceholder.typicode.com/posts/1"
))

# GET /posts/99999
print(status_report(
    "GET",
    "https://jsonplaceholder.typicode.com/posts/99999"
))

# POST /posts
new_post = {
    "title": "Test Post",
    "body": "Created by Python",
    "userId": 1
}

print(status_report(
    "POST",
    "https://jsonplaceholder.typicode.com/posts",
    new_post
))

# DELETE /posts/1
print(status_report(
    "DELETE",
    "https://jsonplaceholder.typicode.com/posts/1"
))

# GET /invalidendpoint
print(status_report(
    "GET",
    "https://jsonplaceholder.typicode.com/invalidendpoint"
))

# GET /users/1/todos
print(status_report(
    "GET",
    "https://jsonplaceholder.typicode.com/users/1/todos"
))
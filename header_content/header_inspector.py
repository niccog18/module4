import requests

def header_inspector(method, url):
# Makes GET requests to three different endpoints:
    if method == "GET":
        response = requests.get(url)
    else:
        return f"{method} is not a supported method.\n"
    print(f"\nURL: {url}")

    print("Content-Type:",
          response.headers.get("Content-Type", "Not specified"))

    print("Content-Length:",
          response.headers.get("Content-Length", "Not specified"))
    # Check caching headers
    cache_headers = [
        "Cache-Control",
        "Expires",
        "Last-Modified"
]

    found_cache_headers = []
    for header in cache_headers:
        if header in response.headers:
            found_cache_headers.append(header)
    if found_cache_headers:
        print("Caching Headers Present:", found_cache_headers)
    else:
        print("Caching Headers Present: None")

# Rate-limiting headers
    rate_limit_headers = []

    for header in response.headers:
        if "rate" in header.lower():
            rate_limit_headers.append(header)
    if rate_limit_headers:
        print("Rate Limiting Headers:", rate_limit_headers)
    else:
        print("Rate Limiting Headers: None")

    print("Total Headers:",
          len(response.headers))
    print("-" * 40)
    
    # https://jsonplaceholder.typicode.com/posts/1
header_inspector(
    "GET",
    "https://jsonplaceholder.typicode.com/posts/1")

    # https://jsonplaceholder.typicode.com/users/1
header_inspector(
    "GET",
    "https://jsonplaceholder.typicode.com/users/1"
)

    # https://httpbin.org/get
header_inspector(
    "GET",
    "https://httpbin.org/get"
)

# Make a POST request to https://httpbin.org/post with a JSON body and custom headers (X-Student-Name set to your name). Print the response, httpbin.org echoes back everything you sent, so you can verify your headers were received.
headers = {
    "X-Student-Name": "Nicco"
}
data = {
    "course": "Python",
    "assignment": "Header Inspector"
}
response = requests.post(
    "https://httpbin.org/post",
    json=data,
    headers=headers
)
print(response.json())
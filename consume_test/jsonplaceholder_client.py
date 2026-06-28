import requests


class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint, params=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def post(self, endpoint, data=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response.json()


class JSONPlaceholderClient(APIClient):
    def __init__(self):
        super().__init__("https://jsonplaceholder.typicode.com")

    def get_user(self, user_id):
        return self.get(f"/users/{user_id}")

    def get_user_posts(self, user_id):
        return self.get("/posts", params={"userId": user_id})

    def create_post(self, user_id, title, body):
        return self.post("/posts", data={
            "userId": user_id,
            "title": title,
            "body": body
        })

    def search_posts(self, query):
        all_posts = self.get("/posts")
        
        return [
            post for post in all_posts
            if query.lower() in post["title"].lower()
        ]
    

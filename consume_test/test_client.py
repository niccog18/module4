from jsonplaceholder_client import JSONPlaceholderClient


def main():
    client = JSONPlaceholderClient()

    # 1. Get user 5 profile
    user = client.get_user(5)
    print("User Name:", user["name"])
    print("City:", user["address"]["city"])

    print("\n------------------------\n")

    # 2. Get user 5 posts
    posts = client.get_user_posts(5)
    print("Number of posts:", len(posts))

    print("\n------------------------\n")

    # 3. Create a new post
    new_post = client.create_post(
        user_id=5,
        title="Learning API Clients",
        body="This is a test post created via the API client."
    )
    print("New Post ID:", new_post.get("id"))

    print("\n------------------------\n")

    # 4. Search posts containing "qui"
    matches = client.search_posts("qui")
    print('Posts containing "qui":', len(matches))


if __name__ == "__main__":
    main()
"""
Module 4 Project — Part 1: API Exploration
Explore 3 public APIs and document what you find.

Instructions:
- Fill in each TODO section
- Run the script to verify your code works
- Document your findings in comments and print statements
"""

import requests

BASE_URLS = {
    "jsonplaceholder": "https://jsonplaceholder.typicode.com",
    "pokeapi": "https://pokeapi.co/api/v2",
    "restcountries": "https://restcountries.com/v3.1",
}

# ============================================================
# API 1: JSONPlaceholder
# Documentation: https://jsonplaceholder.typicode.com/guide/
# ============================================================

def explore_jsonplaceholder():
    print("\n=== API 1: JSONPlaceholder ===")

    base = BASE_URLS["jsonplaceholder"]

    # TODO 1: GET all users    
    try:
        response = requests.get(f"{base}/users")
        print("\nGET /users")
        print("Status:", response.status_code, response.reason)

        users = response.json()
        print(f"Total users: {len(users)}")

        for user in users:
            print(f"- {user['name']} ({user['email']})")

    except requests.exceptions.RequestException as e:
        print("Request failed:", e)

    # TODO 2: GET posts by a specific user
    try:
        response = requests.get(f"{base}/posts", params={"userId": 1})

        print("\nGET /posts?userId=1")
        print("Status:", response.status_code, response.reason)

        posts = response.json()
        print("Post count:", len(posts))

        if posts:
            print("First post title:", posts[0]["title"])

    except requests.exceptions.RequestException as e:
        print("Request failed:", e)

    # TODO 3: POST a new post
    try:
        payload = {
            "title": "Learning REST APIs",
            "body": "Testing POST request",
            "userId": 1
        }

        response = requests.post(f"{base}/posts", json=payload)

        print("\nPOST /posts")
        print("Status:", response.status_code, response.reason)

        data = response.json()
        print("Returned ID:", data.get("id"))

    except requests.exceptions.RequestException as e:
        print("Request failed:", e)


# ============================================================
# API 2: PokeAPI
# Documentation: https://pokeapi.co/docs/v2
# ============================================================

def explore_pokeapi():
    print("\n=== API 2: PokeAPI ===")

    base = BASE_URLS["pokeapi"]

    # TODO 4: GET a specific Pokémon (try ID 1 = Bulbasaur, or 25 = Pikachu)
    try:
        response = requests.get(f"{base}/pokemon/25")  # Pikachu

        print("\nGET /pokemon/25")
        print("Status:", response.status_code, response.reason)

        pokemon = response.json()

        print("Name:", pokemon["name"])
        print("Height:", pokemon["height"])
        print("Weight:", pokemon["weight"])

        abilities = [a["ability"]["name"] for a in pokemon["abilities"]]
        print("Abilities:", abilities)

    except requests.exceptions.RequestException as e:
        print("Request failed:", e)

    # TODO 5: Follow the first type URL from the Pokémon response
    try:
        response = requests.get(f"{base}/pokemon/25")
        pokemon = response.json()

        type_url = pokemon["types"][0]["type"]["url"]
        type_name = pokemon["types"][0]["type"]["name"]

        type_response = requests.get(type_url)
        type_data = type_response.json()

        print("\nPokémon type:", type_name)
        print("First 5 Pokémon of this type:")

        pokemon_list = type_data["pokemon"][:5]
        for p in pokemon_list:
            print("-", p["pokemon"]["name"])

    except requests.exceptions.RequestException as e:
        print("Request failed:", e)


    # TODO 6: Document the response structure in a comment below:
    """
    /pokemon/<id> response top-level keys:
    - abilities
    - base_experience
    - forms
    - game_indices
    - height
    - id
    - name
    - species
    - sprites
    - stats
    - types
    - weight
    """


# ============================================================
# API 3: REST Countries
# Documentation: https://restcountries.com/#endpoints
# ============================================================

def explore_restcountries():
    print("\n=== API 3: REST Countries ===")

    base = BASE_URLS["restcountries"]

    # TODO 7: GET a country by name (try "Japan" or any country you like)
    try:
        response = requests.get(f"{base}/name/japan")

        print("\nGET /name/japan")
        print("Status:", response.status_code, response.reason)

        data = response.json()

        if not isinstance(data, list):
            print("Unexpected response format:")
            print(data)
            return  # stops function safely

        data = data[0]

        print("Official Name:", data["name"]["official"])
        print("Capital:", data.get("capital", ["N/A"])[0])
        print("Population:", data["population"])
        print("Region:", data["region"])

    except requests.exceptions.RequestException as e:
        print("Request failed:", e)

    # TODO 8: GET all countries in a region (try "Europe" or "Asia")
    try:
        response = requests.get(f"{base}/region/asia")

        print("\nGET /region/asia")
        print("Status:", response.status_code, response.reason)

        countries = response.json()

        names = sorted([c["name"]["common"] for c in countries])

        print("Total countries:", len(names))
        print("First 10 alphabetically:")
        for name in names[:10]:
            print("-", name)

    except requests.exceptions.RequestException as e:
        print("Request failed:", e)

    # TODO 9: Handle an error
    # Try a country name that doesn't exist
    # Handle the response gracefully (don't crash)
    try:
        response = requests.get(f"{base}/name/thiscountrydoesnotexist")

        print("\nGET invalid country")
        print("Status:", response.status_code, response.reason)

        if response.status_code == 404:
            print("Country not found — handled gracefully.")

    except requests.exceptions.RequestException as e:
        print("Request failed:", e)


# ============================================================
# Run all explorations
# ============================================================

if __name__ == "__main__":
    explore_jsonplaceholder()
    explore_pokeapi()
    explore_restcountries()
    print("\n=== Exploration complete! ===")

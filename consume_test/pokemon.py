import requests
import random
from datetime import datetime

POKEAPI_BASE = "https://pokeapi.co/api/v2"
OPEN_METEO_URL = "https://api.open-meteo.com/v1/forecast"

# Example location: Santa Ana, CA
LAT = 33.7455
LON = -117.8677


# API FUNCTIONS
def get_weather():
    """Fetch current weather data"""
    try:
        url = f"{OPEN_METEO_URL}?latitude={LAT}&longitude={LON}&current_weather=true"
        res = requests.get(url, timeout=10)
        res.raise_for_status()
        return res.json()
    except requests.RequestException as e:
        print(f"[Weather API Error] {e}")
        return None


def get_random_pokemon():
    """Fetch a random Pokémon"""
    try:
        pokemon_id = random.randint(1, 1025)
        url = f"{POKEAPI_BASE}/pokemon/{pokemon_id}"
        res = requests.get(url, timeout=10)
        res.raise_for_status()
        return res.json()
    except requests.RequestException as e:
        print(f"[PokéAPI Error] {e}")
        return None


def get_pokemon_species(name):
    """Fetch Pokémon lore / flavor text"""
    try:
        url = f"{POKEAPI_BASE}/pokemon-species/{name}"
        res = requests.get(url, timeout=10)
        res.raise_for_status()
        return res.json()
    except requests.RequestException as e:
        print(f"[Species API Error] {e}")
        return None


# COMBINE LOGIC
def build_pokemon_of_the_day():
    print("\n🎴 Generating Pokémon of the Day...\n")

    pokemon = get_random_pokemon()
    weather = get_weather()

    if not pokemon:
        print("❌ Could not fetch Pokémon. Try again later.")
        return

    name = pokemon["name"].title()
    types = [t["type"]["name"] for t in pokemon["types"]]

    # --- 3rd API request (species lore)
    species = get_pokemon_species(pokemon["name"])
    flavor = "No lore available."

    if species:
        for entry in species.get("flavor_text_entries", []):
            if entry["language"]["name"] == "en":
                flavor = entry["flavor_text"].replace("\n", " ").strip()
                break

    # Weather parsing
    weather_text = "Weather unavailable."
    temp = None

    if weather and "current_weather" in weather:
        w = weather["current_weather"]
        temp = w["temperature"]
        weather_text = f"{temp}°C, wind {w['windspeed']} km/h"

    # OUTPUT REPORT
    print("=" * 45)
    print("🌟 POKÉMON OF THE DAY REPORT 🌟")
    print("=" * 45)
    print(f"📅 Date: {datetime.now().strftime('%Y-%m-%d')}")
    print()
    print(f"🎴 Pokémon: {name}")
    print(f"🏷️ Type(s): {', '.join(types)}")
    print()
    print("📖 Pokédex Entry:")
    print(f"   {flavor}")
    print()
    print("🌤️ Current Weather (Santa Ana, CA):")
    print(f"   {weather_text}")
    print("=" * 45)

    # COMBINED INSIGHT (DATA MERGING)
    if temp is not None:
        if temp >= 30:
            mood = "🔥 It’s extremely hot—this Pokémon would prefer water or shade!"
        elif temp <= 10:
            mood = "❄️ It’s cold—this Pokémon might struggle or become more defensive!"
        else:
            mood = "🌈 Mild weather—perfect conditions for Pokémon encounters!"

        print("\n🧠 Pokémon of the Day Insight:")
        print(f"   {name}: {mood}")

    # Bonus trait mapping (simple logic fusion)
    if "fire" in types and temp and temp > 25:
        print("🔥 BONUS MATCH: Fire-type synergy with hot weather detected!")
    elif "water" in types and temp and temp > 25:
        print("💧 WATER WARNING: Water-type may be stressed in heat!")


# RUN PROGRAM
if __name__ == "__main__":
    build_pokemon_of_the_day()
#!/usr/bin/node

import requests
import sys

def get_movie_characters(movie_id):
    # Base URL for the Star Wars API
    base_url = "https://swapi.dev/api"

    # Get the film details
    film_response = requests.get(f"{base_url}/films/{movie_id}/")

    if film_response.status_code != 200:
        print(f"Error: Unable to fetch film with ID {movie_id}")
        return

    film_data = film_response.json()
    character_urls = film_data.get("characters", [])

    # Fetch and print each character's name
    for url in character_urls:
        character_response = requests.get(url)

        if character_response.status_code == 200:
            character_data = character_response.json()
            print(character_data.get("name"))
        else:
            print(f"Error: Unable to fetch character data from {url}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <movie_id>")
        sys.exit(1)

    movie_id = sys.argv[1]
    get_movie_characters(movie_id)

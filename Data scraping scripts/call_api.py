import requests
import json

with open("api_football_key", "r") as file:
    api_key = file.read().strip()

headers = {
    "x-apisports-key": api_key
}


def call_API(endpoint, params):

    api_url = f"https://v3.football.api-sports.io/{endpoint}"

    response = requests.get(
        api_url,
        headers=headers,
        params=params
    )

    response.raise_for_status()
    

    return response.json()



from call_api import call_API

def get_players(league, season):

    page = 1

    all_players = []

    params = {"league": league,
              "season": season,
              "page": page}


    data = call_API("players", params)

    all_players.extend(data["response"])

    total_pages = data["paging"]["total"]

    while page < total_pages:
        page += 1
        params["page"] = page
        data = call_API("players", params)
        all_players.extend(data["response"])

    return all_players



all_players = get_players(39, 2022)

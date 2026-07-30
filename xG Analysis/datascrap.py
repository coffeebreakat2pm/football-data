# Libraries
import soccerdata as sd
import pandas as pd
import streamlit as st

# Data collection

def season_label(y: int) -> str:
    """Returns a season label like 2015/16."""
    return f"{y}/{str(y + 1)[-2:]}"


def understat_season_code(y: int) -> str:
    """Returns an explicit Understat season code like 15-16 (avoids ambiguity warnings)."""
    return f"{str(y)[-2:]}-{str(y + 1)[-2:]}"


def players_all_seasons(
    league_list,
    start_year=2015,
    end_year=2025,
    out_file=None,
):
    if out_file is None:
        leagues = (
            league_list
            .replace(" ", "_")
            .replace("-", "_")
        )
        out_file = f"{leagues}_players_{start_year}-{str(start_year + 1)[-2:]}_to_{end_year}-{str(end_year + 1)[-2:]}.csv"

    all_dfs = []

    for y in range(start_year, end_year + 1):
        label = season_label(y)
        season_code = understat_season_code(y)
        print(f"Fetching {label} (code={season_code})...")

        try:
            understat = sd.Understat(leagues=league_list, seasons=season_code)
            df = understat.read_player_season_stats().copy()
            all_dfs.append(df)
            print(f"Added {label}: {len(df)} rows")
        except Exception as e:
            print(f"Skipped {label}: {e}")

    if not all_dfs:
        raise ValueError("No season data was collected.")

    combined = pd.concat(all_dfs, ignore_index=False)
    combined.to_csv(out_file, index=True)
    print(f"Saved combined file: {out_file} | total rows: {len(combined)}")
    return combined



# EDA

leagues = ["ENG-Premier League", "ESP-La Liga", "ITA-Serie A", "GER-Bundesliga", "FRA-Ligue 1"]
for league in leagues:
    players_all_seasons(league_list=league, start_year=2015, end_year=2025)



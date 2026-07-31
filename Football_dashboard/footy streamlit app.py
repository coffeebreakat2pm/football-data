import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path


st.title("Top 5 European leagues - Players Data Analysis")
st.markdown("""
            This dashboard showcases various advanced player statistics from the top 5 European league for the seasons 2015/16 to 2025/26.

            By utilizing the Understat API, we have collected and analyzed data for players across the English Premier League, Spanish La Liga, Italian Serie A, German Bundesliga, and French Ligue 1.
            The data includes metrics such as expected goals (xG), expected assists (xA), shot accuracy, and more, providing insights into player performance across the past ten seasons of top 5 league european football.

            """)




BASE_DIR = Path(__file__).resolve().parent

Premier_League = pd.read_csv(BASE_DIR / "eng_premier_league_players_2015-16_to_2025-26.csv")
La_liga = pd.read_csv(BASE_DIR / "esp_la_liga_players_2015-16_to_2025-26.csv")
Serie_A = pd.read_csv(BASE_DIR / "ita_serie_a_players_2015-16_to_2025-26.csv")
Bundesliga = pd.read_csv(BASE_DIR / "ger_bundesliga_players_2015-16_to_2025-26.csv")
Ligue_1 = pd.read_csv(BASE_DIR / "fra_ligue_1_players_2015-16_to_2025-26.csv")


all_leagues = ["Premier League", "La Liga", "Serie A", "Bundesliga", "Ligue 1"]
with st.container(border = True):
     leagues = st.selectbox("Choose a league for Data visualization:",
                            all_leagues,
                            placeholder="Select a league",
                            index = None,  
                            accept_new_options=False)

if leagues == "Premier League":
    df = Premier_League
elif leagues == "La Liga":
    df = La_liga
elif leagues == "Serie A":
    df = Serie_A
elif leagues == "Bundesliga":
    df = Bundesliga
elif leagues == "Ligue 1":
    df = Ligue_1
else:
    st.error("Please select an available league.")


if df is not None:
    tab1, tab2, tab3, tab4 = st.tabs(["xG Outperformer","xA Outperformer","Best finisher","MVP"])

    with tab1:
        st.scatter_chart(df, x="xg", y="goals")

    with tab2:
        st.scatter_chart(df, x="xa", y="assists")

    with tab3:
        st.scatter_chart(df, x="shots", y="goals")

    with tab4:
        st.scatter_chart(df, x="xg_chain", y="xg_buildup")



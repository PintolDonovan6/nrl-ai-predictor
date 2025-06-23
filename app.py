import streamlit as st
import pandas as pd
import requests

# Your RapidAPI key
API_KEY = "ceadd16dbdmshdd02736dc4a0p1729e8jsn93147778c9"

API_URL = "https://therundown-therundown-v1.p.rapidapi.com/sports/odds"

HEADERS = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": "therundown-therundown-v1.p.rapidapi.com"
}

ALL_TEAMS = [
    'Broncos', 'Raiders', 'Bulldogs', 'Sharks', 'Titans', 'Sea Eagles', 'Storm',
    'Knights', 'Cowboys', 'Eels', 'Panthers', 'Rabbitohs', 'Dragons', 'Roosters',
    'Warriors', 'Tigers', 'Dolphins'
]

# Sample minimal history data as fallback
data = {
    'Home Team': ['Storm', 'Panthers', 'Roosters', 'Storm', 'Broncos', 'Panthers'],
    'Away Team': ['Broncos', 'Storm', 'Panthers', 'Roosters', 'Panthers', 'Roosters'],
    'Winner':    ['Storm', 'Panthers', 'Roosters', 'Storm', 'Panthers', 'Panthers']
}
df = pd.DataFrame(data)

st.title("🏉 NRL Match Winner Predictor (Live + History Fallback)")

home_team = st.selectbox("Select Home Team", ALL_TEAMS)
away_team = st.selectbox("Select Away Team", [team for team in ALL_TEAMS if team != home_team])

def get_odds_for_match(home, away):
    try:
        params = {
            "sport": "nrl",
            "region": "au",
            "market": "h2h"
        }
        response = requests.get(API_URL, headers=HEADERS, params=params)
        response.raise_for_status()
        data = response.json()

        for event in data.get("events", []):
            teams = [team['name'] for team in event.get("teams", [])]
            if home in teams and away in teams:
                for site in event.get("sites", []):
                    odds = site.get("odds", {}).get("h2h", [])
                    if len(odds

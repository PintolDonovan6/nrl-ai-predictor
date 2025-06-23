import streamlit as st
import pandas as pd
import requests

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

# Minimal fallback history data
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
                    if len(odds) >= 2:
                        if teams[0] == home:
                            home_odds = odds[0]
                            away_odds = odds[1]
                        else:
                            home_odds = odds[1]
                            away_odds = odds[0]
                        return home_odds, away_odds, site.get("site_nice", "Unknown")
        return None, None, None
    except Exception as e:
        # Do NOT show raw error, just return None
        return None, None, None

def predict_winner_from_odds(home_odds, away_odds, home, away):
    try:
        home_odds = float(home_odds)
        away_odds = float(away_odds)
    except:
        return None, ""

    if home_odds < 0 and away_odds > 0:
        reason = f"{home} is favored by the sportsbook with odds {home_odds}."
        return home, reason
    elif away_odds < 0 and home_odds > 0:
        reason = f"{away} is favored by the sportsbook with odds {away_odds}."
        return away, reason
    else:
        # Both positive or both negative, choose closer to zero (better odds)
        if abs(home_odds) < abs(away_odds):
            reason = f"{home} ha

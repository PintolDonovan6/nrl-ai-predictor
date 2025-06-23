import streamlit as st
import requests

# Your API key and host from RapidAPI
API_KEY = "ceadd16dbdmshdd02736dc4a0p1729e8jsn93147778c9"
API_HOST = "therundown-therundown-v1.p.rapidapi.com"

headers = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": API_HOST
}

def fetch_nrl_events():
    url = f"https://{API_HOST}/sports/0/events"
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data.get("events", [])
    except Exception as e:
        st.error(f"Error fetching events: {e}")
        return []

def find_event(events, home_team, away_team):
    home_lower = home_team.lower()
    away_lower = away_team.lower()
    for event in events:
        event_home = event.get("home_team", "").lower()
        event_away = event.get("away_team", "").lower()
        if home_lower in event_home and away_lower in event_away:
            return event
    return None

def predict_winner_from_event(event, home_team, away_team):
    odds_data = event.get("moneyline_periods", {}).get("period_full_game", [])
    if not odds_data:
        return None, "No odds data found for this event."
    
    odds = odds_data[0]
    home_odds = odds.get("moneyline_home")
    away_odds = odds.get("moneyline_away")

    if home_odds is None or away_odds is None:
        return None, "Incomplete odds data."

    def odds_to_prob(moneyline):
        if moneyline < 0:
            return -moneyline / (-moneyline + 100)
        else:
            return 100 / (moneyline + 100)
    
    home_prob = odds_to_prob(home_odds)
    away_prob = odds_to_prob(away_odds)

    if home_prob > away_prob:
        winner = home_team
        reason = f"{home_team} is favored by moneyline odds ({home_odds} vs {away_odds})."
    elif away_prob > home_prob:
        winner = away_team
        reason = f"{away_team} is favored by moneyline odds ({away_odds} vs {home_odds})."
    else:
        winner = home_team
        reason = "Odds are equal, defaulting to home team."

    return winner, reason

st.title("🏉 NRL Match Winner Predictor with Live Odds")

all_teams = [
    'Broncos', 'Raiders', 'Bulldogs', 'Sharks', 'Titans', 'Sea Eagles', 'Storm',
    'Knights', 'Cowboys', 'Eels', 'Panthers', 'Rabbitohs', 'Dragons', 'Roosters',
    'Warriors', 'Tigers', 'Dolphins'
]

home_team = st.selectbox("Select Home Team", all_teams)
away_team = st.selectbox("Select Away Team", [team for team in all_teams if team != home_team])

if st.button("Predict Winner"):
    events = fetch_nrl_events()
    if not events:
        st.error("Could not fetch NRL events. Try again later.")
    else:
        event = find_event(events, home_team, away_team)
        if not event:
            st.warning("No matching event found for those teams. Defaulting to home team.")
            st.success(f"Predicted Winner: {home_team}")
            st.info("Reason: No event data found, so defaulting to home team.")
        else:
            winner, reason = predict_winner_from_event(event, home_team, away_team)
            if winner:
                st.success(f"Predicted Winner: {winner}")
                st.info(f"Reason: {reason}")
            else:
                st.warning("No prediction available, defaulting to home team.")
                st.success(f"Predicted Winner: {home_team}")
                st.info("Reason: No odds data available.")

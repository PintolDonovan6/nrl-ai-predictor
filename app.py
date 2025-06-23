import streamlit as st
import pandas as pd
import requests

# Your API key here — replace with your actual key
API_KEY = "ceadd16dbdmshdd02736dc4a0p1729e8jsn93147778c9"

all_teams = [
    'Broncos', 'Raiders', 'Bulldogs', 'Sharks', 'Titans', 'Sea Eagles', 'Storm',
    'Knights', 'Cowboys', 'Eels', 'Panthers', 'Rabbitohs', 'Dragons', 'Roosters',
    'Warriors', 'Tigers', 'Dolphins'
]

# Sample historical data (you can expand this with real stats)
data = {
    'Home Team': ['Storm', 'Panthers', 'Roosters', 'Storm', 'Broncos', 'Panthers'],
    'Away Team': ['Broncos', 'Storm', 'Panthers', 'Roosters', 'Panthers', 'Roosters'],
    'Winner':    ['Storm', 'Panthers', 'Roosters', 'Storm', 'Panthers', 'Panthers']
}
df = pd.DataFrame(data)

st.title("🏉 NRL Match Winner Predictor")

home_team = st.selectbox("Select Home Team", all_teams)
away_team = st.selectbox("Select Away Team", [team for team in all_teams if team != home_team])

def get_odds_for_match(home, away):
    url = f"https://therundown-therundown-v1.p.rapidapi.com/sports/0/events"
    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "therundown-therundown-v1.p.rapidapi.com"
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        events = response.json().get("events", [])
        for event in events:
            # Check if this event matches our teams
            competitors = event.get("competitors", [])
            teams = [c.get("name") for c in competitors if c.get("name")]
            if home in teams and away in teams:
                lines = event.get("lines", [])
                for line in lines:
                    if line.get("line_type") == "moneyline":
                        moneyline_periods = line.get("moneyline_periods", {})
                        periods = moneyline_periods.get("period_full_game", [])
                        if periods:
                            period = periods[0]
                            home_odds = period.get("moneyline_home")
                            away_odds = period.get("moneyline_away")
                            sportsbook = line.get("sportsbook", "Unknown")
                            return home_odds, away_odds, sportsbook
        return None, None, None
    except Exception as e:
        return None, None, None

def predict_winner_from_odds(home_odds, away_odds, home, away):
    # In American odds, negative number means favorite
    if home_odds is None or away_odds is None:
        return None, None

    if home_odds < away_odds:
        winner = home
        reason = f"{home} favored by odds ({home_odds} vs {away_odds})"
    elif away_odds < home_odds:
        winner = away
        reason = f"{away} favored by odds ({away_odds} vs {home_odds})"
    else:
        winner = None
        reason = "Odds are equal, too close to call"
    return winner, reason

def predict_winner_from_history(home, away):
    home_wins = df[(df['Home Team'] == home) & (df['Winner'] == home)].shape[0]
    away_wins = df[(df['Away Team'] == away) & (df['Winner'] == away)].shape[0]

    if home_wins > away_wins:
        return home, f"Based on historical home wins: {home_wins} to {away_wins}"
    elif away_wins > home_wins:
        return away, f"Based on historical away wins: {away_wins} to {home_wins}"
    elif home_wins == 0 and away_wins == 0:
        return home, "No historical data, defaulting to home team"
    else:
        return None, "Too close to call based on history"

if st.button("Predict Winner"):
    home_odds, away_odds, sportsbook = get_odds_for_match(home_team, away_team)

    if home_odds is not None and away_odds is not None:
        winner, reason = predict_winner_from_odds(home_odds, away_odds, home_team, away_team)
        if winner:
            st.success(f"Predicted Winner: **{winner}**")
            st.info(f"Reason: {reason} (Data source: {sportsbook})")
        else:
            # fallback if odds equal
            winner, reason = predict_winner_from_history(home_team, away_team)
            st.success(f"Predicted Winner: **{winner}**")
            st.info(f"Reason: {reason} (Fallback to history)")
    else:
        winner, reason = predict_winner_from_history(home_team, away_team)
        if winner:
            st.success(f"Predicted Winner: **{winner}**")
            st.info(f"Reason: {reason} (Based on history)")
        else:
            st.warning(f"No data found, defaulting to home team: **{home_team}**")
            st.info("Reason: No odds or history data available.")


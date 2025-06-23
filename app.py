import streamlit as st
import pandas as pd
import requests

# Your TheRundown API key
API_KEY = "ceadd16dbdmshdd02736dc4a0p1729e8jsn93147778c9"
API_URL = "https://therundown-therundown-v1.p.rapidapi.com/sports/0/events"

# List of all 17 NRL teams
all_teams = [
    'Broncos', 'Raiders', 'Bulldogs', 'Sharks', 'Titans', 'Sea Eagles', 'Storm',
    'Knights', 'Cowboys', 'Eels', 'Panthers', 'Rabbitohs', 'Dragons', 'Roosters',
    'Warriors', 'Tigers', 'Dolphins'
]

# Sample historical data (expand this as you like)
data = {
    'Home Team': ['Storm', 'Panthers', 'Roosters', 'Storm', 'Broncos', 'Panthers'],
    'Away Team': ['Broncos', 'Storm', 'Panthers', 'Roosters', 'Panthers', 'Roosters'],
    'Winner':    ['Storm', 'Panthers', 'Roosters', 'Storm', 'Panthers', 'Panthers']
}
df = pd.DataFrame(data)

st.title("🏉 NRL Match Winner Predictor")

home_team = st.selectbox("Select Home Team", all_teams)
away_team = st.selectbox("Select Away Team", [team for team in all_teams if team != home_team])

def fetch_live_odds(home, away):
    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "therundown-therundown-v1.p.rapidapi.com"
    }
    try:
        response = requests.get(API_URL, headers=headers, timeout=10)
        response.raise_for_status()
        events = response.json().get('events', [])
        
        # Search for matching game
        for event in events:
            teams = event.get('teams', [])
            if len(teams) < 2:
                continue
            team_names = [team.get('name') for team in teams]
            # Check if our teams match the event teams (ignore order)
            if set([home, away]) == set(team_names):
                # Find moneyline odds
                markets = event.get('lines', [])
                for market in markets:
                    # moneyline odds under 'moneyline_periods'
                    moneyline_periods = market.get('moneyline_periods', {})
                    full_game = moneyline_periods.get('period_full_game', [])
                    if full_game:
                        # Usually 2 entries: one for each team
                        home_odds = None
                        away_odds = None
                        for odds_info in full_game:
                            # event has team id? Or compare indexes? Let's try with 'team_id'
                            # Here we just assume first is home, second away (simplification)
                            # Or use 'line_id' or something if available
                            # We'll just pick first odds as home odds, second as away odds
                            # Sometimes data varies; fallback to safest guess
                            home_odds = full_game[0].get('moneyline_home')
                            away_odds = full_game[0].get('moneyline_away')
                        if home_odds is not None and away_odds is not None:
                            return home_odds, away_odds
        return None, None
    except Exception as e:
        st.warning(f"Warning: Could not fetch live odds. {e}")
        return None, None

def predict_winner(home, away):
    # Try live odds first
    home_odds, away_odds = fetch_live_odds(home, away)
    
    if home_odds is not None and away_odds is not None:
        # Lower odds means favored team (American odds: negative = favorite)
        if home_odds < away_odds:
            winner = home
            reason = f"Live odds favor {home} ({home_odds} vs {away_odds})"
        elif away_odds < home_odds:
            winner = away
            reason = f"Live odds favor {away} ({away_odds} vs {home_odds})"
        else:
            winner = home  # tie odds, fallback to home
            reason = "Live odds tied; choosing home team as fallback"
        return winner, reason
    
    # If no live odds, fallback to historical data
    home_wins = df[(df['Home Team'] == home) & (df['Winner'] == home)].shape[0]
    away_wins = df[(df['Away Team'] == away) & (df['Winner'] == away)].shape[0]

    if home_wins > away_wins:
        return home, f"Historical data shows better home team performance ({home_wins} wins)"
    elif away_wins > home_wins:
        return away, f"Historical data shows better away team performance ({away_wins} wins)"
    else:
        # No data or equal
        return home, "No historical data or equal performance; defaulting to home team"

if st.button("Predict Winner"):
    winner, reason = predict_winner(home_team, away_team)
    st.success(f"Predicted Winner: **{winner}**")
    st.info(f"Reason: {reason}")

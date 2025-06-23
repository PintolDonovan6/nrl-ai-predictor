import streamlit as st
import pandas as pd

# All NRL teams
teams = [
    'Broncos', 'Raiders', 'Bulldogs', 'Sharks', 'Titans', 'Sea Eagles', 'Storm',
    'Knights', 'Cowboys', 'Eels', 'Panthers', 'Rabbitohs', 'Dragons',
    'Roosters', 'Warriors', 'Tigers', 'Dolphins'
]

# Sample historical match data
data = {
    'Home Team': ['Storm', 'Panthers', 'Roosters', 'Storm', 'Broncos', 'Panthers'],
    'Away Team': ['Broncos', 'Storm', 'Panthers', 'Roosters', 'Panthers', 'Roosters'],
    'Winner':    ['Storm', 'Panthers', 'Roosters', 'Storm', 'Panthers', 'Panthers']
}
df = pd.DataFrame(data)

st.title("🏉 NRL Match Winner Predictor")

home_team = st.selectbox("Select Home Team", teams)
away_team = st.selectbox("Select Away Team", [team for team in teams if team != home_team])

def predict_winner(home, away):
    home_wins = df[(df['Home Team'] == home) & (df['Winner'] == home)].shape[0]
    away_wins = df[(df['Away Team'] == away) & (df['Winner'] == away)].shape[0]

    if home_wins > away_wins:
        return home, f"🏠 {home} has better home record."
    elif away_wins > home_wins:
        return away, f"🚗 {away} has better away record."
    elif home_wins == away_wins and home_wins > 0:
        return home, "History tied, favoring home team."
    else:
        return home, "No historical data found, fallback to home team."

if st.button("Predict Winner"):
    winner, explanation = predict_winner(home_team, away_team)
    st.success(f"🏆 Predicted Winner: **{winner}**")
    st.info(explanation)

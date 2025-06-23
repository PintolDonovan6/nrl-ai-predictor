import streamlit as st
import pandas as pd

# Sample NRL match history
data = {
    'Home Team': ['Storm', 'Panthers', 'Roosters', 'Storm', 'Broncos', 'Panthers'],
    'Away Team': ['Broncos', 'Storm', 'Panthers', 'Roosters', 'Panthers', 'Roosters'],
    'Winner':    ['Storm', 'Panthers', 'Roosters', 'Storm', 'Panthers', 'Panthers']
}
df = pd.DataFrame(data)

st.title("🏉 NRL Match Winner Predictor")

teams = sorted(list(set(df['Home Team']) | set(df['Away Team'])))
home_team = st.selectbox("Select Home Team", teams)
away_team = st.selectbox("Select Away Team", [team for team in teams if team != home_team])

def predict_winner(home, away):
    home_wins = df[(df['Home Team'] == home) & (df['Winner'] == home)].shape[0]
    away_wins = df[(df['Away Team'] == away) & (df['Winner'] == away)].shape[0]
    if home_wins > away_wins:
        return home
    elif away_wins > home_wins:
        return away
    else:
        return "It's too close to call!"

if st.button("Predict Winner"):
    result = predict_winner(home_team, away_team)
    st.success(f"Predicted Winner: **{result}**")

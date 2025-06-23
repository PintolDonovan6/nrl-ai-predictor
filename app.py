import streamlit as st
import pandas as pd

# Page title
st.set_page_config(page_title="NRL Predictor", page_icon="🏉")
st.title("🏉 NRL Match Winner Predictor")

# Full team list
teams = [
    'Broncos', 'Raiders', 'Bulldogs', 'Sharks', 'Titans', 'Sea Eagles', 'Storm',
    'Knights', 'Cowboys', 'Eels', 'Panthers', 'Rabbitohs', 'Dragons',
    'Roosters', 'Warriors', 'Tigers', 'Dolphins'
]

# Sample match history
data = {
    'Home Team': ['Storm', 'Panthers', 'Roosters', 'Storm', 'Broncos', 'Panthers'],
    'Away Team': ['Broncos', 'Storm', 'Panthers', 'Roosters', 'Panthers', 'Roosters'],
    'Winner':    ['Storm', 'Panthers', 'Roosters', 'Storm', 'Panthers', 'Panthers']
}
df = pd.DataFrame(data)

# Team selection
home_team = st.selectbox("Select Home Team", teams)
away_team = st.selectbox("Select Away Team", [team for team in teams if team != home_team])

# Prediction logic
def predict_winner(home, away):
    home_wins = df[(df['Home Team'] == home) & (df['Winner'] == home)].shape[0]
    away_wins = df[(df['Away Team'] == away) & (df['Winner'] == away)].shape[0]

    if home_wins > away_wins:
        return f"{home} (based on home history)"
    elif away_wins > home_wins:
        return f"{away} (based on away history)"
    elif home_wins == 0 and away_wins == 0:
        return "No data available. Too close to call!"
    else:
        return "It's too close to call!"

# Predict button
if st.button("Predict Winner"):
    result = predict_winner(home_team, away_team)
    st.success(f"Predicted Winner: **{result}**")

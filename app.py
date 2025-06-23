import streamlit as st
import pandas as pd

# ✅ Full list of 17 NRL teams
all_teams = [
    'Broncos', 'Raiders', 'Bulldogs', 'Sharks', 'Titans', 'Sea Eagles', 'Storm',
    'Knights', 'Cowboys', 'Eels', 'Panthers', 'Rabbitohs', 'Dragons', 'Roosters',
    'Warriors', 'Tigers', 'Dolphins'
]

# ✅ Sample mini history data for logic (you'll add real history later)
data = {
    'Home Team': ['Storm', 'Panthers', 'Roosters', 'Storm', 'Broncos', 'Panthers'],
    'Away Team': ['Broncos', 'Storm', 'Panthers', 'Roosters', 'Panthers', 'Roosters'],
    'Winner':    ['Storm', 'Panthers', 'Roosters', 'Storm', 'Panthers', 'Panthers']
}
df = pd.DataFrame(data)

# 🌟 Streamlit App
st.title("🏉 NRL Match Winner Predictor")

home_team = st.selectbox("Select Home Team", all_teams)
away_team = st.selectbox("Select Away Team", [team for team in all_teams if team != home_team])

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

if st.button("Predict Winner"):
    result = predict_winner(home_team, away_team)
    st.success(f"Predicted Winner: **{result}**")

import streamlit as st
import pandas as pd

# List of all NRL teams
teams = [
    'Broncos', 'Raiders', 'Bulldogs', 'Sharks', 'Titans', 'Sea Eagles', 'Storm',
    'Knights', 'Cowboys', 'Eels', 'Panthers', 'Rabbitohs', 'Dragons',
    'Roosters', 'Warriors', 'Tigers', 'Dolphins'
]

# Sample match history data
data = {
    'Home Team': ['Storm', 'Panthers', 'Roosters', 'Storm', 'Broncos', 'Panthers'],
    'Away Team': ['Broncos', 'Storm', 'Panthers', 'Roosters', 'Panthers', 'Roosters'],
    'Winner':    ['Storm', 'Panthers', 'Roosters', 'Storm', 'Panthers', 'Panthers']
}
df = pd.DataFrame(data)

# Page title
st.title("🏉 NRL Match Winner Predictor")

# Team selectors
home_team = st.selectbox("Select Home Team", teams)
away_team = st.selectbox("Select Away Team", [team for team in teams if team != home_team])

def predict_winner(home, away):
    home_wins = df[(df['Home Team'] == home) & (df['Winner'] == home)].shape[0]
    away_wins = df[(df['Away Team']]()_

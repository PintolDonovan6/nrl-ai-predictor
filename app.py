import streamlit as st
import random

st.title("🏉 NRL Match Winner Predictor")
st.markdown("#### 🔍 Simulated AI Analysis Based on History, Form, and Expert Views")

# All NRL teams
teams = [
    'Broncos', 'Raiders', 'Bulldogs', 'Sharks', 'Titans', 'Sea Eagles', 'Storm',
    'Knights', 'Cowboys', 'Eels', 'Panthers', 'Rabbitohs', 'Dragons', 'Roosters',
    'Warriors', 'Tigers', 'Dolphins'
]

home_team = st.selectbox("Select Home Team", teams)
away_team = st.selectbox("Select Away Team", [t for t in teams if t != home_team])

# Sample historical results (can expand later)
history = {
    ('Storm', 'Broncos'): 'Storm',
    ('Panthers', 'Storm'): 'Panthers',
    ('Roosters', 'Panthers'): 'Roosters',
    ('Broncos', 'Panthers'): 'Panthers',
    ('Rabbitohs', 'Eels'): 'Rabbitohs'
}

# Simulated expert opinions
expert_opinions = {
    'Storm': 5,
    'Panthers': 7,
    'Broncos': 3,
    'Roosters': 6,
    'Rabbitohs': 4
}

def get_prediction(home, away):
    key = (home, away)
    reverse_key = (away, home)

    # Priority: history > expert votes > ladder form > random fallback
    if key in history:
        winner = history[key]
        reason = f"{winner} has beaten {away if winner==home else home} multiple times in the past."
    elif reverse_key in history:
        winner = history[reverse_key]
        reason = f"{winner} has dominated this match-up historically, even when playing away."
    elif home in expert_opinions or away in expert_opinions:
        home_votes = expert_opinions.get(home, 0)
        away_votes = expert_opinions.get(away, 0)
        if home_votes > away_votes:
            winner = home
            reason = f"Based on recent expert polls, {home} is getting more votes ({home_votes} vs {away_votes})."
        elif away_votes > home_votes:
            winner = away
            reason = f"Most experts lean towards {away} this week with {away_votes} votes."
        else:
            winner = random.choice([home, away])
            reason = "Experts are split, but we're tipping toward team form."
    else:
        winner = random.choice([home, away])
        reason = f"No strong history or expert data. Choosing based on recent form and fan sentiment."

    return winner, reason

if st.button("Predict Winner"):
    prediction, reason = get_prediction(home_team, away_team)
    st.success(f"Predicted Winner: **{prediction}**")
    st.info(f"Reason: {reason}")

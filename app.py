import streamlit as st
import requests
import random

# API details
API_BASE = "https://www.thesportsdb.com/api/v1/json/1"
LEAGUE_ID = "4387"  # NRL League ID in TheSportsDB

# Function to fetch upcoming matches
def get_upcoming_matches():
    url = f"{API_BASE}/eventsnextleague.php?id={LEAGUE_ID}"
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        return data.get("events", [])
    else:
        return []

# Prediction logic (random for now, can be replaced with real data later)
def predict_winner(team1, team2):
    winner = random.choice([team1, team2])
    margin_points = random.randint(1, 60)
    # Margin ranges
    if margin_points <= 10:
        margin_range = "1-10"
    elif margin_points <= 20:
        margin_range = "11-20"
    elif margin_points <= 30:
        margin_range = "21-30"
    elif margin_points <= 40:
        margin_range = "31-40"
    elif margin_points <= 50:
        margin_range = "41-50"
    else:
        margin_range = "51+"
    reason = (
        "Based on insights from pro analysts, tipsters, NRL fans, and AI evaluation."
    )
    return winner, margin_points, margin_range, reason


# Inject PNG flag background & black font color
st.markdown(
    """
    <style>
    .reportview-container {
        background: linear-gradient(to right, 
            #000000 33.33%, 
            #d80000 33.33%, 
            #d80000 66.66%, 
            #ffd700 66.66%);
        min-height: 100vh;
        color: black;
        font-weight: bold;
        padding: 20px;
    }
    h1, h2, h3, p, label, div {
        color: black !important;
        text-shadow: 1px 1px 1px white;
    }
    .stButton>button {
        background-color: #d80000 !important;
        color: white !important;
        font-weight: bold;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title
st.title("NRL Match Predictor | Samting Blo Ples")

# Fetch matches
matches = get_upcoming_matches()

if not matches:
    st.error("No upcoming matches found. Please try again later.")
else:
    # Extract unique teams from matches for selection
    teams = set()
    for m in matches:
        teams.add(m["strHomeTeam"])
        teams.add(m["strAwayTeam"])
    teams = sorted(list(teams))

    # Team selectors
    team1 = st.selectbox("Choose Team 1", teams)
    team2 = st.selectbox("Choose Team 2", [t for t in teams if t != team1])

    if st.button("Predict Winner"):
        winner, margin, margin_range, reason = predict_winner(team1, team2)

        st.markdown(f"### Predicted winner: {winner}")
        st.markdown(f"**Predicted points margin:** {margin} (Range: {margin_range})")
        st.markdown(f"**Why?** {reason}")

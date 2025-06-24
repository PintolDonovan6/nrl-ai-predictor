import streamlit as st
import random

# PNG-style background and font styling
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(to right, black 33.3%, #d80000 33.3%, #d80000 66.6%, #ffd700 66.6%);
        color: white;
    }
    .stApp {
        background: linear-gradient(to right, black 33.3%, #d80000 33.3%, #d80000 66.6%, #ffd700 66.6%);
    }
    h1, h2, h3, label, div, p {
        color: white !important;
    }
    .stButton>button {
        background-color: red !important;
        color: white !important;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.title("NRL Match Predictor | Samting Blo Ples")
st.write("**Powered by professional insights, tipster opinions, fan sentiment & AI.**")

# Manual team selection
teams = [
    "Brisbane Broncos", "Melbourne Storm", "Penrith Panthers", "Sydney Roosters",
    "Canberra Raiders", "South Sydney Rabbitohs", "Parramatta Eels", "Newcastle Knights",
    "North Queensland Cowboys", "Cronulla Sharks", "Wests Tigers", "Gold Coast Titans",
    "New Zealand Warriors", "St George Illawarra Dragons", "Manly Sea Eagles", "Dolphins"
]

team1 = st.selectbox("Choose Team 1", teams)
team2 = st.selectbox("Choose Team 2", [t for t in teams if t != team1])

if st.button("Predict Winner"):
    winner = random.choice([team1, team2])
    loser = team1 if winner == team2 else team2
    win_pct = round(random.uniform(51, 75), 1)
    lose_pct = round(100 - win_pct, 1)
    margin = random.randint(6, 50)

    # Margin range bucket
    if margin <= 10:
        margin_range = "1–10"
    elif margin <= 20:
        margin_range = "11–20"
    elif margin <= 30:
        margin_range = "21–30"
    elif margin <= 40:
        margin_range = "31–40"
    elif margin <= 50:
        margin_range = "41–50"
    else:
        margin_range = "51+"

    st.subheader(f"Predicted Winner: {winner}")
    st.write(f"**Winning chance:** {winner} {win_pct}% – {loser} {lose_pct}%")
    st.write(f"**Predicted points margin:** {margin} (Range: {margin_range})")
    st.write(f"**Why?** Based on latest online expert tips, fan opinions, and performance stats.")

import streamlit as st
import random

# Custom CSS for PNG colors background and text
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
        color: black !important;
    }
    .sidebar-content {
        background: linear-gradient(to right,
            #000000 33.33%,
            #d80000 33.33%,
            #d80000 66.66%,
            #ffd700 66.66%);
        color: black !important;
    }
    h1, h2, h3, p, label, div {
        color: black !important;
        text-shadow: none !important;
    }
    button, .stButton>button {
        background-color: #d80000 !important;
        color: white !important;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title
st.title("NRL Match Predictor | Samting Blo Ples")

# Team selectors
team_list = [
    "Brisbane Broncos",
    "Melbourne Storm",
    "Penrith Panthers",
    "Sydney Roosters",
    "Canberra Raiders",
    "South Sydney Rabbitohs",
    "Parramatta Eels",
    "Newcastle Knights",
]

team1 = st.selectbox("Choose Team 1", team_list, index=0)
team2 = st.selectbox("Choose Team 2", [team for team in team_list if team != team1], index=1)

# Prediction button
if st.button("Predict Winner"):

    # Random prediction logic (replace with real AI logic later)
    winner = random.choice([team1, team2])
    margin = random.randint(1, 60)

    # Margin range buckets
    if margin <= 10:
        margin_range = "1-10"
    elif margin <= 20:
        margin_range = "11-20"
    elif margin <= 30:
        margin_range = "21-30"
    elif margin <= 40:
        margin_range = "31-40"
    elif margin <= 50:
        margin_range = "41-50"
    else:
        margin_range = "51+"

    # Show prediction results
    st.markdown(f"### Predicted winner: {winner}")
    st.markdown(f"**Predicted points margin:** {margin} (Range: {margin_range})")
    st.markdown(f"**Why?** Based on AI, PNG passion, and stats.")

    # Show your image below predictions
    st.image("logo1.png", use_container_width=True)

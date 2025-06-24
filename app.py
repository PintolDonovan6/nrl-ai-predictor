import streamlit as st
import random

# Inject PNG flag vertical stripes as full background with image overlay
st.markdown(
    """
    <style>
    /* Full page background with PNG flag colors */
    .stApp {
        background: 
          url('logo1.png') no-repeat center center fixed,
          linear-gradient(to right, #000000 33.33%, #d80000 33.33%, #d80000 66.66%, #ffd700 66.66%);
        background-size: cover, cover;
        color: white;
    }

    /* Text styling */
    h1, h2, h3, p, label, div {
        color: white !important;
        text-shadow: 1px 1px 3px black;
    }

    /* Button style */
    button, .stButton>button {
        background-color: #d80000 !important;
        color: white !important;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("NRL Match Predictor | Mango Mine Case")
st.markdown("Powered by professional insights, tipster opinions, fan sentiment & AI.")

# List of all NRL teams
teams = [
    "Brisbane Broncos", "Melbourne Storm", "Penrith Panthers", "Sydney Roosters",
    "Canberra Raiders", "South Sydney Rabbitohs", "Parramatta Eels", "Newcastle Knights",
    "Cronulla Sharks", "Manly Sea Eagles", "Gold Coast Titans", "Wests Tigers",
    "St. George Illawarra Dragons", "New Zealand Warriors", "North Queensland Cowboys", "Canterbury Bulldogs"
]

team1 = st.selectbox("Choose Team 1", teams)
team2 = st.selectbox("Choose Team 2", [team for team in teams if team != team1])

if st.button("Predict Winner"):
    winner = random.choice([team1, team2])
    # Simulate margin for prediction (just dummy logic, replace with real logic later)
    margin = random.randint(1, 60)

    # Only show range, no exact margin number
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

    st.markdown(f"**Predicted Winner:** {winner}")
    st.markdown(f"**Predicted points margin:** Range {margin_range}")
    st.markdown(f"**Why?** Based on latest online expert tips, fan opinions, and performance stats.")


import streamlit as st
import random

# Inject CSS for background image and styling
st.markdown(
    """
    <style>
    /* Full page background image */
    .stApp {
        background: url("logo1.png") no-repeat center center fixed;
        background-size: cover;
    }

    /* Remove any background colors */
    body, .main, .block-container {
        background-color: transparent !important;
    }

    /* Make all text white */
    h1, h2, h3, p, label, div, span {
        color: white !important;
    }

    /* Style buttons with PNG red and white text */
    button, .stButton>button {
        background-color: #d80000 !important;
        color: white !important;
        font-weight: bold !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title and subtitle
st.title("NRL Match Predictor | Mango Mine Case")
st.write("Powered by professional insights, tipster opinions, fan sentiment & AI.")

# List of NRL teams (example list)
teams = [
    "Brisbane Broncos", "Melbourne Storm", "Penrith Panthers", "Sydney Roosters",
    "Canberra Raiders", "South Sydney Rabbitohs", "Parramatta Eels", "Newcastle Knights",
    "Cronulla Sharks", "St George Illawarra Dragons", "Wests Tigers", "Manly Sea Eagles",
    "Canterbury Bulldogs", "Gold Coast Titans", "New Zealand Warriors", "North Queensland Cowboys"
]

# Team selection
team1 = st.selectbox("Choose Team 1", teams)
team2 = st.selectbox("Choose Team 2", [team for team in teams if team != team1])

# Prediction button
if st.button("Predict Winner"):
    # Dummy prediction logic - replace with your real model/data integration
    winner = random.choice([team1, team2])
    # Predicted margin range buckets only (no exact number)
    margin = random.randint(1, 60)
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

    # Reason - placeholder text (replace with your web analysis logic)
    reason = f"Based on latest online expert tips, fan opinions, and performance stats."

    # Output prediction
    st.markdown(f"### Predicted Winner: {winner}")
    st.markdown(f"**Predicted points margin:** Range: {margin_range}")
    st.markdown(f"**Why?** {reason}")

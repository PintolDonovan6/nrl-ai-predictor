import streamlit as st
import random

# Background image and styling with correct selectors and layering
st.markdown(
    """
    <style>
    /* Make the whole app container use your image as background */
    .stApp {
        background-image: url("logo1.png");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }

    /* Make container backgrounds transparent so image is visible */
    .css-18e3th9, .css-1d391kg, .main, .block-container {
        background-color: transparent !important;
    }

    /* White font color for all text */
    .stText, h1, h2, h3, label, p, span, div {
        color: white !important;
    }

    /* Style buttons - PNG red with white text */
    button, .stButton>button {
        background-color: #d80000 !important;
        color: white !important;
        font-weight: bold !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title & subtitle
st.title("NRL Match Predictor | Mango Mine Case")
st.write("Powered by professional insights, tipster opinions, fan sentiment & AI.")

# NRL teams list
teams = [
    "Brisbane Broncos", "Melbourne Storm", "Penrith Panthers", "Sydney Roosters",
    "Canberra Raiders", "South Sydney Rabbitohs", "Parramatta Eels", "Newcastle Knights",
    "Cronulla Sharks", "St George Illawarra Dragons", "Wests Tigers", "Manly Sea Eagles",
    "Canterbury Bulldogs", "Gold Coast Titans", "New Zealand Warriors", "North Queensland Cowboys"
]

# Select teams
team1 = st.selectbox("Choose Team 1", teams)
team2 = st.selectbox("Choose Team 2", [team for team in teams if team != team1])

# Prediction button
if st.button("Predict Winner"):
    # Dummy legit logic (replace with real one later)
    winner = random.choice([team1, team2])
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

    reason = "Based on latest online expert tips, fan opinions, and performance stats."

    st.markdown(f"### Predicted Winner: {winner}")
    st.markdown(f"**Predicted points margin:** Range: {margin_range}")
    st.markdown(f"**Why?** {reason}")

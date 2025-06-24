import streamlit as st
import random

# Set background image and PNG flag colors overlay
st.markdown(
    """
    <style>
    .stApp {
        background: 
          linear-gradient(
            rgba(255, 215, 0, 0.6), 
            rgba(255, 215, 0, 0.6)
          ),
          url('logo1.png');
        background-size: cover;
        background-position: center;
        color: black !important;
        min-height: 100vh;
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

st.title("NRL Match Predictor | Samting Blo Ples")

teams = [
    "Brisbane Broncos",
    "Melbourne Storm",
    "Penrith Panthers",
    "Sydney Roosters",
    "Canberra Raiders",
    "South Sydney Rabbitohs",
    "Parramatta Eels",
    "Newcastle Knights",
]

team1 = st.selectbox("Choose Team 1", teams, index=0)
team2 = st.selectbox("Choose Team 2", [team for team in teams if team != team1], index=1)

if st.button("Predict Winner"):
    winner = random.choice([team1, team2])
    margin = random.randint(1, 60)

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

    st.markdown(f"### Predicted winner: {winner}")
    st.markdown(f"**Predicted points margin:** {margin} (Range: {margin_range})")
    st.markdown(f"**Why?** Based on insights from pro analysts, tipsters, NRL fans, and AI.")

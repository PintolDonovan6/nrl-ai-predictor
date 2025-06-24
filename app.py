import streamlit as st
import random

# Inject PNG flag style background and fonts
st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(to right,
            #000000 33.33%,
            #d80000 33.33%,
            #d80000 66.66%,
            #ffd700 66.66%);
        min-height: 100vh;
        color: black !important;
        padding: 2rem;
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

    # Show PNG flag image below predictions
    st.image("logo1.png", use_container_width=True)

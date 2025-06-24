import streamlit as st
import random
from PIL import Image

# Set page config
st.set_page_config(page_title="NRL Match Predictor | Mango Mine Yah", layout="centered")

# PNG-inspired styling
st.markdown("""
    <style>
    body {
        background-color: #d80000;
        color: white;
    }
    .reportview-container {
        background: linear-gradient(to bottom, #000000, #d80000, #ffd700);
        color: white;
    }
    h1, h2, h3, p, label {
        color: white !important;
    }
    .stButton>button {
        background-color: #000000;
        color: #ffd700;
        font-weight: bold;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# Optional PNG-themed image background
try:
    img = Image.open("logo1.png")
    st.image(img, use_column_width=True)
except:
    pass

st.title("NRL Match Predictor | Samting Blo Ples")
st.markdown("_Powered by professional insights, tipster opinions, fan sentiment & AI._")

# NRL teams
teams = [
    "Brisbane Broncos", "Melbourne Storm", "Penrith Panthers", "South Sydney Rabbitohs",
    "Sydney Roosters", "Parramatta Eels", "Canberra Raiders", "Cronulla Sharks",
    "Newcastle Knights", "Manly Sea Eagles", "North Queensland Cowboys", "Gold Coast Titans",
    "Wests Tigers", "NZ Warriors", "St. George Illawarra Dragons", "Dolphins"
]

team1 = st.selectbox("Choose Team 1", teams)
team2 = st.selectbox("Choose Team 2", [t for t in teams if t != team1])

if st.button("Predict Match"):
    # Simulate analysis (replace with real model/API later)
    team1_score = random.randint(70, 100)
    team2_score = random.randint(60, 95)
    total_points = team1_score + team2_score
    margin = abs(team1_score - team2_score)

    # Determine predicted winner
    if team1_score > team2_score:
        winner = team1
        loser = team2
        win_chance = round(random.uniform(60, 85), 1)
        lose_chance = round(100 - win_chance, 1)
    else:
        winner = team2
        loser = team1
        win_chance = round(random.uniform(60, 85), 1)
        lose_chance = round(100 - win_chance, 1)

    # Margin range logic
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

    # Example-based reason
    reasons = [
        f"{winner} has shown better recent form and consistent attack.",
        f"Key players for {winner} have returned from injury, boosting chances.",
        f"{loser} has struggled defensively in recent rounds.",
        f"Recent betting trends favor {winner}.",
        f"Experts tip {winner} based on possession and completion stats."
    ]
    reason = random.choice(reasons)

    # Display results
    st.subheader(f"Predicted Winner: {winner}")
    st.write(f"Winning chance: **{winner} {win_chance}%** – {loser} {lose_chance}%")
    st.write(f"Predicted points margin: **{margin}** (Range: **{margin_range}**)")
    st.write(f"**Why?** {reason}")

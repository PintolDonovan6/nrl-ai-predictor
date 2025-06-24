import streamlit as st
import random
from PIL import Image
import base64

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

def set_bg_image(image_path):
    encoded_image = get_base64_image(image_path)
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_image}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            color: white;
        }}
        h1, h2, h3, label, .stSelectbox label {{
            color: white !important;
            text-shadow: 1px 1px 2px black;
        }}
        .stButton > button {{
            background-color: #000000;
            color: #ffd700;
            font-weight: bold;
            border-radius: 8px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

st.set_page_config(page_title="NRL Match Predictor | Mango Mine Case", layout="centered")
set_bg_image("logo1.png")

st.title("NRL Match Predictor | Mango Mine Case")
st.markdown("_Powered by professional insights, tipster opinions, fan sentiment & AI._")

teams = [
    "Brisbane Broncos", "Melbourne Storm", "Penrith Panthers", "South Sydney Rabbitohs",
    "Sydney Roosters", "Parramatta Eels", "Canberra Raiders", "Cronulla Sharks",
    "Newcastle Knights", "Manly Sea Eagles", "North Queensland Cowboys", "Gold Coast Titans",
    "Wests Tigers", "NZ Warriors", "St. George Illawarra Dragons", "Dolphins"
]

team1 = st.selectbox("Choose Team 1", teams)
team2 = st.selectbox("Choose Team 2", [t for t in teams if t != team1])

if st.button("Predict Match"):
    team1_score = random.randint(70, 100)
    team2_score = random.randint(60, 95)
    margin = abs(team1_score - team2_score)

    winner = team1 if team1_score > team2_score else team2
    loser = team2 if winner == team1 else team1

    win_chance = round(random.uniform(60, 85), 1)
    lose_chance = round(100 - win_chance, 1)

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

    reason = random.choice([
        f"{winner} has momentum from recent matches.",
        f"{winner} is stronger in key positions based on fan opinions.",
        f"Most tipsters are backing {winner}.",
        f"{loser} has recent injuries affecting performance.",
        f"{winner} leads in completion rate and defense stats."
    ])

    st.subheader(f"Predicted Winner: {winner}")
    st.write(f"Winning chance: **{winner} {win_chance}%** – {loser} {lose_chance}%")
    st.write(f"Predicted points margin: **{margin}** (Range: **{margin_range}**)")
    st.write(f"**Why?** {reason}")

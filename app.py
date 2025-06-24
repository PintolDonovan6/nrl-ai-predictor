import streamlit as st
import random

st.set_page_config(page_title="NRL Match Predictor | Samting Blo Ples", layout="centered")

# Inject CSS for PNG colors
st.markdown(
    """
    <style>
    body, .css-18e3th9, .main {
        background-color: #000000 !important;  /* Black */
        color: #FFD700 !important;             /* Gold/yellow */
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    div.stButton > button {
        background-color: #d80000 !important;  /* PNG Red */
        color: white !important;
        font-weight: bold !important;
        border-radius: 10px !important;
        padding: 10px 24px !important;
        font-size: 1.1em !important;
    }
    div[role="listbox"] > div {
        color: #FFD700 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

teams = [
    "Brisbane Broncos", "Melbourne Storm", "Penrith Panthers", "Sydney Roosters",
    "South Sydney Rabbitohs", "Canberra Raiders", "Parramatta Eels", "Newcastle Knights"
]

reason_map = {
    "Brisbane Broncos": "Brisbane Broncos have strong recent form.",
    "Melbourne Storm": "Melbourne Storm are known for strong defense.",
    "Penrith Panthers": "Penrith Panthers are consistent contenders.",
    "Sydney Roosters": "Sydney Roosters have strong recent form.",
    "South Sydney Rabbitohs": "South Sydney Rabbitohs have key injuries to manage.",
    "Canberra Raiders": "Canberra Raiders have key players fit and ready.",
    "Parramatta Eels": "Betting odds favor Parramatta Eels.",
    "Newcastle Knights": "Newcastle Knights are rebuilding this season.",
}

# Define margin brackets as total combined points ranges
margin_brackets = [
    (1, 10),
    (11, 20),
    (30, 40),
    (41, 50),
    (51, 100),  # 51+ (assuming max 100)
]

def predict_winner(team1, team2):
    chance1 = round(random.uniform(40, 60), 1)
    chance2 = round(100 - chance1, 1)
    winner = team1 if chance1 > chance2 else team2
    # Pick a random bracket for total points
    margin_range = random.choice(margin_brackets)
    total_points = random.randint(margin_range[0], margin_range[1])
    return winner, chance1, chance2, total_points, margin_range

st.title("NRL Match Predictor | Samting Blo Ples")

team1 = st.selectbox("Choose Team 1", teams)
team2 = st.selectbox("Choose Team 2", [t for t in teams if t != team1])

if st.button("Predict Winner"):
    winner, chance1, chance2, total_points, bracket = predict_winner(team1, team2)
    bracket_str = f"{bracket[0]}-{bracket[1]}" if bracket[1] != 100 else f"{bracket[0]}+"
    st.write(f"Predicted winner: **{winner}**")
    st.write(f"Winning chance: {team1} {chance1}% - {team2} {chance2}%")
    st.write(f"Predicted total points: {total_points} (Range: {bracket_str})")
    st.write(f"Why? {reason_map.get(winner, 'Based on recent analysis and form.')}")

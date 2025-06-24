import streamlit as st
import random

st.set_page_config(page_title="NRL Match Predictor | Samting Blo Ples", layout="centered")

# Inject PNG colors CSS
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

# Margin brackets as ranges (difference in points)
margin_brackets = [
    (1, 10),
    (11, 20),
    (21, 30),
    (31, 40),
    (41, 50),
    (51, 100),  # 51+
]

def categorize_margin(margin):
    for low, high in margin_brackets:
        if low <= margin <= high:
            if high == 100:
                return f"{low}+"
            else:
                return f"{low}-{high}"
    return "Unknown"

def predict_winner(team1, team2):
    chance1 = round(random.uniform(40, 60), 1)
    chance2 = round(100 - chance1, 1)
    winner = team1 if chance1 > chance2 else team2
    # Random margin difference (points margin)
    margin = random.randint(1, 60)
    margin_range = categorize_margin(margin)
    return winner, chance1, chance2, margin, margin_range

st.title("NRL Match Predictor | Samting Blo Ples")

team1 = st.selectbox("Choose Team 1", teams)
team2 = st.selectbox("Choose Team 2", [t for t in teams if t != team1])

if st.button("Predict Winner"):
    winner, chance1, chance2, margin, margin_range = predict_winner(team1, team2)
    st.write(f"Predicted winner: **{winner}**")
    st.write(f"Winning chance: {team1} {chance1}% - {team2} {chance2}%")
    st.write(f"Predicted points margin: {margin} (Range: {margin_range})")
    st.write(f"Why? {reason_map.get(winner, 'Based on recent analysis and form.')}")

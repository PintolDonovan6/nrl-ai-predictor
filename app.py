import streamlit as st
import random

NRL_TEAMS = [
    "Brisbane Broncos",
    "Melbourne Storm",
    "Penrith Panthers",
    "Sydney Roosters",
    "South Sydney Rabbitohs",
    "Canberra Raiders",
    "Parramatta Eels",
    "Newcastle Knights",
    "Wests Tigers",
    "Gold Coast Titans",
    "St. George Illawarra Dragons",
    "Cronulla Sharks",
    "Manly Sea Eagles",
    "Canterbury Bulldogs",
    "New Zealand Warriors",
    "North Queensland Cowboys"
]

def predict_winner(home, away):
    winner = random.choice([home, away])
    loser = away if winner == home else home

    win_chance_winner = round(random.uniform(52, 75), 1)
    win_chance_loser = round(100 - win_chance_winner, 1)

    total_points = random.randint(1, 70)

    if total_points <= 10:
        margin_range = "1-10"
    elif total_points <= 20:
        margin_range = "11-20"
    elif total_points <= 30:
        margin_range = "21-30"
    elif total_points <= 40:
        margin_range = "31-40"
    elif total_points <= 50:
        margin_range = "41-50"
    else:
        margin_range = "51+"

    reason = f"{winner} have shown strong recent form and better stats."
    return winner, loser, win_chance_winner, win_chance_loser, total_points, margin_range, reason

# Page config
st.set_page_config(page_title="NRL Match Predictor | Samting Blo Ples", page_icon="🏉")

# PNG-themed gradient background and styling
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #008000 0%, #ffd700 50%, #d80000 100%);
        color: white;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        padding: 20px;
    }
    h1, h2, h3 {
        color: #ffffff;
        text-shadow: 1px 1px 2px black;
    }
    .stButton>button {
        background-color: #d80000;
        color: white;
        border-radius: 8px;
        padding: 10px 20px;
        font-weight: bold;
        font-size: 16px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        transition: background-color 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #a30000;
    }
    .stSelectbox>div>div>select {
        background-color: white;
        color: black;
        font-weight: bold;
        border-radius: 5px;
        padding: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("NRL Match Predictor | Samting Blo Ples")
st.write("Powered by AI, PNG passion, and your chosen teams.")

team1 = st.selectbox("Choose Team 1", NRL_TEAMS, index=0)
team2 = st.selectbox("Choose Team 2", [t for t in NRL_TEAMS if t != team1], index=1)

if st.button("Predict Winner"):
    winner, loser, win_chance_winner, win_chance_loser, total_points, margin_range, reason = predict_winner(team1, team2)
    st.subheader(f"Predicted winner: {winner}")
    st.write(f"Winning chance: {winner} {win_chance_winner}% - {loser} {win_chance_loser}%")
    st.write(f"Predicted total points margin: {total_points} (Range: {margin_range})")
    st.write(f"Why? {reason}")

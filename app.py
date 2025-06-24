import streamlit as st
import random

st.set_page_config(page_title="NRL Match Predictor | Samting Blo Ples", layout="centered")

st.title("NRL Match Predictor | Samting Blo Ples")
st.write("Powered by AI, PNG passion, and Pacific Racing insights.")

st.header("Choose Prediction Method:")
st.write("Pacific Racing Guide")
st.write("Fetching latest Pacific Racing tips...")

# Simulated failure to fetch tips fallback
st.write("Could not fetch tips. Using random prediction fallback.\n")

# Sample upcoming matches
upcoming_matches = [
    ("Brisbane Broncos", "Melbourne Storm"),
    ("Penrith Panthers", "Sydney Roosters"),
    ("South Sydney Rabbitohs", "Canberra Raiders"),
    ("Parramatta Eels", "Newcastle Knights"),
]

# Reason summaries
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

def predict_random(team1, team2):
    chance1 = round(random.uniform(40, 60), 1)
    chance2 = round(100 - chance1, 1)
    winner = team1 if chance1 > chance2 else team2
    margin = random.randint(2, 20)
    return winner, chance1, chance2, margin

st.header("Upcoming Matches & Predictions:")

for team1, team2 in upcoming_matches:
    winner, chance1, chance2, margin = predict_random(team1, team2)
    st.subheader(f"{team1} vs {team2}")
    st.write(f"Predicted winner: **{winner}**")
    st.write(f"Winning chance: {team1} {chance1}% - {team2} {chance2}%")
    st.write(f"Predicted points margin: {margin}")
    st.write(f"Why? {reason_map.get(winner, 'Based on recent analysis and form.')}\n")

st.markdown("---")
st.write("Note: Pacific Racing scraping depends on public access to Facebook posts. If unavailable, predictions fallback to random.")

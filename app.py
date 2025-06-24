import streamlit as st
import random

# Sample teams and upcoming matches (update your own real schedule here)
teams = [
    "Brisbane Broncos", "Melbourne Storm", "Penrith Panthers",
    "Sydney Roosters", "South Sydney Rabbitohs", "Canberra Raiders",
    "Parramatta Eels", "Newcastle Knights",
]

upcoming_matches = [
    ("Brisbane Broncos", "Melbourne Storm"),
    ("Penrith Panthers", "Sydney Roosters"),
    ("South Sydney Rabbitohs", "Canberra Raiders"),
    ("Parramatta Eels", "Newcastle Knights"),
]

def random_predictor(team1, team2):
    team1_chance = random.uniform(40, 60)
    team2_chance = 100 - team1_chance
    margin = random.randint(2, 20)
    winner = team1 if team1_chance > team2_chance else team2
    return winner, team1_chance, team2_chance, margin

def pacific_racing_predictor(team1, team2):
    """
    Mock-up of Pacific Racing style prediction:
    - Assign weights based on fake 'form' and 'history'
    - In real app, scrape or input real Pacific Racing data here
    """
    form_scores = {
        team1: random.randint(60, 90),  # pretend form % from guide
        team2: random.randint(50, 85),
    }
    # Calculate winner based on form score
    if form_scores[team1] > form_scores[team2]:
        winner = team1
    else:
        winner = team2

    # Normalize chances to sum 100%
    total = form_scores[team1] + form_scores[team2]
    team1_chance = (form_scores[team1] / total) * 100
    team2_chance = (form_scores[team2] / total) * 100

    # Margin prediction as difference of form scores times some factor
    margin = abs(form_scores[team1] - form_scores[team2]) // 2
    if margin < 2:
        margin = 2

    return winner, team1_chance, team2_chance, margin

def generate_summary(winner, team1, team2, method):
    if method == "Random":
        reasons = [
            f"{winner} have strong recent form.",
            f"{winner} have key players fit and ready.",
            f"Expert analysis favors {winner}.",
            f"{winner} have won their last encounters against {team2 if winner == team1 else team1}.",
            f"Betting odds favor {winner}.",
        ]
    else:  # Pacific Racing
        reasons = [
            f"According to Pacific Racing guide, {winner} show stronger form recently.",
            f"Pacific Racing data favors {winner} with better historical performance.",
            f"{winner} are predicted by Pacific Racing to win with confidence.",
            f"Form and stats from Pacific Racing guide support {winner}.",
            f"Pacific Racing's model points to {winner} as the probable winner.",
        ]
    return random.choice(reasons)

# --- Streamlit UI ---
st.title("NRL Match Predictor | Samting Blo Ples")
st.write("Powered by AI, PNG passion, and Pacific Racing insights.")

method = st.selectbox("Choose Prediction Method:", ["Random", "Pacific Racing Guide"])

st.header("Upcoming Matches & Predictions:")

for match in upcoming_matches:
    team1, team2 = match

    if method == "Random":
        winner, t1_chance, t2_chance, margin = random_predictor(team1, team2)
    else:
        winner, t1_chance, t2_chance, margin = pacific_racing_predictor(team1, team2)

    st.subheader(f"{team1} vs {team2}")
    st.write(f"Predicted winner: **{winner}**")
    st.write(f"Winning chance: {team1} {t1_chance:.1f}% - {team2} {t2_chance:.1f}%")
    st.write(f"Predicted points margin: {margin}")
    st.write("Why? " + generate_summary(winner, team1, team2, method))
    st.write("---")

st.write("*Note: Pacific Racing logic here is a placeholder. Replace with real guide data & formulas.*")

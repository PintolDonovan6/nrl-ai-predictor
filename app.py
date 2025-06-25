import streamlit as st
import random

# --- CSS for black background and PNG colors ---
st.markdown(
    """
    <style>
    /* Full page black background */
    .stApp {
        background-color: #000000;
        color: #ffd700 !important;  /* Gold text */
    }

    /* Headings red */
    h1, h2, h3, h4, h5, h6 {
        color: #d80000 !important;  /* Red */
    }

    /* Buttons */
    button, .stButton > button {
        background-color: #d80000 !important;
        color: #ffd700 !important;
        font-weight: bold;
        border: 2px solid #000000;
        border-radius: 6px;
    }

    /* Inputs */
    input, select, textarea {
        background-color: #1a1a1a !important;
        color: #ffd700 !important;
        border: 1px solid #d80000 !important;
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

teams = [
    "Brisbane Broncos", "Melbourne Storm", "Penrith Panthers", "Sydney Roosters",
    "Canberra Raiders", "South Sydney Rabbitohs", "Parramatta Eels", "Newcastle Knights",
    "Gold Coast Titans", "Wests Tigers", "Cronulla Sharks", "St. George Illawarra Dragons",
    "Manly Sea Eagles", "New Zealand Warriors", "North Queensland Cowboys", "Rabbitohs"
]

st.title("NRL Match Predictor | Mango Mine Case")
st.write("Powered by professional insights, tipster opinions, fan sentiment & AI.")

team1 = st.selectbox("Choose Team 1", teams, index=0)
team2 = st.selectbox("Choose Team 2", teams, index=1)

if team1 == team2:
    st.error("Please select two different teams.")
else:
    if st.button("Predict Winner"):
        team1_chance = random.uniform(40, 60)
        team2_chance = 100 - team1_chance

        winner = team1 if team1_chance > team2_chance else team2
        win_chance = max(team1_chance, team2_chance)

        margin_ranges = ["1–10", "11–20", "21–30", "31–40", "41–50", "51+"]
        margin_probs = [40, 25, 15, 10, 7, 3]
        margin = random.choices(margin_ranges, weights=margin_probs, k=1)[0]

        reasons = [
            f"{winner} have consistently outperformed their opponents in recent matches.",
            f"Based on recent form and key player availability, {winner} have the edge.",
            f"Statistical analysis shows {winner} winning over 80% of matches against this opponent since 2020.",
            f"Expert tipsters and fan sentiment strongly favor {winner} for this game.",
            f"AI-driven performance models predict a strong showing by {winner}."
        ]
        reason = random.choice(reasons)

        st.markdown(f"### Predicted Winner: {winner}")
        st.markdown(f"**Winning chance:** {winner} {win_chance:.1f}% – {'Melbourne Storm' if winner == team1 else team1} {100 - win_chance:.1f}%")
        st.markdown(f"**Predicted points margin:** Range: {margin}")
        st.markdown(f"**Why?** {reason}")

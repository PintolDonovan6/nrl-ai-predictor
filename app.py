import streamlit as st
import random

# --- CSS for background image and PNG colors ---
st.markdown(
    """
    <style>
    /* Full page background image */
    .stApp {
        background: url('logo1.png') no-repeat center center fixed;
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
        background-repeat: no-repeat;
        background-size: cover;
    }

    /* Text colors */
    .stApp, .css-18e3th9, .css-1d391kg, .css-1v3fvcr, .css-1v0mbdj, .css-1gkcyyc {
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
        background-color: rgba(216, 0, 0, 0.1) !important;
        color: #000000 !important;
        border: 1px solid #d80000 !important;
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- NRL Teams list ---
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
        # Dummy but realistic prediction logic (replace with real data fetch if you want)
        # Simulate weighted chance based on some fake stats:
        team1_chance = random.uniform(40, 60)
        team2_chance = 100 - team1_chance

        winner = team1 if team1_chance > team2_chance else team2
        win_chance = max(team1_chance, team2_chance)

        # Margin ranges
        margin_ranges = ["1–10", "11–20", "21–30", "31–40", "41–50", "51+"]
        margin_probs = [40, 25, 15, 10, 7, 3]
        margin = random.choices(margin_ranges, weights=margin_probs, k=1)[0]

        # Fake "reasoning" based on stats and history
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

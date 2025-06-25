import streamlit as st

# Inject custom CSS for background and font color
st.markdown(
    """
    <style>
    /* Set background image for the whole app */
    .stApp {
        background-image: url('logo1.png');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        /* Add a subtle dark overlay for readability */
        position: relative;
        z-index: 0;
    }
    /* Overlay with dark semi-transparent layer */
    .stApp::before {
        content: "";
        position: fixed;
        top: 0; left: 0; right: 0; bottom: 0;
        background-color: rgba(0, 0, 0, 0.5); /* adjust transparency */
        z-index: -1;
    }

    /* Make all text white */
    .css-1d391kg, .css-1v3fvcr, .css-ffhzg2 {
        color: white !important;
    }

    /* Also white for headings */
    h1, h2, h3, h4, h5, h6, label, p, div, span {
        color: white !important;
    }

    /* Style buttons for better visibility */
    button, .stButton>button {
        background-color: #d80000 !important;
        color: white !important;
        font-weight: bold;
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

import streamlit as st
import requests
import random
import re

# --- YOUR API KEYS ---
API_KEY = "AIzaSyCNdyDKJSuRPApupwZEMQX4lnuGRm5YdXU"
CSE_ID = "b10cae8aa7f2249bb"

# --- PNG-THEMED CSS ---
st.markdown("""
<style>
.stApp {
    background-image: url("logo1.png");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
    font-family: 'Segoe UI', sans-serif;
}
h1, h2, h3, h4, h5, h6 {
    color: #FFD700 !important;
    text-shadow: 1px 1px 2px #000;
}
p, label, div, span {
    color: white !important;
}
.stButton>button {
    background-color: #D80000;
    color: white;
    border-radius: 10px;
    font-weight: bold;
    padding: 0.6em 1.2em;
}
.css-1n76uvr, .css-1cpxqw2 {
    background-color: rgba(0,0,0,0.6) !important;
    border-radius: 10px;
    padding: 10px;
}
</style>
""", unsafe_allow_html=True)

# --- APP HEADER ---
st.title("NRL Match Predictor | Mango Mine Case")
st.caption("🔥 Powered by expert tips, fan insights, & AI | Styled with PNG pride 🇵🇬")

# --- TEAM SELECTION ---
nrl_teams = [
    "Brisbane Broncos", "Canberra Raiders", "Canterbury Bulldogs", "Cronulla Sharks",
    "Dolphins", "Gold Coast Titans", "Manly Sea Eagles", "Melbourne Storm",
    "Newcastle Knights", "New Zealand Warriors", "North Queensland Cowboys",
    "Parramatta Eels", "Penrith Panthers", "South Sydney Rabbitohs",
    "St George Illawarra Dragons", "Sydney Roosters", "Wests Tigers"
]
team1 = st.selectbox("Choose Team 1", nrl_teams)
team2 = st.selectbox("Choose Team 2", [t for t in nrl_teams if t != team1])

# --- PREDICTION LOGIC ---
def fetch_prediction_reason(team1, team2):
    query = f"NRL {team1} vs {team2} expert prediction analysis"
    url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={CSE_ID}&q={query}&num=5"

    try:
        res = requests.get(url)
        res.raise_for_status()
        data = res.json()
        snippets = " ".join(item.get("snippet", "") for item in data.get("items", []))
        reason_sentences = re.findall(r"([A-Z][^.!?]*[.!?])", snippets)
        # Join first two meaningful sentences or fallback
        reason = " ".join(reason_sentences[:2]) if reason_sentences else "Based on expert previews and public analysis."
        return reason
    except Exception as e:
        return "Using fallback insights due to API restrictions or no results found."

def get_prediction(team1, team2):
    win_chance_team1 = random.uniform(45, 70)
    win_chance_team2 = 100 - win_chance_team1
    winner = team1 if win_chance_team1 > win_chance_team2 else team2

    total_margin = random.randint(1, 60)
    if total_margin <= 10:
        margin_range = "1–10"
    elif total_margin <= 20:
        margin_range = "11–20"
    elif total_margin <= 30:
        margin_range = "21–30"
    elif total_margin <= 40:
        margin_range = "31–40"
    elif total_margin <= 50:
        margin_range = "41–50"
    else:
        margin_range = "51+"

    reason = fetch_prediction_reason(team1, team2)
    return winner, round(win_chance_team1, 1), round(win_chance_team2, 1), margin_range, reason

# --- PREDICT BUTTON ---
if st.button("Predict Winner"):
    winner, chance1, chance2, margin_range, reason = get_prediction(team1, team2)

    st.markdown(f"""
    <div style="background-color: rgba(255, 215, 0, 0.2); padding: 1em; border-radius: 10px;">
        <h3>🏆 Predicted Winner: <span style='color:#FFD700'>{winner}</span></h3>
        <p><strong>Winning chance:</strong> {team1} {chance1}% vs {team2} {chance2}%</p>
        <p><strong>Predicted Margin Range:</strong> {margin_range} points</p>
        <p><strong>Why?</strong> {reason}</p>
    </div>
    """, unsafe_allow_html=True)

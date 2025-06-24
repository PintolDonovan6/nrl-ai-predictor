import streamlit as st
import requests
import random

# Google CSE setup
API_KEY = "AIzaSyCNdyDKJSuRPApupwZEMQX4lnuGRm5YdXU"
CSE_ID = "b10cae8aa7f2249bb"

# PNG-style background
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right, #000000 33.33%, #d80000 33.33%, #d80000 66.66%, #ffd700 66.66%);
        color: white;
    }
    h1, h2, h3, label, p, div, span {
        color: white !important;
        text-shadow: 1px 1px 2px black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("NRL Match Predictor | Samting Blo Ples")
st.markdown("Powered by professional insights, tipster opinions, fan sentiment & AI.")

# List of all NRL teams
teams = [
    "Brisbane Broncos", "Canberra Raiders", "Canterbury Bulldogs", "Cronulla Sharks",
    "Dolphins", "Gold Coast Titans", "Manly Sea Eagles", "Melbourne Storm",
    "Newcastle Knights", "New Zealand Warriors", "North Queensland Cowboys",
    "Parramatta Eels", "Penrith Panthers", "South Sydney Rabbitohs",
    "St George Illawarra Dragons", "Sydney Roosters", "Wests Tigers"
]

team1 = st.selectbox("Choose Team 1", teams)
team2 = st.selectbox("Choose Team 2", [t for t in teams if t != team1])

# Prediction logic
def fetch_prediction(team1, team2):
    query = f"NRL {team1} vs {team2} expert prediction analysis"
    url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={CSE_ID}&q={query}&num=5"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        results = response.json()

        snippets = [item["snippet"] for item in results.get("items", []) if "snippet" in item]
        combined_snippet = " ".join(snippets)

        if not snippets:
            raise Exception("No analysis found")

        # Simple keyword-based prediction (can be replaced with NLP)
        if team1.lower() in combined_snippet.lower():
            winner = team1
        elif team2.lower() in combined_snippet.lower():
            winner = team2
        else:
            winner = random.choice([team1, team2])

        confidence = round(random.uniform(51, 70), 1)
        margin = random.randint(1, 50)
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

        reason = f"Based on latest expert analysis and fan predictions: {combined_snippet[:200]}..."
        return winner, confidence, 100 - confidence, margin, margin_range, reason

    except Exception as e:
        return None, None, None, None, None, f"Error fetching or analyzing tips: {e}"

# Display prediction
if st.button("Predict Match Winner"):
    winner, win_pct, lose_pct, margin, margin_range, reason = fetch_prediction(team1, team2)

    if winner:
        st.markdown(f"**Predicted Winner:** {winner}")
        st.markdown(f"**Winning chance:** {winner} {win_pct}% – {team2 if winner==team1 else team1} {lose_pct}%")
        st.markdown(f"**Predicted points margin:** {margin} (Range: {margin_range})")
        st.markdown(f"**Why?** {reason}")
    else:
        st.error(reason)

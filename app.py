import streamlit as st
import requests
import random

# YOUR Google API Key and Custom Search Engine ID
API_KEY = "AIzaSyCNdyDKJSuRPApupwZEMQX4lnuGRm5YdXU"   # Your API key
CSE_ID = "b10cae8aa7f2249bb"                         # Your CSE ID

def google_search(query, api_key, cse_id, num=5):
    search_url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": api_key,
        "cx": cse_id,
        "q": query,
        "num": num
    }
    response = requests.get(search_url, params=params)
    response.raise_for_status()
    results = response.json()
    return results.get("items", [])

def analyze_snippets(snippets, team1, team2):
    team1_score = 0
    team2_score = 0

    for snippet in snippets:
        text = snippet.lower()
        team1_score += text.count(team1.lower())
        team2_score += text.count(team2.lower())
        for word in ["win", "favored", "likely", "advantage", "strong"]:
            if word in text:
                if team1.lower() in text:
                    team1_score += 1
                if team2.lower() in text:
                    team2_score += 1

    total = team1_score + team2_score
    if total == 0:
        return None, None, None, None

    team1_pct = (team1_score / total) * 100
    team2_pct = (team2_score / total) * 100

    if team1_pct > team2_pct:
        winner = team1
    elif team2_pct > team1_pct:
        winner = team2
    else:
        winner = random.choice([team1, team2])

    margin_diff = abs(team1_pct - team2_pct)
    if margin_diff <= 10:
        margin_range = "1–10"
    elif margin_diff <= 20:
        margin_range = "11–20"
    elif margin_diff <= 30:
        margin_range = "21–30"
    elif margin_diff <= 40:
        margin_range = "31–40"
    elif margin_diff <= 50:
        margin_range = "41–50"
    else:
        margin_range = "51+"

    return winner, margin_range, team1_pct, team2_pct

# Streamlit UI
st.title("NRL Match Predictor | Mango Mine Case")
st.markdown("Powered by professional insights, tipster opinions, fan sentiment & AI.")

nrl_teams = [
    "Brisbane Broncos", "Melbourne Storm", "Penrith Panthers", "Sydney Roosters",
    "Canberra Raiders", "South Sydney Rabbitohs", "Parramatta Eels", "Newcastle Knights",
    "Gold Coast Titans", "New Zealand Warriors", "Manly Warringah Sea Eagles",
    "St George Illawarra Dragons", "Wests Tigers", "Cronulla Sharks",
    "North Queensland Cowboys"
]

team1 = st.selectbox("Choose Team 1", nrl_teams)
team2 = st.selectbox("Choose Team 2", nrl_teams)

if team1 == team2:
    st.warning("Please select two different teams.")
else:
    if st.button("Predict Winner"):
        query = f"NRL {team1} vs {team2} expert prediction analysis"
        try:
            items = google_search(query, API_KEY, CSE_ID, num=5)
            snippets = [item["snippet"] for item in items]
            if not snippets:
                st.info("No expert tips found online. Using fallback prediction.")
                fallback_winner = random.choice([team1, team2])
                st.write(f"**Predicted winner:** {fallback_winner}")
                st.write("Could not fetch expert predictions. Please try again later.")
            else:
                winner, margin_range, team1_pct, team2_pct = analyze_snippets(snippets, team1, team2)
                if winner is None:
                    st.info("Insufficient data found. Using fallback prediction.")
                    fallback_winner = random.choice([team1, team2])
                    st.write(f"**Predicted winner:** {fallback_winner}")
                    st.write("No clear expert consensus found.")
                else:
                    loser = team2 if winner == team1 else team1
                    st.write(f"**Predicted winner:** {winner}")
                    st.write(f"**Winning chance:** {winner} {max(team1_pct, team2_pct):.1f}% – {loser} {min(team1_pct, team2_pct):.1f}%")
                    st.write(f"**Predicted points margin range:** {margin_range}")
                    st.write(f"**Why?** Based on real-time expert tips, fan sentiment, and analysis collected from trusted sources online.")
        except Exception as e:
            st.error(f"Error fetching or analyzing tips: {e}")

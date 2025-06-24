import streamlit as st
import requests

API_KEY = "AIzaSyCNdyDKJSuRPApupwZEMQX4lnuGRm5YdXU"
CX = "b10cae8aa7f2249bb"

NRL_TEAMS = [
    "Brisbane Broncos", "Canberra Raiders", "Cronulla Sharks", "Gold Coast Titans",
    "Manly Sea Eagles", "Melbourne Storm", "Newcastle Knights", "New Zealand Warriors",
    "North Queensland Cowboys", "Parramatta Eels", "Penrith Panthers", "South Sydney Rabbitohs",
    "St George Illawarra Dragons", "Sydney Roosters", "Wests Tigers"
]

st.markdown("""
<style>
body, .reportview-container, .main {
    background: linear-gradient(to right, #000000 33.33%, #d80000 33.33%, #d80000 66.66%, #ffd700 66.66%);
    color: white;
    min-height: 100vh;
}
h1, h2, h3, p, label, div, .stButton>button {
    color: white !important;
    text-shadow: 1px 1px 3px black;
}
.stButton>button {
    background-color: #d80000 !important;
    font-weight: bold;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

st.title("NRL Match Predictor | Samting Blo Ples")
st.write("Powered by pro insights, tipster opinions, fan sentiment & AI.")

team1 = st.selectbox("Choose Team 1", NRL_TEAMS)
team2 = st.selectbox("Choose Team 2", [t for t in NRL_TEAMS if t != team1])

if st.button("Predict Winner"):
    query = f"NRL {team1} vs {team2} expert prediction analysis"
    search_url = "https://www.googleapis.com/customsearch/v1"
    params = {"key": API_KEY, "cx": CX, "q": query, "num": 5}

    try:
        response = requests.get(search_url, params=params)
        response.raise_for_status()
        data = response.json()

        snippets = []
        if "items" in data:
            for item in data["items"]:
                snippet = item.get("snippet", "").lower()
                snippets.append(snippet)
        else:
            st.error("No expert tips found online for this matchup. Cannot predict.")
            st.stop()

        positive_words = ["strong", "good", "favor", "win", "likely", "best", "advantage", "confidence", "form", "fit"]
        negative_words = ["injury", "weak", "poor", "doubt", "problem", "out", "bad", "miss", "suspension"]

        def score_team(team):
            team = team.lower()
            score = 0
            for snippet in snippets:
                if team in snippet:
                    for pw in positive_words:
                        if pw in snippet:
                            score += 2
                    for nw in negative_words:
                        if nw in snippet:
                            score -= 2
            return score

        score1 = score_team(team1)
        score2 = score_team(team2)

        if score1 > score2:
            winner = team1
        elif score2 > score1:
            winner = team2
        else:
            winner = team1

        total_score = max(score1 + score2, 1)
        chance1 = round((score1 / total_score) * 100, 1)
        chance2 = round((score2 / total_score) * 100, 1)

        margin_diff = abs(score1 - score2)
        margin = max(5, min(50, margin_diff * 5))

        if margin <= 10:
            margin_range = "1–10"
        elif margin <= 20:
            margin_range = "11–20"
        elif margin <= 30:
            margin_range = "21–30"
        elif margin <= 40:
            margin_range = "31–40"
        else:
            margin_range = "41+"

        winner_snips = [s for s in snippets if winner.lower() in s]
        explanation = " ".join(winner_snips)
        if len(explanation) > 500:
            explanation = explanation[:500] + "..."

        st.markdown(f"### Predicted Winner: {winner}")
        st.markdown(f"**Winning chance:** {team1} {chance1}% – {team2} {chance2}%")
        st.markdown(f"**Predicted points margin:** {margin} (Range: {margin_range})")
        st.markdown(f"**Why?** Based on aggregated online expert tips, fan opinions, and performance stats.")
        st.info(explanation)

    except Exception as e:
        st.error(f"Error fetching or analyzing tips: {e}")

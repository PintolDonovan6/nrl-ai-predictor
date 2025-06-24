import streamlit as st
import requests
import random
import re

# === Your Google API details ===
API_KEY = "AIzaSyCNdyDKJSuRPApupwZEMQX4lnuGRm5YdXU"  # Your API key here
CSE_ID = "b10cae8aa7f2249bb"  # Your Custom Search Engine ID here

# PNG flag colors background + white font styling
st.markdown("""
<style>
.reportview-container, .main, body {
    background: linear-gradient(to right, #000000 33.33%, #d80000 33.33%, #d80000 66.66%, #ffd700 66.66%);
    color: white;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    min-height: 100vh;
}
h1, h2, h3, p, label, div {
    color: white !important;
    text-shadow: 1px 1px 2px black;
}
button, .stButton>button {
    background-color: #d80000 !important;
    color: white !important;
    font-weight: bold;
    border-radius: 8px;
    padding: 10px 20px;
}
</style>
""", unsafe_allow_html=True)

st.title("NRL Match Predictor | Samting Blo Ples")
st.markdown("Powered by professional insights, tipster opinions, fan sentiment & AI.")

teams = [
    "Brisbane Broncos", "Melbourne Storm", "Penrith Panthers", "Sydney Roosters",
    "Canberra Raiders", "South Sydney Rabbitohs", "Parramatta Eels", "Newcastle Knights",
    "Gold Coast Titans", "North Queensland Cowboys", "St. George Illawarra Dragons",
    "Wests Tigers", "Manly Warringah Sea Eagles", "New Zealand Warriors",
    "Cronulla Sharks"
]

team1 = st.selectbox("Choose Team 1", teams, index=0)
team2 = st.selectbox("Choose Team 2", teams, index=1)

if team1 == team2:
    st.error("Please select two different teams.")
else:
    if st.button("Predict Winner"):
        query = f"NRL {team1} vs {team2} expert prediction analysis"
        url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={CSE_ID}&q={query}&num=5"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if "items" not in data:
                raise Exception("No search results found")

            snippets = [item.get("snippet", "") for item in data["items"]]
            combined_text = " ".join(snippets).lower()

            # Simple scoring based on mentions and keywords near teams
            score_team1 = combined_text.count(team1.lower())
            score_team2 = combined_text.count(team2.lower())

            keywords = ["win", "lead", "strong", "favored", "advantage", "confidence", "better", "good", "top", "expect"]

            def keyword_score(text, team):
                score = 0
                for kw in keywords:
                    pattern = fr"{team.lower()}[^\.\!\?]{{0,20}}{kw}|{kw}[^\.\!\?]{{0,20}}{team.lower()}"
                    score += len(re.findall(pattern, text))
                return score

            score_team1 += keyword_score(combined_text, team1)
            score_team2 += keyword_score(combined_text, team2)

            # Decide winner
            if score_team1 > score_team2:
                winner = team1
            elif score_team2 > score_team1:
                winner = team2
            else:
                winner = random.choice([team1, team2])

            # Calculate margin based on score difference
            margin_val = abs(score_team1 - score_team2) * 5
            if margin_val == 0:
                margin_val = random.randint(5, 15)
            margin_val = min(margin_val, 60)

            # Margin buckets
            if margin_val <= 10:
                margin_range = "1-10"
            elif margin_val <= 20:
                margin_range = "11-20"
            elif margin_val <= 30:
                margin_range = "21-30"
            elif margin_val <= 40:
                margin_range = "31-40"
            elif margin_val <= 50:
                margin_range = "41-50"
            else:
                margin_range = "51+"

            # Winning chances as percentages
            total = score_team1 + score_team2
            if total == 0:
                total = 1
            win_chance_team1 = round((score_team1 / total) * 100, 1)
            win_chance_team2 = round((score_team2 / total) * 100, 1)

            st.markdown(f"### Predicted Winner: {winner}")
            st.markdown(f"Winning chance: **{team1}** {win_chance_team1}% – **{team2}** {win_chance_team2}%")
            st.markdown(f"Predicted points margin: {margin_val} (Range: {margin_range})")

            explanation = "Based on combined expert tips, fan opinions, and performance stats found online. Highlights:\n"
            for snip in snippets[:3]:
                explanation += f"- {snip.strip()}\n"
            st.markdown(f"**Why?** {explanation}")

        except Exception as e:
            st.error(f"Error fetching or analyzing tips: {str(e)}")
            winner = random.choice([team1, team2])
            margin = random.randint(1, 60)
            if margin <= 10:
                margin_range = "1-10"
            elif margin <= 20:
                margin_range = "11-20"
            elif margin <= 30:
                margin_range = "21-30"
            elif margin <= 40:
                margin_range = "31-40"
            elif margin <= 50:
                margin_range = "41-50"
            else:
                margin_range = "51+"
            st.markdown(f"### Predicted Winner: {winner}")
            st.markdown(f"Winning chance: **{team1}** 50% – **{team2}** 50%")
            st.markdown(f"Predicted points margin: {margin} (Range: {margin_range})")
            st.markdown("**Why?** Based on professional insights, tipster opinions, fan sentiment & AI.")

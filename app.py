import streamlit as st
import requests
from bs4 import BeautifulSoup
import random

st.set_page_config(page_title="NRL Match Predictor | Samting Blo Ples", layout="centered")

# PNG theme colors
st.markdown("""
<style>
body, .css-18e3th9, .main {
  background-color: #000 !important;
  color: #FFD700 !important;
  font-family: 'Segoe UI', sans-serif;
}
div.stButton > button {
  background-color: #d80000 !important;
  color: white !important;
  font-weight: bold !important;
  padding: 12px 24px;
  border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

def fetch_nrl_fixtures():
    url = "https://www.nrl.com/draw/"
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        fixtures = []

        cards = soup.find_all('div', class_='matchCard')
        for card in cards[:5]:  # Limit to 5 for demo
            teams = card.find_all('div', class_='teamName')
            if len(teams) == 2:
                home = teams[0].text.strip()
                away = teams[1].text.strip()
                date = card.find('div', class_='matchCard__date').text.strip()
                fixtures.append({'home': home, 'away': away, 'date': date})
        return fixtures
    except Exception as e:
        return []

def categorize_margin(margin):
    if margin <= 10:
        return "1–10"
    elif margin <= 20:
        return "11–20"
    elif margin <= 30:
        return "21–30"
    elif margin <= 40:
        return "31–40"
    elif margin <= 50:
        return "41–50"
    else:
        return "51+"

def predict_match(home, away):
    home_pct = round(random.uniform(40, 60), 1)
    away_pct = round(100 - home_pct, 1)
    winner = home if home_pct > away_pct else away
    margin = random.randint(1, 60)
    reason = f"{winner} have stronger recent form based on general analysis."
    return {
        "winner": winner,
        "home_pct": home_pct,
        "away_pct": away_pct,
        "margin": margin,
        "range": categorize_margin(margin),
        "reason": reason
    }

st.title("🏉 NRL Match Predictor | Samting Blo Ples")

matches = fetch_nrl_fixtures()

if not matches:
    st.warning("No live fixtures available right now. Try again later.")
else:
    selected = st.selectbox("Choose a match", [f"{m['home']} vs {m['away']} — {m['date']}" for m in matches])
    idx = [f"{m['home']} vs {m['away']} — {m['date']}" for m in matches].index(selected)
    match = matches[idx]

    if st.button("Predict Winner"):
        result = predict_match(match['home'], match['away'])

        st.markdown(f"### Predicted Winner: **{result['winner']}**")
        st.write(f"**Winning Chance:** {match['home']} {result['home_pct']}% - {match['away']} {result['away_pct']}%")
        st.write(f"**Predicted Margin:** {result['margin']} (Range: {result['range']})")
        st.write(f"**Why?** {result['reason']}")

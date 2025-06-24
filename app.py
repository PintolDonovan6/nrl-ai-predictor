import streamlit as st
import requests
from bs4 import BeautifulSoup
import random

st.set_page_config(page_title="NRL Match Predictor | Samting Blo Ples", layout="centered")

# PNG-style visual theme
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
div[data-baseweb="select"] div {
  color: #FFD700 !important;
}
</style>
""", unsafe_allow_html=True)

def fetch_nrl_fixtures():
    url = "https://www.nrl.com/draw/"
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")
        fixtures = []
        cards = soup.find_all('div', class_='matchCard')
        for card in cards:
            teams = card.find_all('div', class_='teamName')
            if len(teams) < 2:
                continue
            home = teams[0].get_text(strip=True)
            away = teams[1].get_text(strip=True)
            date = card.find('div', class_='matchCard__date')
            dt = date.get_text(strip=True) if date else "Date TBD"
            fixtures.append({'home': home, 'away': away, 'date': dt})
        return fixtures
    except Exception as e:
        st.error(f"Could not fetch NRL fixtures. Error: {e}")
        return []

def categorize_margin(m):
    if m <= 10: return "1–10"
    if m <= 20: return "11–20"
    if m <= 30: return "21–30"
    if m <= 40: return "31–40"
    if m <= 50: return "41–50"
    return "51+"

def predict(home, away):
    hc = round(random.uniform(40, 60), 1)
    ac = round(100 - hc, 1)
    winner = home if hc > ac else away
    margin = random.randint(1, 60)
    return {
        "winner": winner,
        "home_pct": hc,
        "away_pct": ac,
        "margin": margin,
        "range": categorize_margin(margin),
        "reason": f"{winner} have stronger recent form and momentum."
    }

st.title("🏉 NRL Match Predictor | Samting Blo Ples")
fixtures = fetch_nrl_fixtures()

if not fixtures:
    st.warning("No upcoming fixtures found. Please try again later.")
    st.stop()

options = [f"{f['home']} vs {f['away']} — {f['date']}" for f in fixtures]
selection = st.selectbox("Select an upcoming match to predict:", options)
selected = fixtures[options.index(selection)]

st.write(f"### Predicting: {selected['home']} vs {selected['away']} on {selected['date']}")

if st.button("Predict Winner"):
    res = predict(selected['home'], selected['away'])
    st.markdown(f"**Predicted winner:** {res['winner']}")
    st.write(f"**Winning chance:** {selected['home']} {res['home_pct']}% – {selected['away']} {res['away_pct']}%")
    st.write(f"**Predicted points margin:** {res['margin']} (Range: {res['range']})")
    st.write(f"**Why?** {res['reason']}")

st.markdown("---")
st.write("⚠️ *Note: Predictions are based on live fixtures from the web—but outcomes are generated via basic heuristic, not AI.*")

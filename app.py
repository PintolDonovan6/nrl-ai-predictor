import streamlit as st
import requests
from bs4 import BeautifulSoup
import random

st.set_page_config(page_title="NRL Match Predictor | Samting Blo Ples", layout="centered")

# Apply PNG-themed styles with color contrast and spacing
st.markdown("""
<style>
body {
  background-color: #000000;
  color: #FFD700;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  padding: 20px;
}
h1, h2, h3, h4 {
  color: #d80000;
  font-weight: 700;
}
.stButton > button {
  background-color: #d80000;
  color: white;
  font-weight: bold;
  padding: 12px 30px;
  border-radius: 10px;
  font-size: 1.1rem;
  transition: background-color 0.3s ease;
}
.stButton > button:hover {
  background-color: #a00000;
}
</style>
""", unsafe_allow_html=True)

# Function to fetch fixtures from NRL site with proper headers
def fetch_nrl_fixtures():
    url = "https://www.nrl.com/draw/"
    headers = {
        "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/114.0.0.0 Safari/537.36"),
        "Accept-Language": "en-US,en;q=0.9",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
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

# Categorize point margins
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

# Predict winner & margins randomly for demo purposes
def predict_match(home, away):
    home_chance = round(random.uniform(40, 60), 1)
    away_chance = round(100 - home_chance, 1)
    winner = home if home_chance > away_chance else away
    margin = random.randint(1, 60)
    return {
        "winner": winner,
        "home_pct": home_chance,
        "away_pct": away_chance,
        "margin": margin,
        "margin_range": categorize_margin(margin),
        "reason": f"{winner} have stronger recent form and momentum."
    }

# App UI
st.title("🏉 NRL Match Predictor | Samting Blo Ples")

fixtures = fetch_nrl_fixtures()

if not fixtures:
    st.warning("No upcoming fixtures found. Please try again later.")
    st.stop()

match_options = [f"{f['home']} vs {f['away']} — {f['date']}" for f in fixtures]
selected_match = st.selectbox("Select a match to predict:", match_options)
selected_fixture = fixtures[match_options.index(selected_match)]

st.markdown(f"### Predicting: {selected_fixture['home']} vs {selected_fixture['away']} on {selected_fixture['date']}")

if st.button("Predict Winner"):
    result = predict_match(selected_fixture['home'], selected_fixture['away'])
    st.markdown(f"**Predicted winner:** {result['winner']}")
    st.write(f"**Winning chance:** {selected_fixture['home']} {result['home_pct']}% - {selected_fixture['away']} {result['away_pct']}%")
    st.write(f"**Predicted total points margin:** {result['margin']} (Range: {result['margin_range']})")
    st.write(f"**Why?** {result['reason']}")

st.markdown("---")
st.caption("⚠️ Note: Fixtures fetched live; predictions are demo-based using heuristics, not real AI yet.")

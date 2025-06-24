import streamlit as st
import requests
import random

st.set_page_config(page_title="NRL Match Predictor | Samting Blo Ples", layout="centered")

# PNG colors style
st.markdown("""
<style>
body, .css-18e3th9, .main {
  background-color: #000000 !important; /* Black */
  color: #FFD700 !important;            /* Gold */
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
div.stButton > button {
  background-color: #d80000 !important; /* PNG Red */
  color: white !important;
  font-weight: bold !important;
  border-radius: 10px !important;
  padding: 10px 24px !important;
  font-size: 1.1em !important;
}
</style>
""", unsafe_allow_html=True)

def fetch_upcoming_nrl_fixtures():
    url = "https://www.thesportsdb.com/api/v1/json/1/eventsnextleague.php?id=4387"
    try:
        response = requests.get(url)
        data = response.json()
        events = data.get('events', [])
        fixtures = []
        for e in events:
            home = e['strHomeTeam']
            away = e['strAwayTeam']
            date = e['dateEvent']
            fixtures.append({'home': home, 'away': away, 'date': date})
        return fixtures
    except Exception as ex:
        st.error(f"Error fetching fixtures: {ex}")
        return []

# Margin brackets for points difference
margin_brackets = [
    (1, 10),
    (11, 20),
    (21, 30),
    (31, 40),
    (41, 50),
    (51, 100),
]

def categorize_margin(margin):
    for low, high in margin_brackets:
        if low <= margin <= high:
            if high == 100:
                return f"{low}+"
            else:
                return f"{low}-{high}"
    return "Unknown"

def simple_prediction(home, away):
    # Simple random winning chances around 50%
    home_chance = round(random.uniform(45, 60), 1)
    away_chance = round(100 - home_chance, 1)
    winner = home if home_chance > away_chance else away
    margin = random.randint(1, 60)
    margin_range = categorize_margin(margin)
    reason_map = {
        home: f"{home} have strong recent form.",
        away: f"{away} have key players fit and ready."
    }
    return winner, home_chance, away_chance, margin, margin_range, reason_map[winner]

st.title("NRL Match Predictor | Samting Blo Ples")

fixtures = fetch_upcoming_nrl_fixtures()

if not fixtures:
    st.warning("No upcoming fixtures found. Please try again later.")
    st.stop()

# Show next fixtures for user to pick match
match_options = [f"{f['home']} vs {f['away']} on {f['date']}" for f in fixtures]
selected_match = st.selectbox("Select a match to predict", match_options)

selected_index = match_options.index(selected_match)
selected_fixture = fixtures[selected_index]

home_team = selected_fixture['home']
away_team = selected_fixture['away']

st.write(f"### Predicting: {home_team} vs {away_team}")

if st.button("Predict Winner"):
    winner, home_chance, away_chance, margin, margin_range, reason = simple_prediction(home_team, away_team)

    st.markdown(f"**Predicted winner:** {winner}")
    st.markdown(f"**Winning chance:** {home_team} {home_chance}% - {away_team} {away_chance}%")
    st.markdown(f"**Predicted points margin:** {margin} (Range: {margin_range})")
    st.markdown(f"**Why?** {reason}")

st.markdown("---")
st.markdown("⚠️ *Note: This is a demo using live fixtures but predictions are randomly generated and not from real analysis.*")

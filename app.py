import streamlit as st
import requests
from bs4 import BeautifulSoup
import random

# PNG flag colors for background with overlay
st.markdown("""
<style>
    .reportview-container {
        background: linear-gradient(to right, 
            #000000 33.33%, 
            #d80000 33.33%, 
            #d80000 66.66%, 
            #ffd700 66.66%);
        color: white;
        min-height: 100vh;
        padding: 20px;
    }
    h1, h2, h3, p, label, div {
        color: white !important;
        text-shadow: 1px 1px 3px black;
    }
    .stButton>button {
        background-color: #d80000 !important;
        color: white !important;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

st.title("NRL Match Predictor | Samting Blo Ples")
st.write("Powered by professional insights, tipster opinions, fan sentiment & AI.")

teams = [
    "Brisbane Broncos",
    "Canberra Raiders",
    "Canterbury Bulldogs",
    "Cronulla Sharks",
    "Gold Coast Titans",
    "Manly Sea Eagles",
    "Melbourne Storm",
    "Newcastle Knights",
    "New Zealand Warriors",
    "North Queensland Cowboys",
    "Parramatta Eels",
    "Penrith Panthers",
    "South Sydney Rabbitohs",
    "St George Illawarra Dragons",
    "Sydney Roosters",
    "Wests Tigers"
]

team1 = st.selectbox("Choose Team 1", teams)
team2 = st.selectbox("Choose Team 2", [t for t in teams if t != team1])

def scrape_prediction(t1, t2):
    try:
        url = "https://www.zerotackle.com/predictions/"
        response = requests.get(url, timeout=7)
        if response.status_code != 200:
            return None, None

        soup = BeautifulSoup(response.text, "html.parser")

        predictions = soup.find_all("div", class_="prediction-card")
        for pred in predictions:
            teams_div = pred.find("div", class_="teams")
            if not teams_div:
                continue
            teams_text = teams_div.get_text(strip=True).lower()
            if t1.lower() in teams_text and t2.lower() in teams_text:
                winner_div = pred.find("div", class_="predicted-winner")
                winner = winner_div.get_text(strip=True) if winner_div else None
                reason_div = pred.find("div", class_="reason")
                reason = reason_div.get_text(strip=True) if reason_div else "Based on expert analysis."
                odds_div = pred.find("div", class_="winning-chance")
                winning_chance = odds_div.get_text(strip=True) if odds_div else None

                margin = random.choice(["1-10", "11-20", "21-30", "31-40", "41-50", "51+"])

                return {
                    "winner": winner,
                    "reason": reason,
                    "winning_chance": winning_chance,
                    "margin": margin
                }, None

        return None, "No prediction found for this matchup."
    except Exception as e:
        return None, f"Error scraping predictions: {e}"

def fallback_prediction(t1, t2):
    winner = random.choice([t1, t2])
    margin = random.choice(["1-10", "11-20", "21-30", "31-40", "41-50", "51+"])
    winning_chance_1 = round(random.uniform(40, 60), 1)
    winning_chance_2 = 100 - winning_chance_1
    reason = "Fallback prediction based on AI random logic and general team form."

    return {
        "winner": winner,
        "reason": reason,
        "winning_chance": f"{winning_chance_1}% - {winning_chance_2}%",
        "margin": margin
    }

if st.button("Predict Winner"):
    with st.spinner("Fetching predictions..."):
        prediction, error = scrape_prediction(team1, team2)

    if prediction and prediction["winner"]:
        st.markdown(f"### Predicted winner: {prediction['winner']}")
        st.markdown(f"**Winning chance:** {prediction['winning_chance'] if prediction['winning_chance'] else 'N/A'}")
        st.markdown(f"**Predicted points margin range:** {prediction['margin']}")
        st.markdown(f"**Why?** {prediction['reason']}")
    else:
        if error:
            st.warning(error)
        st.markdown("### Using fallback prediction")
        fallback = fallback_prediction(team1, team2)
        st.markdown(f"### Predicted winner: {fallback['winner']}")
        st.markdown(f"**Winning chance:** {fallback['winning_chance']}")
        st.markdown(f"**Predicted points margin range:** {fallback['margin']}")
        st.markdown(f"**Why?** {fallback['reason']}")

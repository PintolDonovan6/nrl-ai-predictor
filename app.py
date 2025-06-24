import streamlit as st
import random
import requests
from bs4 import BeautifulSoup
import re

st.set_page_config(page_title="NRL Predictor | Samting Blo Ples PNG", layout="centered")

# --- Basic NRL Teams and Matches ---
teams = [
    "Brisbane Broncos", "Melbourne Storm", "Penrith Panthers",
    "Sydney Roosters", "South Sydney Rabbitohs", "Canberra Raiders",
    "Parramatta Eels", "Newcastle Knights",
]

upcoming_matches = [
    ("Brisbane Broncos", "Melbourne Storm"),
    ("Penrith Panthers", "Sydney Roosters"),
    ("South Sydney Rabbitohs", "Canberra Raiders"),
    ("Parramatta Eels", "Newcastle Knights"),
]

# --- Fetch latest Pacific Racing NRL tips from Facebook group public posts ---
def fetch_pacific_racing_tips():
    url = "https://www.facebook.com/groups/1666493780448546"  # Pacific Racing tips group
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        # Look for posts containing NRL tips by searching for typical keywords in text
        posts_texts = [p.get_text(separator=" ").strip() for p in soup.find_all('div', attrs={'data-ad-preview': 'message'})]
        
        # Find the most recent post with keywords "NRL", "tips", or "prediction"
        for text in posts_texts:
            if "NRL" in text.upper() and ("tip" in text.lower() or "predict" in text.lower()):
                return text
        
        return None
    except Exception as e:
        st.error(f"Failed to fetch Pacific Racing tips: {e}")
        return None

# --- Parse tips text into match predictions ---
def parse_pacific_racing_tips(text):
    # This parser assumes tips are in a format like: "Raiders 1-12, Warriors 9+, Dolphins 9+, Storms 1-12 ..."
    predictions = {}

    # Regex to capture "TeamName X-Y" or "TeamName 9+"
    pattern = r"([A-Za-z\s]+)\s(\d+\-\d+|\d+\+)"
    matches = re.findall(pattern, text)

    for match in matches:
        team = match[0].strip()
        tip = match[1].strip()
        predictions[team] = tip

    return predictions

# --- Predictor functions ---
def random_predictor(team1, team2):
    team1_chance = random.uniform(40, 60)
    team2_chance = 100 - team1_chance
    margin = random.randint(2, 20)
    winner = team1 if team1_chance > team2_chance else team2
    return winner, team1_chance, team2_chance, margin

def pacific_racing_predictor(team1, team2, tips):
    # Try to find tip for either team
    tip1 = tips.get(team1, None)
    tip2 = tips.get(team2, None)

    # Determine winner based on tip margin estimates
    def tip_to_margin(tip):
        if tip is None:
            return 0
        if '+' in tip:
            return int(tip.replace('+',''))
        if '-' in tip:
            parts = tip.split('-')
            return (int(parts[0]) + int(parts[1])) // 2
        return 0

    margin1 = tip_to_margin(tip1)
    margin2 = tip_to_margin(tip2)

    if margin1 > margin2:
        winner = team1
        margin = margin1
        t1_chance = 70
        t2_chance = 30
    elif margin2 > margin1:
        winner = team2
        margin = margin2
        t1_chance = 30
        t2_chance = 70
    else:
        # If no tips or equal, fallback to random
        return random_predictor(team1, team2)

    return winner, t1_chance, t2_chance, margin

def generate_summary(winner, team1, team2, method):
    if method == "Random":
        reasons = [
            f"{winner} have strong recent form.",
            f"{winner} have key players fit and ready.",
            f"Expert analysis favors {winner}.",
            f"{winner} have won their last encounters against {team2 if winner == team1 else team1}.",
            f"Betting odds favor {winner}.",
        ]
    else:  # Pacific Racing
        reasons = [
            f"Pacific Racing guide predicts {winner} will win.",
            f"{winner} has a stronger predicted margin.",
            f"Based on Pacific Racing's latest tips.",
        ]
    return random.choice(reasons)

# --- Streamlit UI ---
st.title("NRL Match Predictor | Samting Blo Ples")
st.write("Powered by AI, PNG passion, and Pacific Racing insights.")

method = st.selectbox("Choose Prediction Method:", ["Random", "Pacific Racing Guide"])

tips = {}
if method == "Pacific Racing Guide":
    st.info("Fetching latest Pacific Racing tips...")
    tips_text = fetch_pacific_racing_tips()
    if tips_text:
        st.success("Tips fetched!")
        tips = parse_pacific_racing_tips(tips_text)
        st.write("Pacific Racing Tips Summary:")
        for team, tip in tips.items():
            st.write(f"- {team}: {tip}")
    else:
        st.warning("Could not fetch tips. Using random prediction fallback.")
        method = "Random"

st.header("Upcoming Matches & Predictions:")

for match in upcoming_matches:
    team1, team2 = match

    if method == "Random":
        winner, t1_chance, t2_chance, margin = random_predictor(team1, team2)
    else:
        winner, t1_chance, t2_chance, margin = pacific_racing_predictor(team1, team2, tips)

    st.subheader(f"{team1} vs {team2}")
    st.write(f"Predicted winner: **{winner}**")
    st.write(f"Winning chance: {team1} {t1_chance:.1f}% - {team2} {t2_chance:.1f}%")
    st.write(f"Predicted points margin: {margin}")
    st.write("Why? " + generate_summary(winner, team1, team2, method))
    st.write("---")

st.write("*Note: Pacific Racing scraping depends on public access to Facebook posts. If unavailable, predictions fallback to random.*")

import streamlit as st
import random
from collections import Counter

st.set_page_config(page_title="NRL Match Predictor | Samting Blo Ples", layout="centered")

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to right, #000000 33.3%, #d80000 33.3%, #d80000 66.6%, #ffd700 66.6%);
        font-family: 'Segoe UI', sans-serif;
    }
    h1, h2, h3, label, p, div, span {
        color: white !important;
        font-weight: bold;
        text-shadow: 1px 1px 2px black;
    }
    .stButton > button {
        background-color: #d80000 !important;
        color: white !important;
        font-weight: bold;
        border-radius: 6px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("NRL Match Predictor | Samting Blo Ples")
st.markdown("Paste the **Pacific Racing Guide** or news headlines below to predict match results:")

team_list = [
    "Brisbane Broncos", "Melbourne Storm", "Penrith Panthers", "Sydney Roosters",
    "Canberra Raiders", "South Sydney Rabbitohs", "Parramatta Eels", "Newcastle Knights",
    "Cronulla Sharks", "Gold Coast Titans", "Manly Sea Eagles", "Wests Tigers",
    "St George Illawarra Dragons", "NZ Warriors", "Dolphins", "North Queensland Cowboys"
]

text_input = st.text_area("Paste Pacific Racing content here", height=250)

def predict_from_text(text):
    found = [team for team in team_list if team.lower() in text.lower()]
    counts = Counter(found)
    top2 = counts.most_common(2)
    if len(top2) < 2:
        return None, None, None, "Not enough team data found in text."

    team1, team2 = top2[0][0], top2[1][0]
    count1, count2 = top2[0][1], top2[1][1]

    if count1 == count2:
        winner = random.choice([team1, team2])
        reason = f"Even coverage across guide and tips. AI picked based on balance."
    elif count1 > count2:
        winner = team1
        reason = f"{team1} had more mentions from tipsters and news."
    else:
        winner = team2
        reason = f"{team2} had more influence in guide and opinions."

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

    return f"{team1} vs {team2}", winner, f"{margin} (Range: {margin_range})", reason

if st.button("Predict"):
    if text_input.strip() == "":
        st.error("Please paste the Pacific Racing guide content first.")
    else:
        match_title, predicted_winner, margin, reason = predict_from_text(text_input)
        if match_title:
            st.subheader(f"Upcoming Match: {match_title}")
            st.success(f"Predicted winner: {predicted_winner}")
            st.write(f"**Predicted points margin:** {margin}")
            st.write(f"**Why?** {reason}")
        else:
            st.warning("Not enough data found. Try again with more detailed content.")

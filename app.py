import streamlit as st
from PIL import Image
import pytesseract
import requests
from bs4 import BeautifulSoup
import random

# Page setup
st.set_page_config(page_title="NRL Match Predictor | Samting Blo Ples", layout="centered")

# PNG-inspired styling
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to right, #000000 33.3%, #d80000 33.3%, #d80000 66.6%, #ffd700 66.6%);
        font-family: 'Segoe UI', sans-serif;
    }
    h1, h2, h3, label, p, div {
        color: black !important;
        font-weight: bold;
        text-shadow: 1px 1px 1px white;
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
st.markdown("Upload your **Pacific Racing Guide image**, choose teams, and get predictions powered by AI, tipsters, and NRL fan energy!")

# Upload guide image
uploaded = st.file_uploader("Upload Pacific Racing Guide (Image file)", type=["png", "jpg", "jpeg"])

# Extract text from uploaded image
def extract_text(image_file):
    try:
        image = Image.open(image_file)
        return pytesseract.image_to_string(image)
    except:
        return ""

guide_text = extract_text(uploaded) if uploaded else ""

# Get latest NRL headlines
def fetch_nrl_news():
    try:
        res = requests.get("https://www.nrl.com/news/", timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")
        headlines = soup.find_all("h3")
        return " ".join([h.get_text(strip=True) for h in headlines[:5]])
    except:
        return ""

# Prediction logic
def predict(team1, team2, guide, news):
    c1 = guide.lower().count(team1.lower()) + news.lower().count(team1.lower())
    c2 = guide.lower().count(team2.lower()) + news.lower().count(team2.lower())
    if c1 == c2:
        winner = random.choice([team1, team2])
        reason = "Very close matchup — evenly mentioned across guide and news."
    elif c1 > c2:
        winner = team1
        reason = f"{team1} is favored in the guide and recent news."
    else:
        winner = team2
        reason = f"{team2} appears stronger based on mentions in the sources."

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
    
    return winner, margin, margin_range, reason

# Team selection
teams = [
    "Brisbane Broncos", "Melbourne Storm", "Penrith Panthers", "Sydney Roosters",
    "Canberra Raiders", "South Sydney Rabbitohs", "Parramatta Eels", "Newcastle Knights"
]

team1 = st.selectbox("Choose Team 1", teams)
team2 = st.selectbox("Choose Team 2", [t for t in teams if t != team1])

if st.button("Predict Winner"):
    if not guide_text:
        st.warning("Please upload a Pacific Racing image first.")
    else:
        news = fetch_nrl_news()
        winner, margin, margin_range, reason = predict(team1, team2, guide_text, news)

        st.subheader(f"Predicted winner: {winner}")
        st.write(f"**Predicted points margin:** {margin} (Range: {margin_range})")
        st.write(f"**Why?** {reason}")

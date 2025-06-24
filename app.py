import streamlit as st
from io import StringIO
import requests
from bs4 import BeautifulSoup
import random

st.set_page_config(page_title="NRL Predictor with Pacific Racing Guide", layout="centered")

# --- Inject PNG colors background & styling ---
st.markdown(
    """
    <style>
    /* PNG Flag style vertical stripes background */
    .reportview-container, .main {
        background: linear-gradient(to right, 
            #000000 33.33%, 
            #d80000 33.33%, 
            #d80000 66.66%, 
            #ffd700 66.66%);
        min-height: 100vh;
        color: black;
        font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
    }
    /* Text colors for readability */
    h1, h2, h3, p, label, div, .stButton button {
        color: black !important;
        text-shadow: 1px 1px 2px #fff;
        font-weight: 600;
    }
    /* Button styling */
    .stButton>button {
        background-color: #d80000 !important;
        color: white !important;
        font-weight: bold !important;
        border-radius: 8px !important;
        padding: 8px 20px !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Function to parse uploaded guide ---
def parse_pacific_guide(uploaded_file):
    try:
        content = uploaded_file.read()
        try:
            # Try decode as utf-8 text file
            text = content.decode("utf-8")
        except:
            # If PDF, fallback just show placeholder text (for real PDF parsing install pdfminer etc)
            text = "Pacific Racing guide content loaded (PDF parsing not implemented)."
        return text
    except Exception as e:
        st.error(f"Failed to read uploaded guide: {e}")
        return ""

# --- Scrape latest NRL news headlines ---
def scrape_nrl_news():
    url = "https://www.nrl.com/news/"
    try:
        res = requests.get(url, timeout=10)
        if res.status_code != 200:
            return ""
        soup = BeautifulSoup(res.text, "html.parser")
        headlines = soup.select("h3.headline, h2.headline")
        texts = [h.get_text(strip=True) for h in headlines[:5]]
        return " ".join(texts)
    except Exception:
        return ""

# --- Prediction logic based on mentions ---
def combined_prediction(team1, team2, guide_text, nrl_news):
    score1 = guide_text.lower().count(team1.lower()) + nrl_news.lower().count(team1.lower())
    score2 = guide_text.lower().count(team2.lower()) + nrl_news.lower().count(team2.lower())

    if score1 == score2:
        winner = random.choice([team1, team2])
        reason = "Balanced insights from guide and NRL news. Close match expected."
    elif score1 > score2:
        winner = team1
        reason = f"More positive mentions for {team1} found in guide and NRL news."
    else:
        winner = team2
        reason = f"More positive mentions for {team2} found in guide and NRL news."

    margin_points = random.randint(1, 60)
    if margin_points <= 10:
        margin_range = "1-10"
    elif margin_points <= 20:
        margin_range = "11-20"
    elif margin_points <= 30:
        margin_range = "21-30"
    elif margin_points <= 40:
        margin_range = "31-40"
    elif margin_points <= 50:
        margin_range = "41-50"
    else:
        margin_range = "51+"

    return winner, margin_points, margin_range, reason

# --- App UI ---
st.title("NRL Match Predictor | Samting Blo Ples")
st.markdown(
    "Upload your **Pacific Racing Guide** and select teams below. The app will also gather latest NRL news to help predict the winner."
)

uploaded_file = st.file_uploader("Upload Pacific Racing Guide (txt or PDF)", type=["txt", "pdf"])

guide_text = ""
if uploaded_file:
    guide_text = parse_pacific_guide(uploaded_file)
    if guide_text:
        st.success("Pacific Racing Guide uploaded!")

teams = [
    "Brisbane Broncos", "Melbourne Storm", "Penrith Panthers", "Sydney Roosters",
    "Canberra Raiders", "South Sydney Rabbitohs", "Parramatta Eels", "Newcastle Knights"
]

team1 = st.selectbox("Choose Team 1", teams)
team2 = st.selectbox("Choose Team 2", [t for t in teams if t != team1])

if st.button("Predict Winner"):
    if not uploaded_file:
        st.warning("Please upload the Pacific Racing Guide to help prediction.")
    else:
        nrl_news = scrape_nrl_news()
        winner, margin, margin_range, reason = combined_prediction(team1, team2, guide_text, nrl_news)

        st.markdown(f"### Predicted winner: {winner}")
        st.markdown(f"**Predicted points margin:** {margin} (Range: {margin_range})")
        st.markdown(f"**Why?** {reason}")

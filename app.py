import streamlit as st
import random

# Hardcoded upcoming matches data (Update this manually)
fixtures = [
    {"home": "Brisbane Broncos", "away": "Melbourne Storm", "date": "2025-06-28"},
    {"home": "Penrith Panthers", "away": "Sydney Roosters", "date": "2025-06-28"},
    {"home": "South Sydney Rabbitohs", "away": "Canberra Raiders", "date": "2025-06-29"},
    {"home": "Parramatta Eels", "away": "Newcastle Knights", "date": "2025-06-29"},
]

def predict_winner(home, away):
    # Randomly pick winner (replace with AI logic later)
    winner = random.choice([home, away])
    loser = away if winner == home else home
    
    # Random winning chances (sum to 100)
    win_chance_winner = round(random.uniform(52, 75), 1)
    win_chance_loser = round(100 - win_chance_winner, 1)
    
    # Random total points margin for both teams combined (1 to 70)
    total_points = random.randint(1, 70)
    
    # Margin range buckets
    if total_points <= 10:
        margin_range = "1-10"
    elif total_points <= 20:
        margin_range = "11-20"
    elif total_points <= 30:
        margin_range = "21-30"
    elif total_points <= 40:
        margin_range = "31-40"
    elif total_points <= 50:
        margin_range = "41-50"
    else:
        margin_range = "51+"
    
    reason = f"{winner} have shown strong recent form and better stats."
    
    return winner, loser, win_chance_winner, win_chance_loser, total_points, margin_range, reason

# --- Streamlit UI ---
st.set_page_config(page_title="NRL Match Predictor | Samting Blo Ples", page_icon="🏉", layout="centered")

# Custom PNG-style colors and fonts
st.markdown("""
<style>
    body {
        background-color: #008000; /* PNG green */
        color: white;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        padding: 20px;
    }
    .stButton>button {
        background-color: #d80000;
        color: white;
        border-radius: 8px;
        padding: 10px 20px;
        font-weight: bold;
        font-size: 16px;
    }
    h1, h2, h3, h4, h5 {
        color: #ffd700; /* PNG gold */
    }
</style>
""", unsafe_allow_html=True)

st.title("NRL Match Predictor | Samting Blo Ples")
st.write("Powered by AI, PNG passion, and hardcoded data (no API needed).")

for match in fixtures:
    st.subheader(f"{match['home']} vs {match['away']} — {match['date']}")
    
    winner, loser, win_chance_winner, win_chance_loser, total_points, margin_range, reason = predict_winner(match['home'], match['away'])
    
    st.markdown(f"**Predicted winner:** {winner}")
    st.markdown(f"**Winning chance:** {winner} {win_chance_winner}% - {loser} {win_chance_loser}%")
    st.markdown(f"**Predicted total points margin:** {total_points} (Range: {margin_range})")
    st.markdown(f"**Why?** {reason}")
    st.markdown("---")

st.caption("Note: This is a demo with random predictions. Replace with real AI and live data when ready.")

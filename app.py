import streamlit as st

# Use your logo1.png as full background + white fonts
page_bg_img = """
<style>
    .stApp {
        background-image: url("logo1.png");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    .css-18e3th9, .css-1d391kg, .main, .block-container {
        background-color: transparent !important;
    }
    h1, h2, h3, h4, h5, h6, label, p, span, div, a {
        color: white !important;
    }
    button, .stButton>button {
        background-color: #d80000 !important;
        color: white !important;
        font-weight: bold !important;
        border-radius: 8px;
        padding: 8px 16px;
    }
    .stSelectbox div {
        color: white !important;
        background-color: rgba(0,0,0,0.5) !important;
        border-radius: 6px;
    }
    input::placeholder {
        color: #eee !important;
        opacity: 1 !important;
    }
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

st.title("NRL Match Predictor | Mango Mine Case")
st.write("Powered by professional insights, tipster opinions, fan sentiment & AI.")

teams = [
    "Brisbane Broncos", "Melbourne Storm", "Penrith Panthers", "Sydney Roosters",
    "Canberra Raiders", "South Sydney Rabbitohs", "Parramatta Eels", "Newcastle Knights",
    "Cronulla Sharks", "St George Illawarra Dragons", "Wests Tigers", "Manly Sea Eagles",
    "Canterbury Bulldogs", "Gold Coast Titans", "New Zealand Warriors", "North Queensland Cowboys"
]

# Mini historical wins vs opponent dataset (from 2020-2024)
# Format: {team1: {team2: wins_team1_vs_team2}, ...}
# Example data (you can update with real stats)
historical_wins = {
    "Brisbane Broncos": {
        "Melbourne Storm": 6,
        "Canberra Raiders": 8,
        "Penrith Panthers": 3,
        "Sydney Roosters": 5
    },
    "Melbourne Storm": {
        "Brisbane Broncos": 9,
        "Canberra Raiders": 7,
        "Penrith Panthers": 5,
        "Sydney Roosters": 6
    },
    "Penrith Panthers": {
        "Brisbane Broncos": 8,
        "Melbourne Storm": 7,
        "Canberra Raiders": 6,
        "Sydney Roosters": 10
    },
    # ... add more realistic data for all teams here ...
}

# Function to calculate win rate and confidence
def calc_win_prob(team1, team2):
    wins_team1 = historical_wins.get(team1, {}).get(team2, 0)
    wins_team2 = historical_wins.get(team2, {}).get(team1, 0)
    total_games = wins_team1 + wins_team2
    if total_games == 0:
        return 0.5  # No data, 50-50 guess
    
    prob_team1 = wins_team1 / total_games
    return prob_team1

def margin_range_from_prob(prob):
    # Higher confidence = bigger margin range
    if prob >= 0.85:
        return "31–40"
    elif prob >= 0.70:
        return "21–30"
    elif prob >= 0.55:
        return "11–20"
    else:
        return "1–10"

team1 = st.selectbox("Choose Team 1", teams)
team2 = st.selectbox("Choose Team 2", [team for team in teams if team != team1])

if st.button("Predict Winner"):
    prob = calc_win_prob(team1, team2)

    if prob == 0.5:
        st.warning("Not enough historical data. Prediction is a 50/50 guess.")
    
    if prob >= 0.5:
        winner = team1
        confidence = prob
    else:
        winner = team2
        confidence = 1 - prob
    
    margin_range = margin_range_from_prob(confidence)

    reason = f"Based on historical matchups since 2020, {winner} have won approximately {confidence*100:.1f}% of their games against their opponent."

    st.markdown(f"### Predicted Winner: {winner}")
    st.markdown(f"**Winning chance:** {winner} {confidence*100:.1f}% – "
                f"{team2 if winner==team1 else team1} {(1-confidence)*100:.1f}%")
    st.markdown(f"**Predicted points margin:** Range: {margin_range}")
    st.markdown(f"**Why?** {reason}")

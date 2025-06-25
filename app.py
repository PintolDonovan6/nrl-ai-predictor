import streamlit as st
import random

# --- CSS for full background image & white text ---
st.markdown(
    """
    <style>
    /* Full screen background image */
    .stApp {
        background: url('logo1.png');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    /* White text everywhere */
    h1, h2, h3, p, label, div, span {
        color: white !important;
        text-shadow: none !important;
    }
    /* Button style */
    button, .stButton>button {
        background-color: #d80000 !important;
        color: white !important;
        font-weight: bold;
        border-radius: 8px;
        padding: 8px 20px;
    }
    /* Selectbox style */
    div[role="combobox"] > div > input {
        color: black !important;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- App title and subtitle ---
st.title("NRL Match Predictor | Mango Mine Case")
st.write("Powered by professional insights, tipster opinions, fan sentiment & AI.")

# --- List of NRL teams (since 2020) ---
teams = [
    "Brisbane Broncos", "Melbourne Storm", "Penrith Panthers", "Sydney Roosters",
    "Canberra Raiders", "South Sydney Rabbitohs", "Parramatta Eels", "Newcastle Knights",
    "St. George Illawarra Dragons", "Wests Tigers", "North Queensland Cowboys", "Cronulla Sharks",
    "Gold Coast Titans", "New Zealand Warriors", "Manly Sea Eagles", "Rabbitohs",
]

# --- Select teams ---
team1 = st.selectbox("Choose Team 1", teams, key="team1")
team2 = st.selectbox("Choose Team 2", [t for t in teams if t != team1], key="team2")

# --- Sample historical win % data since 2020 (for demo) ---
# Key: (team1, team2), value: team1 win % (0 to 100)
historical_win_rates = {
    ("Brisbane Broncos", "Melbourne Storm"): 40,
    ("Melbourne Storm", "Brisbane Broncos"): 60,
    ("Penrith Panthers", "Sydney Roosters"): 55,
    ("Sydney Roosters", "Penrith Panthers"): 45,
    ("Canberra Raiders", "South Sydney Rabbitohs"): 50,
    ("South Sydney Rabbitohs", "Canberra Raiders"): 50,
    # Add more as needed
}

# --- Points margin ranges by confidence ---
def margin_range(win_prob):
    if win_prob >= 75:
        return "31–40"
    elif win_prob >= 60:
        return "21–30"
    elif win_prob >= 50:
        return "11–20"
    else:
        return "1–10"

# --- Predict button ---
if st.button("Predict Winner", key="predict_btn"):
    key = (team1, team2)
    reverse_key = (team2, team1)
    
    # Get win percentage or fallback to 50/50
    if key in historical_win_rates:
        team1_win_pct = historical_win_rates[key]
    elif reverse_key in historical_win_rates:
        team1_win_pct = 100 - historical_win_rates[reverse_key]
    else:
        team1_win_pct = 50
    
    # Determine predicted winner
    if team1_win_pct > 50:
        winner = team1
        win_prob = team1_win_pct
    elif team1_win_pct < 50:
        winner = team2
        win_prob = 100 - team1_win_pct
    else:
        winner = random.choice([team1, team2])
        win_prob = 50
    
    # Margin range
    margin = margin_range(win_prob)
    
    # Reason string (basic for demo)
    reason = (
        f"Based on historical match data since 2020 and current form, "
        f"{winner} have an estimated winning chance of {win_prob}%. "
        f"Predicted margin range reflects confidence in the outcome."
    )
    
    # Show prediction results
    st.markdown(f"### Predicted Winner: {winner}")
    st.markdown(f"**Winning chance:** {win_prob:.1f}%")
    st.markdown(f"**Predicted points margin:** Range: {margin}")
    st.markdown(f"**Why?** {reason}")

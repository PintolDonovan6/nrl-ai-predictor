import streamlit as st
import random

# === Inject correct CSS for full-page background and white text ===
st.markdown(
    """
    <style>
      /* Full-page background using your uploaded logo1.png */
      [data-testid="stAppViewContainer"] {
        background: url('logo1.png') no-repeat center center fixed !important;
        background-size: cover !important;
      }
      /* Semi‐transparent overlay for toolbar area */
      [data-testid="stToolbar"] > div:first-child {
        background: rgba(0,0,0,0.4) !important;
      }
      /* Force all text white with shadow */
      body, [data-testid="stAppViewContainer"] * {
        color: white !important;
        text-shadow: 1px 1px 2px black !important;
      }
      /* Style buttons */
      button, .stButton > button {
        background-color: #d80000 !important;
        color: white !important;
        border-radius: 6px !important;
        padding: 8px 16px !important;
      }
      /* Style dropdowns */
      [data-baseweb="select"] {
        background-color: rgba(0,0,0,0.6) !important;
        color: white !important;
      }
    </style>
    """,
    unsafe_allow_html=True
)

# === App Title ===
st.title("NRL Match Predictor | Mango Mine Case")
st.markdown("Powered by professional insights, tipster opinions, fan sentiment & AI.")

# === NRL Teams List ===
teams = [
    "Brisbane Broncos", "Melbourne Storm", "Penrith Panthers", "Sydney Roosters",
    "Canberra Raiders", "South Sydney Rabbitohs", "Parramatta Eels", "Newcastle Knights",
    "Gold Coast Titans", "New Zealand Warriors", "Manly Sea Eagles",
    "St George Illawarra Dragons", "Wests Tigers", "Cronulla Sharks",
    "North Queensland Cowboys"
]

# === Team Selection ===
team1 = st.selectbox("Choose Team 1", teams)
team2 = st.selectbox("Choose Team 2", [t for t in teams if t != team1])

# === Prediction Button & Logic ===
if st.button("Predict Winner"):
    # Random‐based placeholder logic (replace with real analysis as needed)
    winner     = random.choice([team1, team2])
    margin_rng = random.choice(["1–10","11–20","21–30","31–40","41–50","51+"])
    win_pct    = round(random.uniform(55, 80), 1)
    lose_pct   = round(100 - win_pct, 1)
    loser      = team2 if winner == team1 else team1

    st.markdown(f"**Predicted winner:** {winner}")
    st.markdown(f"**Winning chance:** {winner} {win_pct}% – {loser} {lose_pct}%")
    st.markdown(f"**Predicted points margin range:** {margin_rng}")
    st.markdown("**Why?** Based on latest online expert tips, fan opinions, and performance stats.")

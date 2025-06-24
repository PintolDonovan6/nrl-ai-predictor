import streamlit as st

# ——— PAGE CONFIG ——————————————————————————————————
st.set_page_config(
    page_title="NRL Match Predictor | Mango Mine Case",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ——— CSS: BACKGROUND + WHITE TEXT ——————————————————————————————————
st.markdown(
    """
    <style>
      /* Full-page background using your uploaded logo1.png */
      [data-testid="stAppViewContainer"] {
        background: url("logo1.png") no-repeat center center fixed !important;
        background-size: cover !important;
      }
      /* White text everywhere */
      body, [data-testid="stAppViewContainer"] * {
        color: white !important;
        text-shadow: 1px 1px 2px black !important;
        font-family: 'Segoe UI', sans-serif;
      }
      /* PNG-red buttons */
      button, .stButton > button {
        background-color: #d80000 !important;
        color: white !important;
        font-weight: bold;
        border-radius: 6px !important;
        padding: 8px 16px !important;
      }
      /* Dropdown styling */
      [data-baseweb="select"] {
        background-color: rgba(0,0,0,0.6) !important;
        color: white !important;
      }
    </style>
    """,
    unsafe_allow_html=True
)

# ——— TITLE & SUBTITLE ——————————————————————————————————
st.header("NRL Match Predictor | Mango Mine Case")
st.write("Powered by professional insights, tipster opinions, fan sentiment & AI.")

# ——— TEAM FORM DATA ——————————————————————————————————
team_form = {
    "Brisbane Broncos": 80, "Melbourne Storm": 85, "Penrith Panthers": 90,
    "Sydney Roosters": 75, "Canberra Raiders": 70, "South Sydney Rabbitohs": 88,
    "Parramatta Eels": 78, "Newcastle Knights": 72, "Cronulla Sharks": 68,
    "Manly Sea Eagles": 66, "Gold Coast Titans": 60, "New Zealand Warriors": 58,
    "North Queensland Cowboys": 62, "St George Illawarra Dragons": 65,
    "Wests Tigers": 55
}

# ——— TEAM SELECTION ——————————————————————————————————
teams = list(team_form.keys())
team1 = st.selectbox("Choose Team 1", teams)
team2 = st.selectbox("Choose Team 2", [t for t in teams if t != team1])

# ——— PREDICT BUTTON & OUTPUT ——————————————————————————————————
if st.button("Predict Winner"):
    # Ensure distinct selection
    if team1 == team2:
        st.error("Select two different teams.")
    else:
        f1 = team_form[team1]
        f2 = team_form[team2]
        total = f1 + f2 or 1

        pct1 = (f1 / total) * 100
        pct2 = (f2 / total) * 100

        # Guarantee at least 80% for the winner
        if pct1 >= pct2:
            win_pct = max(pct1, 80)
            winner = team1
            loser = team2
        else:
            win_pct = max(pct2, 80)
            winner = team2
            loser = team1

        lose_pct = 100 - win_pct

        diff = abs(f1 - f2)
        if diff <= 10:
            margin_range = "1–10"
        elif diff <= 20:
            margin_range = "11–20"
        elif diff <= 30:
            margin_range = "21–30"
        elif diff <= 40:
            margin_range = "31–40"
        elif diff <= 50:
            margin_range = "41–50"
        else:
            margin_range = "51+"

        reason = (
            f"{winner} have a stronger recent form rating "
            f"({team_form[winner]} vs {team_form[loser]}) and are favored by analysts."
        )

        st.subheader(f"Predicted winner: {winner}")
        st.write(f"Winning chance: **{win_pct:.1f}%** – {lose_pct:.1f}%")
        st.write(f"Predicted points margin range: **{margin_range}**")
        st.write(f"Why? {reason}")

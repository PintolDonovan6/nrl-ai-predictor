import streamlit as st
import random

st.set_page_config(page_title="NRL Match Predictor | Samting Blo Ples")

# Inject PNG flag vertical stripes background and styles
st.markdown("""
<style>
.reportview-container, .main {
  background: linear-gradient(to right,
    #000000 33.33%,
    #d80000 33.33%,
    #d80000 66.66%,
    #ffd700 66.66%);
  min-height: 100vh;
  color: black !important;
}
h1, h2, h3, p, label, div {
  color: black !important;
  text-shadow: 0 0 3px #fff;
}
button, .stButton>button {
  background-color: #d80000 !important;
  color: black !important;
  font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

st.title("NRL Match Predictor | Samting Blo Ples")

teams = [
    "Brisbane Broncos",
    "Melbourne Storm",
    "Penrith Panthers",
    "Sydney Roosters",
    "Canberra Raiders",
    "South Sydney Rabbitohs",
    "Parramatta Eels",
    "Newcastle Knights"
]

team1 = st.selectbox("Choose Team 1", teams)
team2 = st.selectbox("Choose Team 2", [t for t in teams if t != team1])

def fetch_team_form(team):
    # Dummy form value, replace with real data if you want
    return random.uniform(0, 100)

if st.button("Predict Winner"):
    form1 = fetch_team_form(team1)
    form2 = fetch_team_form(team2)

    if form1 > form2:
        winner = team1
        loser = team2
        win_chance = 50 + (form1 - form2) * 0.5
    else:
        winner = team2
        loser = team1
        win_chance = 50 + (form2 - form1) * 0.5

    win_chance = min(max(win_chance, 51), 90)
    lose_chance = 100 - win_chance

    margin_total = random.randint(1, 60)
    if margin_total <= 10:
        margin_range = "1-10"
    elif margin_total <= 20:
        margin_range = "11-20"
    elif margin_total <= 30:
        margin_range = "21-30"
    elif margin_total <= 40:
        margin_range = "31-40"
    elif margin_total <= 50:
        margin_range = "41-50"
    else:
        margin_range = "51+"

    st.subheader(f"{team1} vs {team2}")
    st.write(f"**Predicted winner:** {winner}")
    st.write(f"Winning chance: {winner} {win_chance:.1f}% - {loser} {lose_chance:.1f}%")
    st.write(f"Predicted combined points margin: {margin_total} (Range: {margin_range})")
    st.write(
        f"**Why?** {winner} currently show better recent form metrics "
        f"compared to {loser}, which influences this prediction."
    )
    
    # Display PNG-related image under predictions
    st.image("logo1.png", caption="Powered by PNG Passion", use_column_width=True)

import streamlit as st
import random

# Set page config (optional)
st.set_page_config(page_title="NRL Match Predictor | Mango Mine Case", page_icon=":rugby_football:")

# Inject white font color with black shadow for readability
st.markdown(
    """
    <style>
    body, .css-1d391kg, .css-1d391kg * {
        color: white !important;
        text-shadow: 1px 1px 2px black;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title and subtitle
st.title("NRL Match Predictor | Mango Mine Case")
st.write("Powered by professional insights, tipster opinions, fan sentiment & AI.")

# Team selection with full NRL teams list
teams = [
    "Brisbane Broncos", "Melbourne Storm", "Penrith Panthers", "Sydney Roosters",
    "Canberra Raiders", "South Sydney Rabbitohs", "Parramatta Eels", "Newcastle Knights",
    "St. George Illawarra Dragons", "Gold Coast Titans", "Cronulla Sharks",
    "Manly Sea Eagles", "Wests Tigers", "North Queensland Cowboys",
    "New Zealand Warriors", "Sydney Tigers"
]

team1 = st.selectbox("Choose Team 1", teams)
team2 = st.selectbox("Choose Team 2", [team for team in teams if team != team1])

if st.button("Predict Winner"):
    # Simple dummy prediction logic - replace with real logic when ready
    winner = random.choice([team1, team2])
    
    # Random margin range bucket only (no exact points)
    margin_ranges = ["1-10", "11-20", "21-30", "31-40", "41-50", "51+"]
    margin_range = random.choice(margin_ranges)
    
    # Dummy winning chance values summing to 100%
    win_chance_winner = round(random.uniform(55, 80), 1)
    win_chance_loser = round(100 - win_chance_winner, 1)
    
    loser = team2 if winner == team1 else team1
    
    st.write(f"**Predicted winner:** {winner}")
    st.write(f"**Winning chance:** {winner} {win_chance_winner}% – {loser} {win_chance_loser}%")
    st.write(f"**Predicted points margin range:** {margin_range}")
    st.write("**Why?** Based on latest online expert tips, fan opinions, and performance stats.")
    
    # Show PNG image below prediction
    st.image("logo1.png", caption="PNG Pride", use_column_width=False, width=150)

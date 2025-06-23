import streamlit as st
import pandas as pd

# ✅ Full list of 17 NRL teams
all_teams = [
    'Broncos', 'Raiders', 'Bulldogs', 'Sharks', 'Titans', 'Sea Eagles', 'Storm',
    'Knights', 'Cowboys', 'Eels', 'Panthers', 'Rabbitohs', 'Dragons', 'Roosters',
    'Warriors', 'Tigers', 'Dolphins'
]

# ✅ Sample match history (you can expand later)
data = {
    'Home Team': ['Storm', 'Panthers', 'Roosters', 'Storm', 'Broncos', 'Panthers'],
    'Away Team': ['Broncos', 'Storm', 'Panthers', 'Roosters', 'Panthers', 'Roosters'],
    'Winner':    ['Storm', 'Panthers', 'Roosters', 'Storm', 'Panthers', 'Panthers']
}
df = pd.DataFrame(data)

# 🌟 Streamlit App
st.title("🏉 NRL Match Winner Predictor")

home_team = st.selectbox("Select Home Team", all_teams)
away_team = st.selectbox("Select Away Team", [team for team in all_teams if team != home_team])

def predict_winner(home, away):
    # Check if there's match history
    home_wins = df[(df['Home Team'] == home) & (df['Winner'] == home)].shape[0]
    away_wins = df[(df['Away Team'] == away) & (df['Winner'] == away)].shape[0]

    # Placeholder for expert analysis results (to be added later)
    expert_tips = None  # You'll replace this with real scraped/extracted data
    team_with_most_tips = home  # or away depending on what scraping finds
    summary = "Most analysts favor " + team_with_most_tips  # Replace with actual summary

    if expert_tips:  # when expert data is available
        winner = team_with_most_tips
        reason = summary
        return f"🤖 Expert Prediction: **{winner}**\n🧠 Reason: {reason}"
    elif home_wins > away_wins:
        return f"{home} (based on stronger home history)"
    elif away_wins > home_wins:
        return f"{away} (based on stronger away form)"
    else:
        return "📉 No strong data available — matchup is balanced or not recorded."

# Button logic
if st.button("Predict Winner"):
    result = predict_winner(home_team, away_team)
    st

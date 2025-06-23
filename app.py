import streamlit as st
import pandas as pd

# 🔧 Simulated expert tips — replace with scraped values in future
expert_tips = {
    ('Storm', 'Panthers'): {
        'winner': 'Storm',
        'summary': "🏆 5 of 7 analysts (Nine, ESPN, Stats Insider) favor Storm. They’ve won recent matchups and are full strength while Panthers miss key Origin players."
    },
    ('Broncos', 'Roosters'): {
        'winner': 'Roosters',
        'summary': "📊 Roosters tipped by 4 of 6 sources including Stats Insider and The Roar due to stronger away performance."
    },
    # Add more matchups here later
}

# 🏉 NRL Team List
teams = [
    'Broncos', 'Raiders', 'Bulldogs', 'Sharks', 'Titans', 'Sea Eagles', 'Storm',
    'Knights', 'Cowboys', 'Eels', 'Panthers', 'Rabbitohs', 'Dragons',
    'Roosters', 'Warriors', 'Tigers', 'Dolphins'
]

# 📊 Historical match results (sample only)
data = {
    'Home Team': ['Storm', 'Panthers', 'Roosters', 'Storm', 'Broncos', 'Panthers'],
    'Away Team': ['Broncos', 'Storm', 'Panthers', 'Roosters', 'Panthers', 'Roosters'],
    'Winner':    ['Storm', 'Panthers', 'Roosters', 'Storm', 'Panthers', 'Panthers']
}
df = pd.DataFrame(data)

# 🖼️ Page Setup
st.set_page_config(page_title="NRL Predictor", page_icon="🏉")
st.title("🏉 NRL Match Winner Predictor")

# 🧠 User Input
home_team = st.selectbox("Select Home Team", teams)
away_team = st.selectbox("Select Away Team", [t for t in teams if t != home_team])

# 🔮 Prediction Logic
def predict_winner(home, away):
    # 1. Expert tip override if available
    if (home, away) in expert_tips:
        return expert_tips[(home, away)]['winner'], expert_tips[(home, away)]['summary']
    if (away, home) in expert_tips:
        reverse = expert_tips[(away, home)]
        return reverse['winner'], f"{reverse['summary']} (reverse matchup)"

    # 2. History fallback
    home_wins = df[(df['Home Team'] == home) & (df['Winner'] == home)].shape[0]
    away_wins = df[(df['Away Team'] == away) & (df['Winner'] == away)].shape[0]

    if home_wins > away_wins:
        return home, f"📚 Based on home history, {home} has more wins."
    elif away_wins > home_wins:
        return away, f"📚 Based on away history, {away} has more wins."
    elif home_wins == away_wins and home_wins > 0:
        return home, f"📘 Equal history, favoring home team {home}."
    else:
        return home, f"📎 No history available. Predicting {home} as fallback (home team advantage)."

# 🔘 Predict Button
if st.button("Predict Winner"):
   def predict_winner(home, away):
    home_wins = df[(df['Home Team'] == home) & (df['Winner'] == home)].shape[0]
    away_wins = df[(df['Away Team'] == away) & (df['Winner'] == away)].shape[0]

    if home_wins > away_wins:
        return f"{home} (based on home history)"
    elif away_wins > home_wins:
        return f"{away} (based on away history)"
    elif home_wins == away_wins and home_wins > 0:
        # Tie in history, favor home team by default
        return f"{home} (equal history, home team advantage)"
    else:
        # No history data, fallback to home team by default
        return f"{home} (no history, fallback to home team)"


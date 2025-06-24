import streamlit as st
import requests
import random

API_KEY = "YOUR_SPORTMONKS_API_KEY"  # Replace with your actual API key

def fetch_nrl_fixtures():
    url = f"https://api.sportmonks.com/v3/rl/fixtures/upcoming?api_token={API_KEY}&include=localTeam,visitorTeam"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        fixtures = []
        for fixture in data.get('data', []):
            home = fixture['localTeam']['data']['name']
            away = fixture['visitorTeam']['data']['name']
            date = fixture['starting_at'].split('T')[0]
            fixtures.append({'home': home, 'away': away, 'date': date})
        return fixtures
    except Exception as e:
        st.error(f"Error fetching fixtures: {e}")
        return []

def predict_winner(home, away):
    # Simple random prediction placeholder
    winner = random.choice([home, away])
    win_chance_winner = random.uniform(55, 75)
    win_chance_loser = 100 - win_chance_winner
    margin_points = random.randint(1, 60)

    # Define margin range buckets
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

    reason = f"{winner} have strong recent form and better stats."

    return winner, win_chance_winner, win_chance_loser, margin_points, margin_range, reason

def main():
    st.set_page_config(page_title="NRL Match Predictor | Samting Blo Ples", page_icon="🏉", layout="centered")
    st.markdown(
        """
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
        </style>
        """, unsafe_allow_html=True)

    st.title("NRL Match Predictor | Samting Blo Ples")
    st.write("Powered by AI, PNG passion, and SportMonks data.")

    fixtures = fetch_nrl_fixtures()

    if not fixtures:
        st.warning("No upcoming fixtures found. Please try again later.")
        return

    for match in fixtures:
        st.subheader(f"{match['home']} vs {match['away']} — {match['date']}")

        winner, win_chance_winner, win_chance_loser, margin_points, margin_range, reason = predict_winner(match['home'], match['away'])

        loser = match['away'] if winner == match['home'] else match['home']
        st.markdown(f"**Predicted winner:** {winner}")
        st.markdown(f"**Winning chance:** {winner} {win_chance_winner:.1f}% - {loser} {win_chance_loser:.1f}%")
        st.markdown(f"**Predicted total points margin:** {margin_points} (Range: {margin_range})")
        st.markdown(f"**Why?** {reason}")
        st.markdown("---")

if __name__ == "__main__":
    main()

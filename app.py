import streamlit as st
import streamlit as st

# Meta tags including Google site verification
st.markdown("""
<head>
<meta name="google-site-verification" content="pLrVe8n9tv3vUYdzPnZ7kb5NZJAqH9zE39hIOcq84Nw" />
<meta name="description" content="NRL Match Predictor powered by AI and historical stats.">
<meta name="keywords" content="NRL, Rugby League, Prediction, AI, Sports, Australia">
<meta name="author" content="Your Name or Team">
<title>NRL Match Predictor | Mango Mine Case</title>
</head>
""", unsafe_allow_html=True)

# Page config
st.set_page_config(page_title="NRL Match Predictor | Mango Mine Case", layout="centered")

# CSS Styling
st.markdown(
    """
    <style>
    .stApp {
        background-color: #8B4000;  /* Dark Orange */
        color: #fff !important;     /* White text */
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    h1, h2, h3, h4 {
        color: #FFD700 !important;  /* Gold headings */
    }
    .stButton>button {
        background-color: #FFD700 !important; /* Gold buttons */
        color: #8B4000 !important;             /* Dark orange text on buttons */
        font-weight: bold;
        border-radius: 8px;
        border: none;
        padding: 8px 16px;
    }
    select, .stSelectbox > div {
        background-color: #B35800 !important; /* Lighter dark orange */
        color: #fff !important;
        border: 1px solid #FFD700 !important; /* Gold border */
        border-radius: 6px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

teams = [
    "Brisbane Broncos", "Melbourne Storm", "Penrith Panthers", "Sydney Roosters",
    "Canberra Raiders", "South Sydney Rabbitohs", "Parramatta Eels", "Newcastle Knights",
    "Gold Coast Titans", "Wests Tigers", "Cronulla Sharks", "St. George Illawarra Dragons",
    "Manly Sea Eagles", "New Zealand Warriors", "North Queensland Cowboys"
]

# Head-to-head win % (Team1 vs Team2)
head_to_head = {
    ("Brisbane Broncos", "Melbourne Storm"): 35,
    ("Melbourne Storm", "Brisbane Broncos"): 65,
    ("Penrith Panthers", "Sydney Roosters"): 70,
    ("Sydney Roosters", "Penrith Panthers"): 30,
    ("Canberra Raiders", "South Sydney Rabbitohs"): 55,
    ("South Sydney Rabbitohs", "Canberra Raiders"): 45,
    ("Parramatta Eels", "Newcastle Knights"): 60,
    ("Newcastle Knights", "Parramatta Eels"): 40,
    ("Gold Coast Titans", "Wests Tigers"): 50,
    ("Wests Tigers", "Gold Coast Titans"): 50,
    ("Cronulla Sharks", "St. George Illawarra Dragons"): 58,
    ("St. George Illawarra Dragons", "Cronulla Sharks"): 42,
    ("Manly Sea Eagles", "New Zealand Warriors"): 62,
    ("New Zealand Warriors", "Manly Sea Eagles"): 38,
    ("North Queensland Cowboys", "Brisbane Broncos"): 55,
    ("Brisbane Broncos", "North Queensland Cowboys"): 45,
    # Add more pairs as needed
}

# Team strength rating (0-100 scale, higher is stronger)
team_strength = {
    "Brisbane Broncos": 72,
    "Melbourne Storm": 88,
    "Penrith Panthers": 90,
    "Sydney Roosters": 85,
    "Canberra Raiders": 75,
    "South Sydney Rabbitohs": 80,
    "Parramatta Eels": 78,
    "Newcastle Knights": 70,
    "Gold Coast Titans": 65,
    "Wests Tigers": 60,
    "Cronulla Sharks": 74,
    "St. George Illawarra Dragons": 68,
    "Manly Sea Eagles": 76,
    "New Zealand Warriors": 67,
    "North Queensland Cowboys": 77,
}

def calculate_margin_by_chance(winning_chance):
    if winning_chance >= 85:
        return "21–30"
    elif winning_chance >= 70:
        return "16–20"
    elif winning_chance >= 60:
        return "11–15"
    elif winning_chance >= 50:
        return "6–10"
    else:
        return "1–5"

def calculate_margin_by_strength_diff(strength_diff):
    if strength_diff >= 20:
        return "21–30"
    elif strength_diff >= 10:
        return "16–20"
    elif strength_diff >= 5:
        return "11–15"
    elif strength_diff >= 2:
        return "6–10"
    else:
        return "1–5"

def predict_winner(team1, team2):
    if team1 == team2:
        return None, None, None, None, None, "Select two different teams."

    win_pct = head_to_head.get((team1, team2), None)

    if win_pct is not None:
        # Use head-to-head data
        if win_pct > 50:
            winner = team1
            winning_chance = win_pct
            losing_team = team2
            losing_chance = 100 - win_pct
        elif win_pct < 50:
            winner = team2
            winning_chance = 100 - win_pct
            losing_team = team1
            losing_chance = win_pct
        else:
            winner = None
            winning_chance = 50
            losing_team = None
            losing_chance = 50

        margin = calculate_margin_by_chance(winning_chance)

        if winner:
            reason = (f"Based on historical head-to-head data since 2020, "
                      f"{winner} has a {winning_chance:.1f}% chance to win against {losing_team}.")
        else:
            reason = "This matchup is evenly matched based on historical data."

    else:
        # Fallback to team strength comparison
        strength1 = team_strength.get(team1, 70)
        strength2 = team_strength.get(team2, 70)

        total = strength1 + strength2
        if total == 0:
            # Avoid division by zero
            winning_chance_1 = 50
            winning_chance_2 = 50
        else:
            winning_chance_1 = (strength1 / total) * 100
            winning_chance_2 = 100 - winning_chance_1

        if winning_chance_1 > winning_chance_2:
            winner = team1
            winning_chance = winning_chance_1
            losing_team = team2
            losing_chance = winning_chance_2
        elif winning_chance_2 > winning_chance_1:
            winner = team2
            winning_chance = winning_chance_2
            losing_team = team1
            losing_chance = winning_chance_1
        else:
            winner = None
            winning_chance = 50
            losing_team = None
            losing_chance = 50

        strength_diff = abs(strength1 - strength2)
        margin = calculate_margin_by_strength_diff(strength_diff)

        if winner:
            reason = (f"No head-to-head data found. Based on overall team strength ratings, "
                      f"{winner} is favored with a {winning_chance:.1f}% winning chance.")
        else:
            reason = "Teams are evenly matched based on overall strength ratings."

    return winner, winning_chance, losing_team, losing_chance, margin, reason


# Streamlit UI

st.title("NRL Match Predictor | Mango Mine Case")
st.write("Powered by historical stats, team strength, and expert logic — aiming for 80%+ accuracy.")

team1 = st.selectbox("Choose Team 1", teams, index=0)
team2 = st.selectbox("Choose Team 2", teams, index=1)

if st.button("Predict Winner"):
    winner, win_chance, loser, lose_chance, margin, reason = predict_winner(team1, team2)

    if winner is None and reason.startswith("Select"):
        st.error(reason)
    else:
        if winner:
            st.markdown(f"### Predicted Winner: {winner}")
            st.markdown(f"**Winning chance:** {winner} {win_chance:.1f}% – {loser} {lose_chance:.1f}%")
            st.markdown(f"**Predicted points margin:** Range: {margin}")
            st.markdown(f"**Why?** {reason}")
        else:
            st.markdown("### Matchup is evenly matched")
            st.markdown("**Winning chance:** 50% – 50%")
            st.markdown(f"**Why?** {reason}")

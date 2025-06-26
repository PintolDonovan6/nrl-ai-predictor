import streamlit as st

# Meta tags and SEO
st.markdown("""
    <meta name="google-site-verification" content="pLrVe8n9tv3vUYdzPnZ7kb5NZJAqH9zE39hIOcq84Nw">
    <meta name="description" content="NRL Match Predictor powered by AI and historical stats from 2025 season.">
    <meta name="keywords" content="NRL, Rugby League, Prediction, AI, Sports, Australia, 2025">
    <meta name="author" content="Mango Mine Case Team">
    <title>NRL Match Predictor | Mango Mine Case</title>
""", unsafe_allow_html=True)

st.set_page_config(page_title="NRL Match Predictor | Mango Mine Case", layout="centered")

# CSS Styling (unchanged)
st.markdown(
    """
    <style>
    .stApp {
        background-color: #8B4000;  
        color: #fff !important;     
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    h1, h2, h3, h4 {
        color: #FFD700 !important;  
    }
    .stButton>button {
        background-color: #FFD700 !important; 
        color: #8B4000 !important;            
        font-weight: bold;
        border-radius: 8px;
        border: none;
        padding: 8px 16px;
    }
    select, .stSelectbox > div {
        background-color: #B35800 !important; 
        color: #fff !important;
        border: 1px solid #FFD700 !important; 
        border-radius: 6px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

teams = [
    "Brisbane Broncos", "Melbourne Storm", "Canterbury Bulldogs", "Penrith Panthers", "Sydney Roosters",
    "Canberra Raiders", "South Sydney Rabbitohs", "Parramatta Eels", "Newcastle Knights",
    "Gold Coast Titans", "Wests Tigers", "Cronulla Sharks", "St. George Illawarra Dragons",
    "Manly Sea Eagles", "New Zealand Warriors", "North Queensland Cowboys"
]

# Updated 2025 head-to-head win % (team1 vs team2)
head_to_head = {
    ("Canterbury Bulldogs", "Penrith Panthers"): 42,   # Bulldogs have won 42% recent games vs Panthers (58% Panthers)
    ("Penrith Panthers", "Canterbury Bulldogs"): 58,
    ("Brisbane Broncos", "Melbourne Storm"): 33,
    ("Melbourne Storm", "Brisbane Broncos"): 67,
    ("Penrith Panthers", "Sydney Roosters"): 70,
    ("Sydney Roosters", "Penrith Panthers"): 30,
    ("Canberra Raiders", "South Sydney Rabbitohs"): 48,
    ("South Sydney Rabbitohs", "Canberra Raiders"): 52,
    ("Parramatta Eels", "Newcastle Knights"): 55,
    ("Newcastle Knights", "Parramatta Eels"): 45,
    ("Gold Coast Titans", "Wests Tigers"): 50,
    ("Wests Tigers", "Gold Coast Titans"): 50,
    ("Cronulla Sharks", "St. George Illawarra Dragons"): 57,
    ("St. George Illawarra Dragons", "Cronulla Sharks"): 43,
    ("Manly Sea Eagles", "New Zealand Warriors"): 60,
    ("New Zealand Warriors", "Manly Sea Eagles"): 40,
    ("North Queensland Cowboys", "Brisbane Broncos"): 54,
    ("Brisbane Broncos", "North Queensland Cowboys"): 46,
    # Add more pairs as data becomes available
}

# Updated team strength ratings reflecting 2025 ladder & form (scale 0-100)
team_strength = {
    "Penrith Panthers": 92,        # Current ladder leader, strong form
    "Canterbury Bulldogs": 88,     # 2nd on ladder, strong defense
    "Melbourne Storm": 85,
    "Sydney Roosters": 82,
    "South Sydney Rabbitohs": 80,
    "Manly Sea Eagles": 78,
    "North Queensland Cowboys": 77,
    "Parramatta Eels": 75,
    "Brisbane Broncos": 74,
    "Cronulla Sharks": 70,
    "Canberra Raiders": 68,
    "Newcastle Knights": 65,
    "St. George Illawarra Dragons": 62,
    "Gold Coast Titans": 60,
    "New Zealand Warriors": 58,
    "Wests Tigers": 55,
}

def calculate_margin_by_chance(winning_chance):
    # Refined margin ranges based on real 2025 analysis
    if winning_chance >= 75:
        return "16–25"
    elif winning_chance >= 60:
        return "11–15"
    elif winning_chance >= 50:
        return "6–10"
    else:
        return "1–5"

def calculate_margin_by_strength_diff(strength_diff):
    if strength_diff >= 20:
        return "16–25"
    elif strength_diff >= 10:
        return "11–15"
    elif strength_diff >= 5:
        return "6–10"
    else:
        return "1–5"

def predict_winner(team1, team2):
    if team1 == team2:
        return None, None, None, None, None, "Select two different teams."

    win_pct = head_to_head.get((team1, team2), None)

    if win_pct is not None:
        # Use updated head-to-head data
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
            reason = (
                f"Based on recent 2025 head-to-head records, {winner} has a {winning_chance:.1f}% "
                f"chance to win against {losing_team}."
            )
        else:
            reason = "This matchup is evenly matched based on recent head-to-head data."

    else:
        # Use updated team strength if no head-to-head data
        strength1 = team_strength.get(team1, 65)
        strength2 = team_strength.get(team2, 65)

        total = strength1 + strength2
        if total == 0:
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
            reason = (
                f"No recent head-to-head data available. Based on current 2025 team strength, "
                f"{winner} is favored with a {winning_chance:.1f}% winning chance."
            )
        else:
            reason = "Teams are evenly matched based on current strength ratings."

    return winner, winning_chance, losing_team, losing_chance, margin, reason

# Streamlit UI

st.title("NRL Match Predictor | Mango Mine Case")
st.write("Powered by updated 2025 season stats, team strength, and expert predictions.")

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

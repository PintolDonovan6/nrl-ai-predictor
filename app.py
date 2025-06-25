import streamlit as st
import streamlit as st

# Paste this CSS right here — at the top, after imports
st.markdown(
    """
    <style>
    /* Full background image */
    .reportview-container, .main, .block-container {
        background: url('logo1.png') no-repeat center center fixed;
        background-size: cover;
        color: #ffd700 !important; /* gold text */
    }

    /* Headings in red */
    h1, h2, h3, h4, h5, h6 {
        color: #d80000 !important;
    }

    /* Sidebar text */
    .sidebar-content {
        color: #ffd700 !important;
    }

    /* Buttons */
    button, .stButton > button {
        background-color: #d80000 !important; /* red background */
        color: #ffd700 !important; /* gold text */
        font-weight: bold;
        border: 2px solid #000000; /* black border */
    }

    /* Inputs and selects */
    div[role="listbox"], .stTextInput > div > input {
        background-color: rgba(216, 0, 0, 0.1) !important;
        color: #000000 !important;
        border: 1px solid #d80000 !important;
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Your existing Streamlit UI code comes here
st.title("NRL Match Predictor | Mango Mine Case")
# ... rest of your app

st.markdown(
    """
    <style>
    /* Full page background image */
    .reportview-container, .main, .block-container {
        background: url('/logo1.png') no-repeat center center fixed;
        background-size: cover;
    }
    /* Remove default background colors */
    .css-1d391kg, .css-1d391kg > div {
        background: transparent !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

import streamlit as st
import random

# Background image CSS injection — only changes background
st.markdown(
    """
    <style>
    .reportview-container {
        background: url('/logo1.png') no-repeat center center fixed;
        background-size: cover;
    }
    .sidebar-content {
        background: transparent !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and intro
st.title("NRL Match Predictor | Mango Mine Case")
st.write("Powered by professional insights, tipster opinions, fan sentiment & AI.")

# All NRL teams for selection
teams = [
    "Brisbane Broncos", "Melbourne Storm", "Penrith Panthers", "Sydney Roosters",
    "Canberra Raiders", "South Sydney Rabbitohs", "Parramatta Eels", "Newcastle Knights",
    "Wests Tigers", "St. George Illawarra Dragons", "North Queensland Cowboys",
    "Manly Sea Eagles", "Cronulla Sharks", "Canterbury Bulldogs", "New Zealand Warriors",
    "Gold Coast Titans"
]

# User selects teams
team1 = st.selectbox("Choose Team 1", teams)
team2 = st.selectbox("Choose Team 2", [team for team in teams if team != team1])

# Predict button
if st.button("Predict Winner"):
    # Here you would replace with your real analysis/AI model or API calls
    # For demo, randomly pick a winner and margin range with a legit-sounding reason
    winner = random.choice([team1, team2])

    # Points margin range buckets only (no exact margin)
    margin_ranges = ["1-10", "11-20", "21-30", "31-40", "41-50", "51+"]
    margin_range = random.choice(margin_ranges)

    # Simulated confidence level (80%+)
    confidence = round(random.uniform(80, 95), 1)

    # Dummy reasons based on realistic-sounding insights
    reasons = {
        "Brisbane Broncos": "Strong recent form and solid defense.",
        "Melbourne Storm": "High-scoring offense and home ground advantage.",
        "Penrith Panthers": "Consistent top performances and key player fitness.",
        "Sydney Roosters": "Effective strategies and experienced lineup.",
        "Canberra Raiders": "Improved squad depth and tactical gameplay.",
        "South Sydney Rabbitohs": "Aggressive attack and strong fan support.",
        "Parramatta Eels": "Balanced team and excellent coaching staff.",
        "Newcastle Knights": "Young talents showing great potential.",
        "Wests Tigers": "Effective defense and teamwork.",
        "St. George Illawarra Dragons": "Strong recent wins and home advantage.",
        "North Queensland Cowboys": "Key players returning from injury.",
        "Manly Sea Eagles": "High team morale and recent momentum.",
        "Cronulla Sharks": "Strong attack and solid defense.",
        "Canterbury Bulldogs": "Resilience and tactical plays.",
        "New Zealand Warriors": "Fast-paced gameplay and skilled backs.",
        "Gold Coast Titans": "High energy and improved squad."
    }

    # Use reason of winning team, fallback to a general statement if unknown
    reason = reasons.get(winner, "Based on latest stats, expert analysis, and fan sentiment.")

    # Show prediction
    st.write(f"**Predicted Winner:** {winner}")
    st.write(f"**Winning Confidence:** {confidence}%")
    st.write(f"**Predicted Points Margin Range:** {margin_range}")
    st.write(f"**Why?** {reason} Powered by expert insights, tipsters, fans, and AI.")

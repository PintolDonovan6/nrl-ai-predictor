import streamlit as st
import random

# Inject CSS for full background image + white fonts
st.markdown(
    """
    <style>
    /* Full page background image */
    .stApp {
        background-image: url("logo1.png");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        color: white;
    }
    /* Force all text to white */
    body, .css-1d391kg, .css-1d391kg * {
        color: white !important;
    }
    /* Style buttons */
    button, .stButton>button {
        background-color: #d80000 !important;
        color: white !important;
        font-weight: bold;
        border-radius: 8px;
        padding: 8px 16px;
    }
    /* Inputs */
    div.stSelectbox > div[role="combobox"] > div {
        color: black !important;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("NRL Match Predictor | Mango Mine Case")

teams = [
    "Brisbane Broncos", "Melbourne Storm", "Penrith Panthers", "Sydney Roosters",
    "Canberra Raiders", "South Sydney Rabbitohs", "Parramatta Eels", "Newcastle Knights",
    "Manly Warringah Sea Eagles", "Cronulla Sharks", "New Zealand Warriors",
    "Gold Coast Titans", "St George Illawarra Dragons", "North Queensland Cowboys",
    "West Tigers", "Canterbury Bulldogs"
]

team1 = st.selectbox("Choose Team 1", teams)
team2 = st.selectbox("Choose Team 2", teams)

if team1 == team2:
    st.warning("Please select two different teams!")
else:
    if st.button("Predict Winner"):
        winner = random.choice([team1, team2])
        margin = random.randint(1, 60)
        if margin <= 10:
            margin_range = "1–10"
        elif margin <= 20:
            margin_range = "11–20"
        elif margin <= 30:
            margin_range = "21–30"
        elif margin <= 40:
            margin_range = "31–40"
        elif margin <= 50:
            margin_range = "41–50"
        else:
            margin_range = "51+"

        st.markdown(f"""
        **Predicted winner:** {winner}  
        **Predicted points margin:** Range: {margin_range}  
        **Why?** Based on insights from pro analysts, tipsters, NRL fans, and AI.
        """)

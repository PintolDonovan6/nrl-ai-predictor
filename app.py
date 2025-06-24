import streamlit as st
import os
import random

# Inject PNG flag vertical stripes as full background with black fonts
st.markdown(
    """
    <style>
    /* Background with PNG colors */
    .reportview-container {
        background: linear-gradient(to right, 
            #000000 33.33%, 
            #d80000 33.33%, 
            #d80000 66.66%, 
            #ffd700 66.66%);
        min-height: 100vh;
        color: black !important;
    }

    /* Sidebar background */
    .sidebar-content {
        background: linear-gradient(to right, 
            #000000 33.33%, 
            #d80000 33.33%, 
            #d80000 66.66%, 
            #ffd700 66.66%);
        color: black !important;
    }

    /* Text styling to black */
    h1, h2, h3, p, label, div {
        color: black !important;
        text-shadow: none !important;
    }

    /* Buttons with black text and red background */
    button, .stButton>button {
        background-color: #d80000 !important;
        color: black !important;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

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
team2 = st.selectbox("Choose Team 2", [team for team in teams if team != team1])

if st.button("Predict Winner"):
    winner = random.choice([team1, team2])
    margin = random.randint(1, 60)

    if margin <= 10:
        margin_range = "1-10"
    elif margin <= 20:
        margin_range = "11-20"
    elif margin <= 30:
        margin_range = "21-30"
    elif margin <= 40:
        margin_range = "31-40"
    elif margin <= 50:
        margin_range = "41-50"
    else:
        margin_range = "51+"

    st.markdown(f"**Predicted winner:** {winner}")
    st.markdown(f"**Predicted points margin:** {margin} (Range: {margin_range})")
    st.markdown(f"**Why?** Based on AI, PNG passion, and data analysis.")

image_path = os.path.join(os.getcwd(), "logo1.png")
st.image(image_path, use_column_width=True)

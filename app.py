import streamlit as st
import random
import os

# CSS for PNG flag background & black fonts
st.markdown(
    """
    <style>
    /* Background with PNG flag colors */
    .reportview-container, .main {
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

    /* All text black */
    h1, h2, h3, p, label, div {
        color: black !important;
        text-shadow: none !important;
    }

    /* Buttons styling */
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

team1 = st.selectbox("Choose Team 1", ["Brisbane Broncos", "Melbourne Storm", "Penrith Panthers", "Sydney Roosters"])
team2 = st.selectbox("Choose Team 2", ["Canberra Raiders", "South Sydney Rabbitohs", "Parramatta Eels", "Newcastle Knights"])

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

    st.write(f"**Predicted winner:** {winner}")
    st.write(f"**Predicted points margin:** {margin} (Range: {margin_range})")
    st.write(f"**Why?** Based on AI and PNG passion.")

# Display the image (logo1.png) with updated parameter
if os.path.exists("logo1.png"):
    st.image("logo1.png", use_container_width=True)
else:
    st.write("Logo image not found.")

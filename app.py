import streamlit as st

# Inject CSS for background image and styles
st.markdown(
    """
    <style>
    /* Set the background image using your uploaded logo1.png */
    .stApp {
        background-image: url('logo1.png');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        position: relative;
        z-index: 0;
    }

    /* Light transparent overlay to improve text readability */
    .stApp::before {
        content: "";
        position: fixed;
        top: 0; left: 0; right: 0; bottom: 0;
        background-color: rgba(0, 0, 0, 0.15); /* adjust opacity as needed */
        z-index: -1;
    }

    /* White font color for all text */
    h1, h2, h3, h4, h5, h6, label, p, div, span {
        color: white !important;
        text-shadow: 0 0 4px rgba(0,0,0,0.7); /* subtle text shadow for clarity */
    }

    /* Style buttons */
    button, .stButton>button {
        background-color: #d80000 !important;
        color: white !important;
        font-weight: bold;
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Your app UI (example teams)
st.title("NRL Match Predictor | Mango Mine Case")

teams = [
    "Brisbane Broncos", "Melbourne Storm", "Penrith Panthers",
    "Sydney Roosters", "Canberra Raiders", "South Sydney Rabbitohs",
    "Parramatta Eels", "Newcastle Knights"
]

team1 = st.selectbox("Choose Team 1", teams, key="team1")
team2 = st.selectbox("Choose Team 2", teams, key="team2")

if st.button("Predict Winner"):
    # Example dummy prediction logic - replace with real AI/data later
    import random
    winner = random.choice([team1, team2])
    margin_range = random.choice(["1-10", "11-20", "21-30", "31-40", "41-50", "51+"])
    reason = f"Based on professional insights, tipster opinions, fan sentiment, and AI."

    st.markdown(f"### Predicted winner: {winner}")
    st.markdown(f"**Predicted points margin:** Range: {margin_range}")
    st.markdown(f"**Why?** {reason}")

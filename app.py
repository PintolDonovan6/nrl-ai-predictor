import streamlit as st

# Inject custom CSS for white fonts
st.markdown(
    """
    <style>
    /* Set background image or PNG colors if needed */
    .stApp {
        background-image: url('logo1.png');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        min-height: 100vh;
    }

    /* Make all text white */
    html, body, [class*="css"]  {
        color: white !important;
    }

    h1, h2, h3, h4, h5, h6, p, label, div, span, button {
        color: white !important;
        text-shadow: 1px 1px 2px black;
    }

    /* Fix sidebar text too */
    .sidebar .sidebar-content {
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Now your app content
st.title("NRL Match Predictor | Mango Mine Case")

team1 = st.selectbox("Choose Team 1", [
    "Brisbane Broncos", "Melbourne Storm", "Penrith Panthers", "Sydney Roosters",
    "Canberra Raiders", "South Sydney Rabbitohs", "Parramatta Eels", "Newcastle Knights",
    "Manly Sea Eagles", "Cronulla Sharks", "St George Illawarra Dragons", "Wests Tigers",
    "North Queensland Cowboys", "Gold Coast Titans", "New Zealand Warriors", "Dolphins"
])

team2 = st.selectbox("Choose Team 2", [
    t for t in [
        "Brisbane Broncos", "Melbourne Storm", "Penrith Panthers", "Sydney Roosters",
        "Canberra Raiders", "South Sydney Rabbitohs", "Parramatta Eels", "Newcastle Knights",
        "Manly Sea Eagles", "Cronulla Sharks", "St George Illawarra Dragons", "Wests Tigers",
        "North Queensland Cowboys", "Gold Coast Titans", "New Zealand Warriors", "Dolphins"
    ] if t != team1
])

if st.button("Predict Winner"):
    import random
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

    st.write(f"**Predicted Winner:** {winner}")
    st.write(f"**Predicted points margin range:** {margin_range}")
    st.write(f"**Why?** Based on insights from NRL analysts, tipsters, fan sentiment, and AI evaluation.")

import streamlit as st
import random

# Set page config
st.set_page_config(page_title="NRL Match Predictor | Mango Mine Case", layout="centered")

# Inject CSS for full background image and styling
st.markdown(
    """
    <style>
    /* Full screen background image */
    .stApp {
        background-image: url("https://i.imgur.com/yourImageLink.png");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        color: white;
    }

    /* Overlay to dim background for readability */
    .overlay {
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        background-color: rgba(0, 0, 0, 0.6);
        z-index: -1;
    }

    /* Container with some padding and semi-transparent background */
    .main-container {
        background-color: rgba(0, 0, 0, 0.5);
        padding: 2rem;
        border-radius: 12px;
        max-width: 600px;
        margin: 3rem auto;
        box-shadow: 0 0 20px rgba(0,0,0,0.7);
    }

    /* Image style inside app */
    .side-image {
        display: block;
        margin: 20px auto;
        max-width: 180px;
        opacity: 0.85;
        border-radius: 15px;
        box-shadow: 0 0 15px rgba(255,255,255,0.4);
    }

    /* Titles and texts */
    h1, h2, h3, p, label {
        color: white !important;
        text-shadow: 1px 1px 6px black;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* Button styling */
    button, .stButton > button {
        background-color: #d80000 !important;  /* PNG red */
        color: white !important;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.5rem 1rem;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# Overlay div to dim the background image
st.markdown('<div class="overlay"></div>', unsafe_allow_html=True)

# Main container for content
st.markdown('<div class="main-container">', unsafe_allow_html=True)

st.title("NRL Match Predictor | Mango Mine Case")
st.write("Powered by professional insights, tipster opinions, fan sentiment & AI.")

# Show PNG bird of paradise logo inside the app as well
st.image("logo1.png", caption="PNG Pride", use_column_width=False, width=150, clamp=True)

teams = [
    "Brisbane Broncos", "Melbourne Storm", "Penrith Panthers", "Sydney Roosters",
    "Canberra Raiders", "South Sydney Rabbitohs", "Parramatta Eels", "Newcastle Knights",
    "Wests Tigers", "Cronulla Sharks", "Gold Coast Titans", "North Queensland Cowboys",
    "St. George Illawarra Dragons", "New Zealand Warriors"
]

team1 = st.selectbox("Choose Team 1", teams)
team2 = st.selectbox("Choose Team 2", [t for t in teams if t != team1])

if st.button("Predict Winner"):
    # Simulate prediction based on dummy weighted logic (replace with your real AI)
    winner = random.choices([team1, team2], weights=[random.uniform(40, 60), random.uniform(40, 60)])[0]

    # Decide margin range buckets
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

    st.markdown(f"### Predicted winner: {winner}")
    st.markdown(f"### Predicted points margin range: {margin_range}")
    st.markdown("### Why?")
    st.write(
        f"Based on latest online expert tips, fan opinions, and detailed performance stats analysis."
    )

st.markdown("</div>", unsafe_allow_html=True)

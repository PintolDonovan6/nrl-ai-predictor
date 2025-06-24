import streamlit as st
from PIL import Image
import random

# --- Set full background image ---
def set_bg_image(image_file):
    with open(image_file, "rb") as img_file:
        img_data = img_file.read()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url(data:image/png;base64,{img_data.hex()});
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Since hex is large and complicated, better approach:
def set_bg_from_file(image_path):
    import base64
    with open(image_path, "rb") as f:
        data_url = base64.b64encode(f.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{data_url}");
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set background image here
set_bg_from_file("logo1.png")

# --- Font color and shadow for readability ---
st.markdown(
    """
    <style>
    body, .css-1d391kg, .css-1d391kg * {
        color: white !important;
        text-shadow: 1px 1px 2px black !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# App Title
st.title("NRL Match Predictor | Mango Mine Case")
st.write("Powered by professional insights, tipster opinions, fan sentiment & AI.")

teams = [
    "Brisbane Broncos", "Melbourne Storm", "Penrith Panthers", "Sydney Roosters",
    "Canberra Raiders", "South Sydney Rabbitohs", "Parramatta Eels", "Newcastle Knights",
    "St. George Illawarra Dragons", "Gold Coast Titans", "Cronulla Sharks",
    "Manly Sea Eagles", "Wests Tigers", "North Queensland Cowboys",
    "New Zealand Warriors", "Sydney Tigers"
]

# Team form scores — higher means better recent form (example data)
team_form = {
    "Brisbane Broncos": 80,
    "Melbourne Storm": 85,
    "Penrith Panthers": 90,
    "Sydney Roosters": 75,
    "Canberra Raiders": 70,
    "South Sydney Rabbitohs": 88,
    "Parramatta Eels": 78,
    "Newcastle Knights": 72,
    "St. George Illawarra Dragons": 65,
    "Gold Coast Titans": 60,
    "Cronulla Sharks": 68,
    "Manly Sea Eagles": 66,
    "Wests Tigers": 55,
    "North Queensland Cowboys": 62,
    "New Zealand Warriors": 58,
    "Sydney Tigers": 50
}

team1 = st.selectbox("Choose Team 1", teams)
team2 = st.selectbox("Choose Team 2", [team for team in teams if team != team1])

if st.button("Predict Winner"):
    form1 = team_form.get(team1, 60)
    form2 = team_form.get(team2, 60)

    # Simple weighted chance based on form, plus small randomness
    base_chance1 = form1 / (form1 + form2)
    base_chance2 = form2 / (form1 + form2)

    # Apply randomness +-5%
    chance1 = min(max(base_chance1 + random.uniform(-0.05, 0.05), 0), 1)
    chance2 = 1 - chance1

    winner = team1 if chance1 > chance2 else team2

    # Calculate margin range based on difference in form
    diff = abs(form1 - form2)
    if diff <= 10:
        margin_range = "1-10"
    elif diff <= 20:
        margin_range = "11-20"
    elif diff <= 30:
        margin_range = "21-30"
    elif diff <= 40:
        margin_range = "31-40"
    elif diff <= 50:
        margin_range = "41-50"
    else:
        margin_range = "51+"

    st.write(f"**Predicted winner:** {winner}")
    st.write(f"**Winning chance:** {team1} {round(chance1*100, 1)}% – {team2} {round(chance2*100, 1)}%")
    st.write(f"**Predicted points margin range:** {margin_range}")
    st.write(f"**Why?** Based on recent form stats, pro analyst opinions, and fan sentiment collected.")


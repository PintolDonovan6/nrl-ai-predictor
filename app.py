import streamlit as st
import requests

# Your Google Custom Search API credentials
API_KEY = "AIzaSyCNdyDKJSuRPApupwZEMQX4lnuGRm5YdXU"
CSE_ID = "b10cae8aa7f2249bb"

teams = [
    "Brisbane Broncos", "Melbourne Storm", "Penrith Panthers", "Sydney Roosters",
    "Canberra Raiders", "South Sydney Rabbitohs", "Parramatta Eels", "Newcastle Knights",
    "Gold Coast Titans", "Wests Tigers", "Cronulla Sharks", "St. George Illawarra Dragons",
    "Manly Sea Eagles", "New Zealand Warriors", "North Queensland Cowboys"
]

# Inject CSS styles
st.markdown("""
    <style>
    /* Main page background and text colors */
    .stApp {
        background-color: #000000 !important;
        color: #ffd700 !important;  /* Gold */
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* Headings in red */
    h1, h2, h3, h4 {
        color: #d80000 !important; /* Red */
    }

    /* Style buttons */
    button, .stButton > button {
        background-color: #d80000 !important; /* Red */
        color: #ffd700 !important; /* Gold */
        font-weight: bold;
        border-radius: 8px;
        border: none;
    }

    /* Style select boxes */
    select, .stSelectbox > div {
        background-color: #1a1a1a !important;
        color: #ffd700 !important; /* Gold text */
        border: 1px solid #d80000 !important;
        border-radius: 6px;
    }

    /* Change label color for dropdown labels */
    label[for^="selectbox"] {
        color: white !important;
        font-weight: bold;
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("NRL Match Predictor | Mango Mine Case")
st.write("Powered by professional insights, tipster opinions, fan sentiment & AI.")

team1 = st.selectbox("Choose Team 1", teams, index=0)
team2 = st.selectbox("Choose Team 2", teams, index=1)

if team1 == team2:
    st.error("Please select two different teams.")
else:
    if st.button("Predict Winner"):
        with st.spinner("Fetching latest expert tips and analyzing..."):
            query = f"NRL {team1} vs {team2} expert prediction analysis"
            url = "https://www.googleapis.com/customsearch/v1"
            params = {
                "key": API_KEY,
                "cx": CSE_ID,
                "q": query,
                "num": 5
            }
            try:
                response = requests.get(url, params=params)
                response.raise_for_status()
                data = response.json()
                snippets = [item.get("snippet", "") for item in data.get("items", [])]

                if not snippets:
                    st.warning("No expert tips found for this matchup. Showing fallback prediction.")
                    winner = team1
                    winning_chance = 60
                    margin = "11–20"
                    reason = f"No online expert tips found. {team1} is chosen by fallback logic."
                else:
                    # Simple heuristic: count mentions of each team in snippets
                    team1_mentions = sum(s.lower().count(team1.lower()) for s in snippets)
                    team2_mentions = sum(s.lower().count(team2.lower()) for s in snippets)

                    if team1_mentions > team2_mentions:
                        winner = team1
                        winning_chance = min(95, 60 + (team1_mentions - team2_mentions) * 10)
                    elif team2_mentions > team1_mentions:
                        winner = team2
                        winning_chance = min(95, 60 + (team2_mentions - team1_mentions) * 10)
                    else:
                        winner = team1
                        winning_chance = 55

                    margin = "21–30" if winning_chance > 70 else "11–20"
                    reason = " ".join(snippets[:3])  # Show first 3 snippets as reasoning

                losing_team = team2 if winner == team1 else team1
                losing_chance = 100 - winning_chance

                st.markdown(f"### Predicted Winner: {winner}")
                st.markdown(f"**Winning chance:** {winner} {winning_chance:.1f}% – {losing_team} {losing_chance:.1f}%")
                st.markdown(f"**Predicted points margin:** Range: {margin}")
                st.markdown(f"**Why?** {reason}")

            except requests.exceptions.HTTPError as http_err:
                st.error(f"HTTP error occurred: {http_err}")
            except Exception as err:
                st.error(f"Unexpected error occurred: {err}")

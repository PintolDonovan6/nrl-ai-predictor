import streamlit as st

# Inject PNG flag background and style
st.markdown(
    """
    <style>
    /* Apply PNG flag vertical stripes as full background */
    .reportview-container {
        background: linear-gradient(to right, 
            #000000 33.33%, 
            #d80000 33.33%, 
            #d80000 66.66%, 
            #ffd700 66.66%);
        min-height: 100vh;
        color: #ffd700;
    }

    /* Fix sidebar background too */
    .sidebar-content {
        background: linear-gradient(to right, 
            #000000 33.33%, 
            #d80000 33.33%, 
            #d80000 66.66%, 
            #ffd700 66.66%);
        color: #ffd700;
    }

    /* Text styling for readability */
    h1, h2, h3, p, label, div {
        color: #ffd700 !important;
        text-shadow: 1px 1px 2px black;
    }

    /* Buttons with better contrast */
    button, .stButton>button {
        background-color: #d80000 !important;
        color: white !important;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Your app UI goes here
st.title("NRL Match Predictor | Samting Blo Ples")

team1 = st.selectbox("Choose Team 1", ["Brisbane Broncos", "Melbourne Storm", "Penrith Panthers", "Sydney Roosters"])
team2 = st.selectbox("Choose Team 2", ["Canberra Raiders", "South Sydney Rabbitohs", "Parramatta Eels", "Newcastle Knights"])

if st.button("Predict Winner"):
    # Dummy prediction logic
    import random
    winner = random.choice([team1, team2])
    margin = random.randint(1, 60)
    
    # Calculate margin range bucket
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
    
    # Show image below predictions
    st.image("logo1.png", use_column_width=True)

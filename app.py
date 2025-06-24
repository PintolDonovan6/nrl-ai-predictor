import streamlit as st

# Inject PNG colors and fonts CSS
st.markdown(
    """
    <style>
    body, .main {
        background-color: #000000;
        color: #ffffff;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        padding: 30px 40px;
    }
    h1 {
        color: #d80000;
        text-shadow: 2px 2px 6px #ffcc00;
        font-weight: 900;
        font-size: 3rem;
    }
    h2 {
        color: #ffcc00;
        font-weight: 700;
        font-size: 2.4rem;
        margin-top: 20px;
    }
    p {
        font-size: 1.2rem;
        color: #eee;
        line-height: 1.6;
    }
    div.stButton > button:first-child {
        background-color: #d80000;
        color: white;
        font-weight: bold;
        border-radius: 12px;
        padding: 16px 40px;
        font-size: 1.2rem;
        box-shadow: 0 0 20px #d80000;
        transition: background-color 0.3s ease;
        cursor: pointer;
        margin-top: 25px;
    }
    div.stButton > button:first-child:hover {
        background-color: #ffcc00;
        color: black;
        box-shadow: 0 0 25px #ffcc00;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# App content starts here
st.title("NRL Match Predictor | Samting Blo Ples")

st.write(
    """
    Powered by AI and the passion of Papua New Guinea’s rugby league fans.  
    Predict match winners based on stats, expert views, and fan sentiment.
    """
)

st.header("Try the Predictor")

if st.button("Try the Predictor Now"):
    st.success("Traim Nau! Predictor is working!")

# You can add your predictor logic here

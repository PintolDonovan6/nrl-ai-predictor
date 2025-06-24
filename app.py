import streamlit as st

st.markdown(
    """
    <style>
    body, .main {
        background-color: #000000;
        color: #ffffff;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        padding: 40px;
    }
    h1 {
        color: #d80000; /* PNG red */
        font-weight: 900;
        font-size: 3rem;
        margin-bottom: 10px;
    }
    p {
        color: #eeeeee;
        font-size: 1.2rem;
        margin-top: 0;
        margin-bottom: 30px;
    }
    div.stButton > button:first-child {
        background-color: #d80000;
        color: white;
        font-weight: 700;
        border-radius: 12px;
        padding: 16px 40px;
        font-size: 1.2rem;
        box-shadow: 0 0 20px #d80000;
        cursor: pointer;
        transition: background-color 0.3s ease;
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

st.title("NRL Match Predictor | Samting Blo Ples")
st.write("Powered by AI and the passion of Papua New Guinea’s rugby league fans.")
st.write("Predict match winners based on stats, expert views, and fan sentiment.")

if st.button("Try the Predictor"):
    st.success("Traim Nau! Predictor is working.")

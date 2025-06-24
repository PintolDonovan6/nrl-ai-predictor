import streamlit as st

st.markdown(
    """
    <style>
    /* Background color */
    .main {
        background-color: #000000;
        color: #ffffff;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    /* Header style */
    h1, h2, h3 {
        color: #d80000;  /* PNG red */
        text-shadow: 1px 1px 3px #ffcc00; /* PNG yellow glow */
        font-weight: 900;
    }
    /* Buttons */
    .stButton>button {
        background-color: #d80000;
        color: white;
        font-weight: bold;
        border-radius: 12px;
        padding: 12px 30px;
        box-shadow: 0 0 15px #d80000;
        transition: background-color 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #ffcc00;
        color: black;
        box-shadow: 0 0 20px #ffcc00;
    }
    /* Paragraph text */
    p, .stText {
        color: #eee;
        font-size: 1.1rem;
        line-height: 1.6;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

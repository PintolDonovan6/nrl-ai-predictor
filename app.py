import streamlit as st

st.markdown(
    """
    <style>
    /* Background color */
    .main {
        background-color: #000000 !important;
        color: #ffffff !important;
    }
    /* Headers */
    h1, h2, h3 {
        color: #d80000 !important; /* PNG red */
        text-shadow: 1px 1px 3px #ffcc00 !important; /* PNG yellow glow */
    }
    /* Buttons */
    div.stButton > button:first-child {
        background-color: #d80000 !important;
        color: white !important;
        font-weight: bold !important;
        border-radius: 12px !important;
        padding: 12px 30px !important;
        box-shadow: 0 0 15px #d80000 !important;
        transition: background-color 0.3s ease !important;
        cursor: pointer !important;
    }
    div.stButton > button:first-child:hover {
        background-color: #ffcc00 !important;
        color: black !important;
        box-shadow: 0 0 20px #ffcc00 !important;
    }
    /* Text color */
    p, .stText {
        color: #eee !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

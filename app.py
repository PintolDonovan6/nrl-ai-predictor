import streamlit as st

st.markdown(
    """
    <style>
    .main {
        background-color: #000 !important;
        color: #fff !important;
    }
    h1, h2, h3 {
        color: #d80000 !important;
        text-shadow: 1px 1px 3px #ffcc00 !important;
    }
    div.stButton > button:first-child {
        background-color: #d80000 !important;
        color: #fff !important;
        border-radius: 12px !important;
        padding: 12px 30px !important;
        box-shadow: 0 0 15px #d80000 !important;
        transition: background-color 0.3s ease !important;
    }
    div.stButton > button:first-child:hover {
        background-color: #ffcc00 !important;
        color: #000 !important;
        box-shadow: 0 0 20px #ffcc00 !important;
    }
    p, .stText {
        color: #eee !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

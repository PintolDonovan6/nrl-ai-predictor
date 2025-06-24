import streamlit as st

st.markdown(
    """
    <style>
    /* Background & text */
    .main {
        background-color: #000000;
        color: #ffffff;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        padding: 20px 40px;
    }
    /* Headers */
    h1 {
        color: #d80000; /* PNG red */
        text-shadow: 1px 1px 4px #ffcc00; /* PNG yellow glow */
        font-weight: 900;
        font-size: 3rem;
    }
    h2 {
        color: #ffcc00; /* PNG yellow */
        font-weight: 700;
        font-size: 2.4rem;
    }
    /* Paragraph text */
    p {
        color: #eee;
        font-size: 1.1rem;
        line-height: 1.5;
    }
    /* Buttons */
    div.stButton > button:first-child {
        background-color: #d80000;
        color: white;
        border-radius: 10px;
        padding: 12px 30px;
        font-weight: bold;
        font-size: 1.2rem;
        box-shadow: 0 0 15px #d80000;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    div.stButton > button:first-child:hover {
        background-color: #ffcc00;
        color: black;
        box-shadow: 0 0 20px #ffcc00;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="main">', unsafe_allow_html=True)

st.title("NRL Match Predictor | Samting Blo Ples")

st.markdown(
    """
    <p>Powered by AI and PNG fan energy!</p>
    """,
    unsafe_allow_html=True,
)

st.header("NRL Match Winner Predictor")

st.markdown(
    """
    <p>This predictor uses data from past matches, expert opinions, and passionate PNG fan sentiment.</p>
    """,
    unsafe_allow_html=True,
)

if st.button("Try the Predictor Now"):
    st.markdown("<p><strong>Traim Nau!</strong></p>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

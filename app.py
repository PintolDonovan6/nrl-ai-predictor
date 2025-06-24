import streamlit as st

# Inject PNG-themed CSS styles
st.markdown(
    """
    <style>
    /* Background & font */
    .main {
        background-color: #000000;
        color: #ffffff;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        padding: 20px 40px 60px 40px;
    }
    /* Headers */
    h1 {
        color: #d80000; /* PNG Red */
        text-shadow: 2px 2px 8px #ffcc00; /* PNG Yellow glow */
        font-weight: 900;
        font-size: 3.5rem;
        margin-bottom: 0.2em;
        letter-spacing: 3px;
    }
    h2 {
        color: #ffcc00; /* PNG Yellow */
        font-weight: 800;
        font-size: 2.8rem;
        margin-top: 1em;
        margin-bottom: 0.5em;
    }
    /* Paragraph text */
    p, .stText, .stMarkdown {
        color: #eee;
        font-size: 1.15rem;
        line-height: 1.6;
    }
    /* Buttons */
    div.stButton > button:first-child {
        background-color: #d80000;
        color: white;
        font-weight: 700;
        border-radius: 12px;
        padding: 16px 40px;
        font-size: 1.3rem;
        box-shadow: 0 0 20px #d80000;
        transition: background-color 0.3s ease, color 0.3s ease;
        cursor: pointer;
        margin-top: 20px;
    }
    div.stButton > button:first-child:hover {
        background-color: #ffcc00;
        color: black;
        box-shadow: 0 0 25px #ffcc00;
    }
    /* Bird of Paradise container */
    .bird-container {
        margin: 50px auto 80px auto;
        max-width: 320px;
        background: linear-gradient(90deg, #ffcc00 0%, #d80000 100%);
        border-radius: 16px;
        padding: 30px;
        text-align: center;
        color: #000;
        font-weight: 600;
        font-style: italic;
        font-size: 1.2rem;
        box-shadow: 0 0 30px #ffcc00;
        user-select: none;
    }
    /* Footer */
    footer {
        margin-top: 60px;
        text-align: center;
        color: #bbb;
        font-size: 0.9rem;
        border-top: 1px solid #222;
        padding: 15px 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Body content
st.markdown('<div class="main">', unsafe_allow_html=True)

st.markdown("<h1>NRL Match Predictor | Samting Blo Ples</h1>", unsafe_allow_html=True)

st.markdown(
    """
    <p>
    Powered by AI and the passion of Papua New Guinea’s rugby league fans. Analyze past matches, expert insights, and fan energy to get smarter predictions.
    </p>
    """,
    unsafe_allow_html=True,
)

st.markdown("<h2>NRL Match Winner Predictor</h2>", unsafe_allow_html=True)

st.markdown(
    """
    <p>
    This predictor uses data from past matches, current form, expert opinions, and fan sentiment. Built for everyone in PNG who lives and breathes rugby league!
    </p>
    """,
    unsafe_allow_html=True,
)

# Try predictor button
if st.button("Try the Predictor Now"):
    st.markdown("<p><strong>Traim Nau!</strong></p>", unsafe_allow_html=True)

# Bird of Paradise placeholder block
st.markdown(
    """
    <div class="bird-container">
        🦜 PNG’s Iconic Bird of Paradise (Image coming soon!)
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <footer>
    &copy; 2025 Donovan Pintol | Powered by PNG Fans and Smart AI
    </footer>
    """,
    unsafe_allow_html=True,
)

st.markdown("</div>", unsafe_allow_html=True)

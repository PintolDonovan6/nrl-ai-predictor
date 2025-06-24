import streamlit as st

# Page config
st.set_page_config(
    page_title="NRL Match Predictor | Samting Blo Ples",
    page_icon="🏉",
    layout="centered",
)

# PNG Colors & Styles CSS
st.markdown(
    """
    <style>
    /* Overall background and font */
    .main {
        background-color: #000000;
        color: #fff;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        padding: 0 20px 40px 20px;
    }
    /* Header with PNG flag gradient */
    .header {
        background: linear-gradient(90deg, #d80000 0%, #ffcc00 50%, #000000 100%);
        padding: 40px 20px;
        text-align: center;
        border-radius: 15px;
        box-shadow: 0 0 20px #d80000;
        margin-bottom: 40px;
    }
    .header h1 {
        margin: 0;
        font-size: 3.5rem;
        font-weight: 900;
        color: white;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.7);
        letter-spacing: 3px;
    }
    /* Intro paragraph */
    .intro-text {
        max-width: 750px;
        margin: 0 auto 40px auto;
        font-size: 1.3rem;
        color: #eee;
        line-height: 1.6;
    }
    /* Button with PNG red & yellow */
    .btn-primary {
        background-color: #d80000;
        color: white;
        font-weight: 700;
        padding: 16px 36px;
        font-size: 1.3rem;
        border-radius: 12px;
        border: none;
        cursor: pointer;
        transition: background-color 0.3s ease, color 0.3s ease;
        box-shadow: 0 0 15px #d80000;
        margin-bottom: 10px;
        display: inline-block;
    }
    .btn-primary:hover {
        background-color: #ffcc00;
        color: #000;
        box-shadow: 0 0 20px #ffcc00;
    }
    /* Bird placeholder container */
    .bird-container {
        text-align: center;
        margin-top: 50px;
        margin-bottom: 60px;
        padding: 30px;
        border-radius: 15px;
        background: linear-gradient(90deg, #ffcc00 0%, #d80000 100%);
        box-shadow: 0 0 30px #ffcc00;
        max-width: 300px;
        margin-left: auto;
        margin-right: auto;
        color: #000;
        font-weight: 600;
        font-style: italic;
        font-size: 1.1rem;
        user-select: none;
    }
    /* Footer style */
    footer {
        text-align: center;
        color: #bbb;
        font-size: 0.9rem;
        padding: 15px 10px;
        border-top: 1px solid #222;
        margin-top: 40px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header
st.markdown('<div class="header"><h1>NRL Match Predictor | Samting Blo Ples</h1></div>', unsafe_allow_html=True)

# Intro text
st.markdown(
    """
    <div class="intro-text">
    Powered by AI and the passion of Papua New Guinea’s rugby league fans. Analyze past matches, expert insights, and fan energy to get smarter predictions.
    </div>
    """,
    unsafe_allow_html=True,
)

# Predictor button
if st.button("Try the Predictor Now"):
    st.write("Launching Predictor... Traim Nau!")

# Bird of Paradise placeholder (replace with image later)
st.markdown(
    """
    <div class="bird-container">
        🦜 PNG's Iconic Bird of Paradise (Image coming soon!)
    </div>
    """,
    unsafe_allow_html=True,
)

# Footer
st.markdown(
    """
    <footer>
        &copy; 2025 Donovan Pintol | Powered by PNG Fans and Smart AI
    </footer>
    """,
    unsafe_allow_html=True,
)

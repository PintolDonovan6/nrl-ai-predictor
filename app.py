import streamlit as st

# Page config
st.set_page_config(
    page_title="NRL Match Predictor | Samting Blo Ples",
    page_icon="🏉",
    layout="centered",
)

# Custom CSS for PNG colors and style
st.markdown(
    """
    <style>
    .main {
        background-color: #000000;
        color: #fff;
        font-family: 'Segoe UI', sans-serif;
    }
    .header {
        background: linear-gradient(to right, #d80000, #ffcc00, #000);
        padding: 30px;
        text-align: center;
        border-radius: 10px;
        margin-bottom: 25px;
    }
    .header h1 {
        color: white;
        font-size: 3em;
        margin: 0;
        font-weight: bold;
        text-shadow: 2px 2px 4px #000000;
    }
    .btn-primary {
        background-color: #d80000;
        color: #fff;
        font-weight: bold;
        padding: 12px 24px;
        border-radius: 12px;
        border: none;
        cursor: pointer;
        transition: background-color 0.3s ease;
        font-size: 1.2em;
        margin-top: 20px;
    }
    .btn-primary:hover {
        background-color: #ffcc00;
        color: #000;
    }
    .bird-container {
        text-align: center;
        margin-top: 40px;
    }
    .bird-caption {
        color: #ffcc00;
        font-style: italic;
        margin-top: 10px;
        font-size: 1.1em;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header
st.markdown('<div class="header"><h1>NRL Match Predictor | Samting Blo Ples</h1></div>', unsafe_allow_html=True)

st.write(
    """
    Welcome to the free NRL Match Predictor, powered by AI and the passion of PNG fans.
    Try it now and see who’s likely to win!
    """
)

# Predictor button
if st.button("Try the Predictor Now"):
    st.write("Launching Predictor... Traim Nau!")

# Bird of Paradise bird image + caption
st.markdown(
    """
    <div class="bird-container">
        <img src="bird_of_paradise_bird.png" alt="Bird of Paradise Bird" width="200" style="border-radius: 12px;" />
        <div class="bird-caption">PNG’s iconic Bird of Paradise — a symbol of strength and beauty</div>
    </div>
    """,
    unsafe_allow_html=True,
)

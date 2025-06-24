import streamlit as st

st.markdown(
    """
    <style>
    /* Main background and text */
    .css-18e3th9 {
        background-color: #000000 !important;
        color: #ffffff !important;
    }
    /* Headers */
    h1, h2, h3 {
        color: #d80000 !important;
        text-shadow: 1px 1px 3px #ffcc00 !important;
    }
    /* Buttons */
    button.css-1emrehy.edgvbvh3 {
        background-color: #d80000 !important;
        color: #ffffff !important;
        border-radius: 12px !important;
        padding: 12px 30px !important;
        box-shadow: 0 0 15px #d80000 !important;
        transition: background-color 0.3s ease !important;
        cursor: pointer;
    }
    button.css-1emrehy.edgvbvh3:hover {
        background-color: #ffcc00 !important;
        color: #000000 !important;
        box-shadow: 0 0 20px #ffcc00 !important;
    }
    /* Paragraph text */
    p, .stText {
        color: #eeeeee !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("NRL Match Predictor | Samting Blo Ples")

st.write("Powered by AI and PNG fan energy!")

if st.button("Try the Predictor Now"):
    st.write("Traim Nau!")

import streamlit as st

# Your existing imports and code here...

# Add this near the top of your app.py file (just after imports and before main UI)
st.markdown(
    """
    <div style="
        border: 2px solid #d80000; 
        background-color: #fff3cd; 
        padding: 15px; 
        border-radius: 8px; 
        color: #856404;
        font-family: Arial, sans-serif;
        margin-bottom: 20px;">
        <strong>Note:</strong> This app uses Google Custom Search Engine (CSE) configured to search only trusted NRL and sports sites to deliver focused, relevant predictions.<br>
        If you want to customize which sites are included in the search, you can create or edit your CSE here: <a href="https://cse.google.com/cse/all" target="_blank">Google Custom Search Engine Setup</a>
    </div>
    """,
    unsafe_allow_html=True,
)

# Continue with your normal Streamlit app UI
st.title("NRL Match Predictor | Samting Blo Ples")

# ... rest of your app code ...

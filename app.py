import streamlit as st
import requests

# Replace these with your actual API key and CSE ID
API_KEY = "YOUR_GOOGLE_API_KEY"
CX_ID = "YOUR_CUSTOM_SEARCH_ENGINE_ID"

# Add this helper text so users know how to set up CSE focus
st.markdown("""
**Note:**  
This app uses Google Custom Search Engine (CSE) configured to search only trusted NRL and sports sites to deliver focused, relevant predictions.  
If you want to customize which sites are included in the search, you can create or edit your CSE here:  
[Google Custom Search Engine Setup](https://programmablesearchengine.google.com/about/)  
""")

NRL_TEAMS = [
    "Brisbane Broncos", "Melbourne Storm", "Penrith Panthers", "Sydney Roosters",
    "Canberra Raiders", "South Sydney Rabbitohs", "Parramatta Eels", "Newcastle Knights",
    "Wests Tigers", "Manly Sea Eagles", "Cronulla Sharks", "New Zealand Warriors",
    "Gold Coast Titans", "St George Illawarra Dragons", "North Queensland Cowboys",
    "Canterbury Bulldogs"
]

def google_search(query, num=5):
    url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={CX_ID}&q={query}&num={num}"
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        results = resp.json()
        return results.get('items', [])
    except Exception as e:
        st.error(f"Error fetching search results: {e}")
        return []

# The rest of your prediction and UI code here ...

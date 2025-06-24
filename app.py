import streamlit as st
import requests
import random

# === Your Google Custom Search credentials ===
API_KEY = "AIzaSyCNdyDKJSuRPApupwZEMQX4lnuGRm5YdXU"
CSE_ID   = "b10cae8aa7f2249bb"

# === Simple recent-form scores for fallback ===
team_form = {
    "Brisbane Broncos": 80, "Melbourne Storm": 85, "Penrith Panthers": 90,
    "Sydney Roosters": 75, "Canberra Raiders": 70, "South Sydney Rabbitohs": 88,
    "Parramatta Eels": 78, "Newcastle Knights": 72, "Cronulla Sharks": 68,
    "Manly Sea Eagles": 66, "Gold Coast Titans": 60, "New Zealand Warriors": 58,
    "North Queensland Cowboys": 62, "St George Illawarra Dragons": 65,
    "Wests Tigers": 55
}

# === Attempt a Google CSE search ===
def google_snippets(t1, t2):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": API_KEY, "cx": CSE_ID,
        "q": f"NRL {t1} vs {t2} expert prediction analysis",
        "num": 5
    }
    r = requests.get(url, params=params, timeout=5)
    r.raise_for_status()
    return [item["snippet"] for item in r.json().get("items", [])]

# === Fallback prediction based on form ===
def fallback_predict(t1, t2):
    f1, f2 = team_form.get(t1,60), team_form.get(t2,60)
    total = (f1+f2) or 1
    p1, p2 = f1/total*100, f2/total*100
    winner = t1 if p1>=p2 else t2
    diff = abs(f1-f2)
    if diff<=10:   rng="1–10"
    elif diff<=20: rng="11–20"
    elif diff<=30: rng="21–30"
    elif diff<=40: rng="31–40"
    elif diff<=50: rng="41–50"
    else:          rng="51+"
    return winner, p1, p2, rng, "Using recent form data (fallback)."

# === Combined prediction logic ===
def predict(t1, t2):
    try:
        snippets = google_snippets(t1, t2)
        if not snippets:
            raise requests.HTTPError("no snippets")
        s1 = sum(s.lower().count(t1.lower()) for s in snippets)
        s2 = sum(s.lower().count(t2.lower()) for s in snippets)
        for kw in ["win","favored","likely","advantage","strong"]:
            s1 += sum(1 for s in snippets if t1.lower() in s.lower() and kw in s.lower())
            s2 += sum(1 for s in snippets if t2.lower() in s.lower() and kw in s.lower())
        total = s1+s2 or 1
        p1, p2 = s1/total*100, s2/total*100
        winner = t1 if p1>=p2 else t2
        diff = abs(p1-p2)
        if diff<=10:   rng="1–10"
        elif diff<=20: rng="11–20"
        elif diff<=30: rng="21–30"
        elif diff<=40: rng="31–40"
        elif diff<=50: rng="41–50"
        else:          rng="51+"
        return winner, p1, p2, rng, "Based on live expert tips & fan sentiment."
    except Exception:
        return fallback_predict(t1, t2)

# === Streamlit UI & styling ===
st.set_page_config(page_title="NRL Match Predictor | Mango Mine Case")

st.markdown("""
    <style>
      .stApp {
        background: url("logo1.png") center/cover no-repeat fixed;
      }
      body, h1, h2, h3, p, div, label, span, button {
        color: white !important;
        text-shadow: 1px 1px 2px black;
        font-family: 'Segoe UI', sans-serif;
      }
      button, .stButton>button {
        background-color: #d80000 !important;
        color: white !important;
        font-weight: bold;
        border-radius: 6px;
        padding: 8px 16px;
      }
      .stSelectbox>div>div>div>div {
        background-color: rgba(0,0,0,0.6) !important;
        color: white !important;
      }
    </style>
""", unsafe_allow_html=True)

st.title("NRL Match Predictor | Mango Mine Case")
st.markdown("Powered by professional insights, tipster opinions, fan sentiment & AI.")

teams = list(team_form.keys())
t1 = st.selectbox("Choose Team 1", teams)
t2 = st.selectbox("Choose Team 2", [x for x in teams if x!=t1])

if st.button("Predict Winner"):
    winner, p1, p2, margin, reason = predict(t1, t2)
    loser = t2 if winner==t1 else t1
    st.markdown(f"**Predicted winner:** {winner}")
    st.markdown(f"**Winning chances:** {winner} {max(p1,p2):.1f}% – {loser} {min(p1,p2):.1f}%")
    st.markdown(f"**Predicted points margin range:** {margin}")
    st.markdown(f"**Why?** {reason}")

import streamlit as st

# SEO meta tags
st.markdown("""
<meta name="description" content="2025 NRL Match Predictor with live ladder & team stats.">
<title>NRL Match Predictor 2025</title>
""", unsafe_allow_html=True)

st.set_page_config(page_title="NRL Match Predictor 2025", layout="centered")

teams = [
    "Penrith Panthers","Canterbury Bulldogs","Brisbane Broncos","Melbourne Storm",
    "Newcastle Knights","Sydney Roosters","Canberra Raiders","New Zealand Warriors",
    "Dolphins","North Queensland Cowboys","Cronulla Sharks","South Sydney Rabbitohs",
    "Manly Sea Eagles","Parramatta Eels","St. George Illawarra Dragons",
    "Gold Coast Titans","Wests Tigers"
]

# Head-to-head example
head_to_head = {
    ("Canterbury Bulldogs", "Penrith Panthers"): 41.3,
    ("Penrith Panthers", "Canterbury Bulldogs"): 58.7,
}

# 2025 ladder data & compute strengths
ladder = {
    "Canterbury Bulldogs": {"played":13,"wins":11,"pf":330,"pa":232,"pts":28},
    "Canberra Raiders": {"played":15,"wins":12,"pf":412,"pa":312,"pts":26},
    "Melbourne Storm": {"played":13,"wins":9,"pf":429,"pa":257,"pts":24},
    "New Zealand Warriors": {"played":14,"wins":10,"pf":309,"pa":284,"pts":24},
    "Brisbane Broncos": {"played":14,"wins":7,"pf":372,"pa":322,"pts":18},
    "Cronulla Sharks": {"played":15,"wins":8,"pf":360,"pa":340,"pts":18},
    "Sydney Roosters": {"played":14,"wins":7,"pf":344,"pa":328,"pts":18},
    "Penrith Panthers": {"played":14,"wins":6,"pf":314,"pa":313,"pts":17},
    "Dolphins": {"played":15,"wins":7,"pf":428,"pa":288,"pts":16},
    "Manly Sea Eagles": {"played":14,"wins":6,"pf":322,"pa":300,"pts":16},
    "St. George Illawarra Dragons": {"played":13,"wins":5,"pf":272,"pa":331,"pts":16},
    "North Queensland Cowboys": {"played":14,"wins":5,"pf":286,"pa":426,"pts":15},
    "Newcastle Knights": {"played":15,"wins":6,"pf":219,"pa":282,"pts":14},
    "Wests Tigers": {"played":14,"wins":5,"pf":280,"pa":346,"pts":14},
    "Parramatta Eels": {"played":14,"wins":5,"pf":267,"pa":356,"pts":14},
    "South Sydney Rabbitohs": {"played":15,"wins":6,"pf":265,"pa":354,"pts":14},
    "Gold Coast Titans": {"played":14,"wins":4,"pf":288,"pa":426,"pts":12},
}

team_strength = {
    t: d["pts"]*3 + (d["pf"] - d["pa"])/10
    for t, d in ladder.items()
}

def calc_margin(pct):
    if pct >= 75: return "16–25"
    if pct >= 60: return "11–15"
    if pct >= 50: return "6–10"
    return "1–5"

def predict(t1, t2):
    if t1 == t2:
        return None, None, None, None, None, "Select two different teams."
    h2h = head_to_head.get((t1, t2))
    if h2h is not None:
        winner = t1 if h2h > 50 else t2
        wp = max(h2h, 100-h2h)
        lp = min(h2h, 100-h2h)
        return winner, wp, t2 if winner==t1 else t1, lp, calc_margin(wp), f"H2H: {winner} has {wp:.1f}% vs opponent."
    s1, s2 = team_strength[t1], team_strength[t2]
    wp1 = s1 / (s1 + s2) * 100
    wp2 = 100 - wp1
    winner, loser, wp, lp = (t1, t2, wp1, wp2) if wp1 > wp2 else (t2, t1, wp2, wp1)
    return winner, wp, loser, lp, calc_margin(abs(wp1-wp2)), f"Form-based: {winner} has {wp:.1f}%."

st.title("NRL Match Predictor 2025")
st.write("✅ All 17 teams included with 2025 ladder & matchup logic.")

t1 = st.selectbox("Team 1", teams)
t2 = st.selectbox("Team 2", teams, index=1)

if st.button("Predict"):
    w, wp, l, lp, margin, reason = predict(t1, t2)
    if not w:
        st.error(reason)
    else:
        st.markdown(f"**Predicted Winner:** {w}")
        st.markdown(f"**Winning chance:** {w} {wp:.1f}% – {l} {lp:.1f}%")
        st.markdown(f"**Predicted points margin:** {margin}")
        st.markdown(f"**Why?** {reason}")

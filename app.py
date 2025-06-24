def fetch_nrl_fixtures():
    url = "https://www.nrl.com/draw/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/114.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
    }
    try:
        r = requests.get(url, headers=headers, timeout=10)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")
        fixtures = []
        cards = soup.find_all('div', class_='matchCard')
        for card in cards:
            teams = card.find_all('div', class_='teamName')
            if len(teams) < 2:
                continue
            home = teams[0].get_text(strip=True)
            away = teams[1].get_text(strip=True)
            date = card.find('div', class_='matchCard__date')
            dt = date.get_text(strip=True) if date else "Date TBD"
            fixtures.append({'home': home, 'away': away, 'date': dt})
        return fixtures
    except Exception as e:
        st.error(f"Could not fetch NRL fixtures. Error: {e}")
        return []

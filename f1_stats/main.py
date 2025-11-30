from bs4 import BeautifulSoup
import cloudscraper
import pandas as pd
scraper = cloudscraper.create_scraper()

URL = ""

response = scraper.get(URL, headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",

    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",

    "Accept-Language": "en-US,en;q=0.9",

    "Referer": "https://www.google.com/",

    "Upgrade-Insecure-Requests": "1",

    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Connection": "keep-alive",
}
)

print(response.status_code)
print(response.text[:5000])
web_page = response.text
print(web_page)
with open("site_text.html", "w") as file:
    file.write(web_page)

filehandle = open("site_text.html")

soup = BeautifulSoup(filehandle, "html.parser")
drivers = soup.find_all(class_="msr_col2")
wins = soup.find_all(class_="msr_col4")
pole_positions = soup.find_all(class_="msr_col8")
podiums = soup.find_all(class_="msr_col7")

driver_name = []
driver_wins = []
driver_poles = []
driver_podiums = []

for driver  in drivers:
    names = driver.get_text()
    driver_name.append(names)

for win in wins:
    all_wins = win.get_text()
    driver_wins.append(all_wins)

for pole in pole_positions:
    pol_pos = pole.get_text()
    driver_poles.append(pol_pos)

for podium in podiums:
    all_podiums = podium.get_text()
    driver_podiums.append(all_podiums)

data = {
    "Name": driver_name[1:110],
    "Wins": driver_wins[2:111],
    "Poles": driver_poles[1:110],
    "Podiums": driver_podiums[1:110]
}

df = pd.DataFrame(data)
df.to_csv('f1_driver_stats.csv')
print("CSV created successfully")

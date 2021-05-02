import asyncio
import webbrowser
from pyppeteer import launch
from bs4 import BeautifulSoup
from items import Item

def get_query():
    return input("Please enter search query:\n").replace(" ", "-")

def get_preference():
    return input("Please mention your preference for opening tracks (press w for web version or a for desktop app).\n")

async def main():
    query = get_query()
    preference = get_preference()
    print("Scraping...Please wait.\n")
    browser = await launch()
    page = await browser.newPage()
    await page.goto("https://aniplaylist.com/{}".format(query), timeout=1000000)
    try:
        await page.click("#qc-cmp2-ui > div.qc-cmp2-footer.qc-cmp2-footer-overlay.qc-cmp2-footer-scrolled > div > button.css-1rr34en") # Agree button
    except: # Sometimes the message doesn't show up
        pass
    soup = BeautifulSoup(await page.content(), 'html.parser')
    await browser.close()
    songs = []
    playlists = []
    elems = soup.select(".song-card")
    for e in elems:
        kind = e.select_one(".tag").get_text().strip()
        name = e.select_one(".song-data strong").get_text().strip()
        user = e.select_one(".artists .tag a").get_text().strip()
        user_url = e.select_one(".artists .tag a")["href"]
        url = e.select_one(".card-image a")["href"]
        anime = e.select_one(".card-image a figure div")["alt"]
        i = Item(name, anime, kind, url, user_url)
        if kind == "Playlist":
            playlists.append(i)
        else:
            songs.append(i)
    print(f"Found {len(songs)} song(s), {len(playlists)} playlist(s).")
    while True:
        for index, song in enumerate(songs):
            print(str(index) + ". ", song)
        i = input("Please enter index of song you want to open or press q to exit.\n")
        if i == "q": break
        chosen_song = songs[int(i)]
        if preference == "w":
            chosen_song.open_in_browser()
            print(f"Opened {song} in browser!")
        else:
            chosen_song.open_in_app()
            print(f"Opened {song} in app!")

asyncio.get_event_loop().run_until_complete(main())

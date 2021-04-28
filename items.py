import webbrowser

class Item:
    def __init__(self, name, anime, kind, url, user_url):
        self.name = name
        self.anime = anime
        self.url = url
        self.user_url = user_url
        self.kind = kind

    def open_in_browser(self):
        webbrowser.open(self.url)

    def open_user(self):
        webbrowser.open(self.user_url)

    def __str__(self):
        return f"{self.name} - {self.anime} {self.kind}"


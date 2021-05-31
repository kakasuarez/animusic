class Item:
    def __init__(self, name, anime, kind, url, user_url):
        self.name = name
        self.anime = anime
        self.url = url
        self.user_url = user_url
        self.kind = kind 

    def __str__(self):
        return f"{self.name} - {self.anime} {self.kind}"


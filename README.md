# animusic

### Unofficial aniplaylist.com API

Find official anime music on Spotify.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/kakasuarez/animusic/)

## API Endpoints

- `/`:

  ### GET Parameters:

  `query`: _Required._ The search query to search on aniplaylist.

  ### Returns:

  - Error with HTTP code 400 and a message of "No query parameter." if no `query` GET parameter was supplied.
  - A JSON object with the following keys:

    1. `playlists`: A JSON array of objects with the following keys:

       - `anime`: The name of the anime.

       - `kind`: For all playlists, the value will be "Playlist".

       - `name`: For a playlist, this will be details about the playlist contents, like "openings, endings & OST".

       - `url`: The URL to the Spotify playlist.

       - `user_url`: The URL of the Spotify user who created the playlist, which is most likely the AniPlaylist Spotify account.

    2. `songs`: A JSON array of objects with the following keys:

       - `anime`: The name of the anime.

       - `kind`: How the song was used in the anime, for example "Ending".

       - `name`: The name of the track.

       - `url`: The URL to the Spotify track.

       - `user_url`: The URL of the track's artist on Spotify.

Note: A hosted instance is available at https://animusicapi.herokuapp.com; however, currently it runs only for the first 25 days of the month as I have yet to verify my account. **The ideal choice currently is to host an instance yourself.**

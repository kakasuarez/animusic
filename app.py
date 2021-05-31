from quart import Quart, request, jsonify
import asyncio
import scraper

app = Quart(__name__)

@app.route('/', methods=["GET"])
async def hello():
    query = request.args.get("query")
    songs, playlists = await scraper.main(query=query)
    return jsonify({"songs": songs, "playlists": playlists})

if __name__ == "__main__":
    asyncio.run(app.run_task(host='0.0.0.0'))
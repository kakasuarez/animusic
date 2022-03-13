from quart import Quart, request, jsonify
import asyncio
import scraper
import os

app = Quart(__name__)

@app.route('/', methods=["GET"])
async def hello():
    query = request.args.get("query")
    if not query:
        return "No query parameter.", 400
    songs, playlists = await scraper.main(query=query)
    response = jsonify({"songs": songs, "playlists": playlists})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    asyncio.run(app.run_task(host='0.0.0.0', port=port))

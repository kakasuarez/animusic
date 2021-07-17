from flask import Flask, request, jsonify
from flask_cors import CORS
import asyncio
import scraper
import os
import nest_asyncio
nest_asyncio.apply()
app = Flask(__name__)
loop = asyncio.get_event_loop()
CORS(app)
@app.route('/', methods=["GET"])
def hello():
    query = request.args.get("query")
    if not query:
        return jsonify({"message": "Query must be provided."})
    songs, playlists = loop.run_until_complete(scraper.main(query=query))
    return jsonify({"songs": songs, "playlists": playlists})

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, use_reloader=True, threaded=True)
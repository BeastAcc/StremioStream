
from json import dumps
from flask import jsonify, abort, Response
from StremioStream import app
from StremioStream.manifest.manifest import MANIFEST
from StremioStream.catalogs.catalogs import getCatalog
from StremioStream.streams.streams import Streams
from StremioStream.meta.meta import getMeta
def common_headers(resp_obj):
    resp_obj.headers["Access-Control-Allow-Origin"] = "*"
    resp_obj.headers["Access-Control-Allow-Headers"] = "*"
    return resp_obj

@app.route("/")
def init():
    return "Welcome to StremioStream."


@app.route("/manifest.json")
def addon_manifest():
    return common_headers(jsonify(MANIFEST))
@app.route("/catalog/movie/StremioStream/genre=<genre>.json")
def addon_catalog(genre):
    return common_headers(jsonify({ 'metas': getCatalog(genreFull=genre)}))
@app.route("/catalog/movie/StremioStreamSearch/search=<query>.json")
def addon_catalog_search(query):
    return common_headers(jsonify({ 'metas': getCatalog(search=query)}))
@app.route("/stream/<type>/<full_id>.json")
def addon_stream(type,full_id):
    strm_obj=Streams(type,full_id)
    return common_headers(jsonify({ 'streams': strm_obj.get_streams()}))
@app.route("/meta/movie/<id>.json")
def addon_meta(id):
    if id[:2]=='ST':
        return common_headers(jsonify({
        'meta': {
        "description": id.replace('ST',''),
        "id": id,
        "name": id.replace('ST',''),
        "type": "movie"}
        }))
    return common_headers(jsonify({
        'meta': getMeta(id)
    }))
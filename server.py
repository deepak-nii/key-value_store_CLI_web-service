import json
import asyncio
import aiohttp
from aiohttp import web

app = web.Application()
store, watchers = {}, {}
store_lock = asyncio.Lock()
routes = web.RouteTableDef()


@routes.get("/{key}")
async def hello(request):
    key = request.match_info["key"]
    global store
    return web.json_response({key: store.get(key)})


@routes.post("/{key}")
async def hello(request):
    global store, watchers, store_lock
    async with store_lock:
        key = request.match_info["key"]
        value = (await request.json()).get("value")
        store[key] = value
        active = []
        for ws in watchers.get(key, []):
            try:
                if not ws.closed:
                    await ws.send_str(json.dumps({key: value}))
                    active.append(ws)
            except Exception:
                pass
        watchers[key] = active
    return web.Response(text="")


@routes.get("/{key}/watch")
async def websocket_handler(request):
    key = request.match_info["key"]
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    global watchers
    if key not in watchers:
        watchers[key] = []
    watchers[key].append(ws)
    async for msg in ws:
        if msg.type == aiohttp.WSMsgType.ERROR or msg.type == aiohttp.WSMsgType.CLOSE:
            await ws.close()
    return ws


app = web.Application()
app.add_routes(routes)
web.run_app(app)

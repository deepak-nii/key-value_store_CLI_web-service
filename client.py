import aiohttp
import asyncio
import requests as R
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("key", metavar=('key'))
parser.add_argument("--set", metavar=(''), type=str)
parser.add_argument("--watch", action="store_true", default=False)
parser.add_argument("--root", metavar=('http://0.0.0.0:8080'), type=str, default="http://0.0.0.0:8080")
args = parser.parse_args()

async def watch():
    async with aiohttp.ClientSession() as session:
        async with session.ws_connect(f"{args.root}/{args.key}/watch") as ws:
            async for msg in ws:
                if msg.type == aiohttp.WSMsgType.TEXT:
                    print(msg.data)
                elif msg.type == aiohttp.WSMsgType.ERROR:
                    break

if args.set:
    r = R.post(args.root + f"/{args.key}", json={"value": args.set})
    assert r.status_code == 200
elif args.watch:
    asyncio.run(watch())
else:
    r = R.get(f"{args.root}/{args.key}")
    print(r.json())

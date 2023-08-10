from structs import discord, websocket
import asyncio

__TOKEN = "MTA3NTMxMjMwODY0MjkxMDI3OQ.GAspN0.f73nNfF6UgtnUD-bSP6ScpccgOW7P61ImleCFs"

asyncio.get_event_loop().create_task(discord.client.start(__TOKEN))
websocket.init()
asyncio.get_event_loop().run_forever()

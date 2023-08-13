import asyncio
import websockets
from structs import discord, handler

connections = {}

async def on_register(websocket, identifier):
    if connections.get(identifier) is None:
        print("Registered " + identifier)
        connections[identifier] = [websocket, {}]
        await discord.on_register(identifier)

async def on_unregister(identifier, *err):
    if connections.get(identifier):
        print("Unregistered " + identifier)
        await discord.on_unregister(identifier)
        await handler.on_unregister(identifier, connections[identifier])
        del connections[identifier]
    if err:
        print(err)

async def connect(websocket, path):
    identifier = await websocket.recv()
    await on_register(websocket, identifier)
    try:
        async for message in websocket:
            await handler.on_message_received(identifier, connections[identifier], message)
    except Exception as e:
        print(e)
        await on_unregister(identifier, f"{e.args}")
    finally:
        await on_unregister(identifier)

def init():
    server = websockets.serve(connect, "0.0.0.0", 3000)  # Permitir conexiones desde cualquier dirección
    loop = asyncio.get_event_loop()
    loop.run_until_complete(server)
    print("Websocket alive")

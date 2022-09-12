from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
app = FastAPI()

app.mount("/", StaticFiles(directory="static/", html=True), name="static")
    
@app.get("/config/")
async def config(interface: str=None, channel: str=None):
    print(interface)
    print(channel)

    return {"config": "Accepted config"}
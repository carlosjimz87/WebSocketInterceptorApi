from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import PlainTextResponse

app = FastAPI()

EXPECTED = "demo-token-123"

def extract_token(headers: dict, query: dict) -> str | None:
    auth = headers.get("authorization")
    if auth and auth.lower().startswith("bearer "):
        return auth.split(" ", 1)[1].strip()
    # browser-friendly fallback: ws://.../ws?token=...
    return query.get("token")

@app.websocket("/ws")
async def ws_endpoint(ws: WebSocket):
    await ws.accept()
    # FastAPI exposes headers via scope; also get query params
    token = extract_token(
        {k.decode(): v.decode() for k, v in ws.scope["headers"]},
        ws.query_params,  # Mapping
    )
    print("Received token:", token)

    if token != EXPECTED:
        await ws.close(code=4401)  # custom unauthorized
        return

    await ws.send_text("Welcome! Token accepted.")
    try:
        while True:
            msg = await ws.receive_text()
            await ws.send_text(f"echo: {msg}")
    except WebSocketDisconnect:
        pass

@app.get("/", response_class=PlainTextResponse)
def root():
    return "WS server up. Connect to ws://host:8000/ws"
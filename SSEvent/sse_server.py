from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import asyncio
import uvicorn

app = FastAPI()

@app.get("/sse")
async def sse():
    # Async generator that keeps yielding events
    async def event_generator():
        while True:
            # SSE format: "data: <message>\n\n"
            yield "data: Hello world!\n\n"
            await asyncio.sleep(1.5)  # send every 1.5 seconds

    # Keep the HTTP connection open and stream events
    return StreamingResponse(event_generator(), media_type="text/event-stream")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

# http://127.0.0.1:8000/sse


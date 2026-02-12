from fastapi import FastAPI, Request  # FastAPI framework + request access
import uvicorn  # ASGI server that runs async apps and handles HTTP connections

# Create FastAPI app instance
app = FastAPI()

# POST endpoint that reads a streaming request body
@app.post("/stream")
async def stream(request: Request):

    # request.stream() reads body chunk-by-chunk (async)
    async for chunk in request.stream():

        # Each chunk is bytes → decode to text
        print("Received chunk:", chunk.decode())

    return

# Run the ASGI server if this file is executed directly
if __name__ == "__main__":

    # ASGI server = program that receives HTTP requests
    # and passes them to the async FastAPI app
    uvicorn.run(app, host="127.0.0.1", port=8000)

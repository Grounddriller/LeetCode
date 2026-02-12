# Import time module (used here to pause between chunk sends)
import time

# Import HTTPX (used to send HTTP requests to a server)
import httpx

# Generator that yields parts of the POST body over time
def chunks():
    for part in ["Hello ", "world", "!"]:

        # HTTP body must be bytes → encode string to bytes
        yield part.encode()

        # Pause 0.5 seconds so we can visually see streaming
        time.sleep(0.5)


# Send a POST request to the FastAPI server
response = httpx.post(

    # URL of your local server endpoint
    "http://127.0.0.1:8000/stream",

    # content= accepts a generator → sends body chunk-by-chunk
    content=chunks()
)


# Print the JSON response returned by the server
print(response.json())

from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse
from prometheus_client import Counter, generate_latest
from pytz import timezone
from datetime import datetime

app = FastAPI()

gandalf_counter = Counter("gandalf_requests_total", "Total requests to /gandalf")
colombo_counter = Counter("colombo_requests_total", "Total requests to /colombo")

@app.get("/gandalf")
def serve_gandalf():
    gandalf_counter.inc()
    return FileResponse("gandalf.jpg", media_type="image/jpeg")

@app.get("/colombo")
def get_colombo_time():
    colombo_counter.inc()
    colombo_time = datetime.now(timezone("Asia/Colombo")).strftime("%Y-%m-%d %H:%M:%S")
    return JSONResponse(content={"time": colombo_time})

@app.get("/metrics")
def metrics():
    return generate_latest()

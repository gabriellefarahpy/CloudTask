import redis
import json
import time

r = redis.Redis(host= "localhost", port= 6379, decode_responses= True)

while True:
    _, job_data = r.blpop("job_queue")
    job = json.loads(job_data)
    job_id = job["Id"]

    try:
        r.hset(f"job:{job_id}", "status", "processing") #mark as processing

        payload = job["Payload"]
        result = payload  # simple "processing"

        time.sleep(5)

        r.hset(f"job:{job_id}", mapping={
            "status": "completed",
            "result": result
        }) #mark as completed
    except Exception:
        r.hset(f"job:{job_id}", "status", "failed") #mark as failed
from fastapi import APIRouter
import uuid
import json
import redis

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

router = APIRouter() # new router

@router.post("/jobs")
def create_job(payload: dict):
    """Create a job with a unique ID, add it to Redis queue, and store its status"""
    job_id = str(uuid.uuid4()) # generates a unique job ID
    job_data = {
        "Id": job_id,
        "Payload": json.dumps(payload),  # store payload as JSON string
        "Status": "queued"
    }

    # Pushing to Redis Queue
    r.lpush("job_queue", json.dumps(job_data))

    # Store as a hash in Redis
    r.hset(f"job:{job_id}", mapping=job_data)

    return {"job_id": job_id}

@router.get("/jobs/{job_id}")
def get_job_status(job_id: str):
    """Get status of a job by its ID from Redis"""
    job = r.hgetall(f"job:{job_id}")  # get all fields from hash
    if not job:
        return {"error": "Job not found"}

    # Deserialize payload back to dict
    if "Payload" in job:
        job["Payload"] = json.loads(job["Payload"])
    return job
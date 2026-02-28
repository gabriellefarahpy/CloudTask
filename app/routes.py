from fastapi import APIRouter
import uuid
import json
from app.redis_client import r


router = APIRouter() #new router
@router.post("/jobs")

def create_job(payload:dict):
    """Create a job with a unique ID, add it to Redis queue, and store its status"""
    job_id = str(uuid.uuid4()) #generates a unique job ID
    job_data = {
        "Id":job_id,
        "Payload": payload,
        "Status": "queued" 
    }

    #Pushing to Redis Queue
    r.lpush("job_queue", json.dumps(job_data))

    #Store Status
    r.set(f"job:{job_id}", json.dumps(job_data))

    return {"job_id": job_id}

@router.get("/jobs/{job_id}")
def get_job_status(job_id: str):
    """Get status of a job by its ID from Redis"""
    job = r.get(f"job:{job_id}")
    if not job:
        return {"error": "Job not found"}
    return json.loads(job) #deserialize back to dictionary

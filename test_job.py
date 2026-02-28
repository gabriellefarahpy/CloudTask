import requests

resp = requests.post("http://127.0.0.1:8000/jobs", json={"task":"process data"})
print("Job submitted:", resp.json())

job_id = resp.json()["job_id"]
resp2 = requests.get(f"http://127.0.0.1:8000/jobs/{job_id}")
print("Job status:", resp2.json())
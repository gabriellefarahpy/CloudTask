import redis

r = redis.Redis(host ='host.docker.internal', port=6379, decode_responses=True)
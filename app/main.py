from fastapi import FastAPI
from app.routes import router #import router
app = FastAPI() #Create a FastAPI Instance
app.include_router(router) #include the router so endpoints are available
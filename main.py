import logging
from contextlib import asynccontextmanager
from pydantic import BaseModel
from fastapi import FastAPI
from temporalio.client import Client
from internal.worker.name import GreetingWorkflow
import uvicorn

log = logging.getLogger(__name__)
class NameRequest(BaseModel):
    name: str
@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.info("Setting up temporal client")
    app.state.temporal_client = await Client.connect('localhost:7233')
    yield

app = FastAPI(lifespan=lifespan)

@app.get('/', status_code=200, response_model=dict)
def root():
    return {"hello": "world"}

@app.post('/name', status_code=201, response_model=dict)
async def say_hello(request: NameRequest):
    result = await app.state.temporal_client.execute_workflow(
        GreetingWorkflow.run, request.name, id=f"name-workflow-{request.name}", task_queue='name-task-queue'
    )
    return {
        "result": result
    }
    

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8000)
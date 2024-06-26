import asyncio
import concurrent.futures

from internal.activity.name import say_hello
from internal.worker.name import GreetingWorkflow
from temporalio.client import Client
from temporalio.worker import Worker


async def main() :
    client = await Client.connect('localhost:7233')

    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
        worker = Worker(client, task_queue='name-task-queue', workflows=[GreetingWorkflow], activities=[say_hello], activity_executor=executor)
        await worker.run()

if __name__ == "__main__":
    asyncio.run(main())
from temporalio import workflow
from datetime import timedelta
from internal.activity.name import say_hello

@workflow.defn
class GreetingWorkflow:
    @workflow.run
    async def run(self, name: str) -> str:
        return await workflow.execute_activity(
            say_hello, name, start_to_close_timeout=timedelta(seconds=120)
        )
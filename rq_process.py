from app import create_app


app = create_app()
app.app_context().push()

queue = app.task_queue
job = queue.enqueue('app.tasks.background_job', result_ttl=0)

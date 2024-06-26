# Temporal Worker with FastAPI
create virtual environment
```bash
python -m venv .venv
source .venv/bin/activate
```

Install requirements
```bash
pip install -r requirements.txt
```
**NOTE: TEMPORAL SHOULD BE INSTALLED IN THE VIRTUAL ENVIRONMENT**

Run the temporal server in development mode
```bash
temporal server start-dev
```
Set Python Path and Run the Application

When running your scripts, make sure to set the `PYTHONPATH` so that Python can locate the `internal` module:

```bash
export PYTHONPATH=$(pwd)
```

Run the Temporal worker:

```bash
python internal/worker/run.py
```

Run the FastAPI application:

```bash
python main.py
```

### Test the API

Test the API using `curl` or any HTTP client like Postman:

```bash
curl -X POST "http://127.0.0.1:8000/name" -H "Content-Type: application/json" -d '{"name": "Suresh"}'
```

You should receive a response like:

```json
{
  "result": "Hello Suresh!"
}
```

Check the workflows in the Temporal UI \
http://localhost:8233/namespaces/default/workflows
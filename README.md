# CST Booking System API

A lightweight Flask backend for the CST Booking System assignment. The API exposes a simple JSON homepage route and includes Pytest tests plus a GitHub Actions workflow for CI/CD deployment to Render.

## Project Structure

```text
project/
|-- app.py
|-- test_app.py
|-- requirements.txt
|-- .github/workflows/ci.yml
```

## Setup

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Flask app locally:

```bash
python app.py
```

The app will run on `http://localhost:5000` by default. Render can provide the `PORT` environment variable automatically in production.

## Run Tests Locally

```bash
pytest
```

## GitHub Repository Secret

To store the Render deploy hook URL in GitHub:

1. Open your GitHub repository.
2. Go to `Settings`.
3. Select `Secrets and variables`, then `Actions`.
4. Click `New repository secret`.
5. Set the name to `RENDER_DEPLOY_HOOK_URL`.
6. Paste your Render deploy hook URL as the secret value.
7. Click `Add secret`.

## Render Deployment

To link this repository to Render:

1. Create a new Web Service in Render.
2. Connect your GitHub repository.
3. Use `pip install -r requirements.txt` as the build command.
4. Use `gunicorn app:app` as the start command.
5. Add any required environment variables in Render.
6. Copy the Render deploy hook URL and save it in GitHub as `RENDER_DEPLOY_HOOK_URL`.

After setup, every push to the `main` branch will install dependencies, run tests, and trigger deployment to Render if the tests pass.

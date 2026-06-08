# Simple Flask API

A minimal Flask API with two endpoints:
- `GET /` – returns "Hello World"
- `GET /health` – returns HTTP 200 (empty body)

## Quick Start

### Locally
```bash
pip install -r requirements.txt
python app.py
```

The server starts at `http://0.0.0.0:5000`.

### Docker
```bash
docker build -t flask-api .
docker run -p 5000:5000 flask-api
```

## Testing
```bash
pip install pytest
pytest tests/
```

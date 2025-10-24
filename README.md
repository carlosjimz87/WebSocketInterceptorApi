# WebSocketInterceptor API

This is the API of the [WebSocketInterceptor](https://github.com/carlosjimz87/WebSocketInterceptor) project.

## Requirements

1. Python 3.10+  
2. (Optional) `requirements.txt` for dependencies

## Setup

1. Clone the repository.  
```
git clone https://github.com/yourusername/WebSocketInterceptor.git
cd WebSocketInterceptor
```
2. Create and activate the virtual environment: 

```
python3 -m venv venv
source venv/bin/activate
```
 
3. Install dependencies:

```
pip install -r requirements.txt
```

Or install dependencies manually as needed:

```
pip install "fastapi[all]" "uvicorn[standard]"
```

## Usage

Run scripts or modules directly, for example:  
```
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

Once running, open your browser or WebSocket client and connect to:

[http://127.0.0.1:8000/](ws://127.0.0.1:8000/ws)

To open a WebSocket connection directly, use: 

[ws://127.0.0.1:8000/ws](ws://127.0.0.1:8000/ws)

## Development Notes

Developed with PyCharm. You can open the project and run/debug using PyCharm’s built-in configurations.

## Contributing

Contributions via pull requests are welcome. Keep changes small and document important decisions in commit messages.

## License

This project is open source.

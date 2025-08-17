# FastAPI Request Logger

A simple FastAPI application demonstrating structured logging of incoming HTTP requests using a custom middleware. The project is configured to send logs to both a local file (with daily rotation) and an external log management service (Better Stack).

## Features

- **FastAPI Framework**: A modern, fast (high-performance) web framework for building APIs.
- **Structured Logging**: Logs are formatted as JSON for easy parsing and analysis.
- **Request Middleware**: A custom middleware intercepts all incoming requests to log important details like method, URL, headers, client IP, and processing time.
- **Log Rotation**: The local log file (`logs.log`) is automatically rotated daily, keeping a backup of the last 7 days to prevent excessive disk usage.
- **Cloud Logging**: Integrated with [Better Stack](https://betterstack.com/logtail) for centralized cloud log management.

## Project Structure

```
.
├── src/
│   ├── main.py         # Main application file, defines FastAPI app and endpoints.
│   ├── logger.py       # Configures the application logger (file, stream, and Better Stack).
│   ├── middleware.py   # Contains the request logging middleware.
│   └── logs.log        # Local log file (auto-generated).
├── .env              # Environment variables file (needs to be created).
└── README.md         # This file.
```

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd FastAPI-Logs
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install dependencies:**
    Create a `requirements.txt` file with the following content:
    ```
    fastapi
    uvicorn[standard]
    python-dotenv
    logtail
    ```
    Then, install the dependencies using pip:
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1.  **Create a `.env` file in the root directory:**
    This file will hold your secret token for the Better Stack service.

2.  **Add your `TOKEN` to the `.env` file:**
    Open the `.env` file and add your Better Stack source token like this:
    ```
    TOKEN="your-better-stack-source-token"
    ```

## Running the Application

To run the application, use `uvicorn` from the root directory:

```bash
uvicorn src.main:app --reload
```

The application will be available at `http://127.0.0.1:8000`.

## API Endpoints

The following endpoints are available:

### `GET /`

- **Description:** A simple root endpoint that returns a "Hello World" message.
- **Response (`200 OK`):**
  ```json
  {
    "message": "Hello World"
  }
  ```

### `GET /upload-videos`

- **Description:** A placeholder endpoint for uploading videos.
- **Response (`200 OK`):**
  ```json
  {}
  ```

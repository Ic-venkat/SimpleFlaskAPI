# SimpleFlaskAPI

## Overview

This repository contains a simple Flask API endpoint implemented in `main.py` for handling user data via a POST request. The API validates and saves user information to a JSON file named `dict.json`. The accompanying `test_API.py` script provides a sample test for the API.

## Setup

Before running the Flask API, make sure you have the necessary dependencies installed. You can install them using the following command:

```bash
pip install flask
```

## Running the API

Execute the `main.py` script to start the Flask server:

```bash
python main.py
```

The server will run on `http://127.0.0.1:5000/` by default.

## API Endpoint

### `/users` (POST)

#### Request

- Accepts a JSON payload with user information.
  - Required fields:
    - `name`: User's name (non-empty string, max length: 32 characters).
    - `age`: User's age (numeric value, must be 16 or older).

#### Response

- If the request is valid, the API responds with a success message and a status code of 201 (Created).
- If there's an error in the request or processing, an error message along with a status code of 400 (Bad Request) is returned.

## Error Handling

In case of exceptions during request processing, the API returns a JSON-formatted error message containing the exception traceback and a status code of 400.

## Test

The `test_API.py` script provides a basic test for the API. Run it using the following command:

```bash
python test_API.py
```

## Note

- The user data is saved in a JSON file named `dict.json`.
- The `save` function is used to save the JSON data.

Feel free to customize and extend the API based on your requirements.

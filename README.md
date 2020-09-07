# Suggestic Code Challenge - API

## Getting Started

### Pre-requisites

In order to use and install this software, the following requisites must be present in your computer:

- Python v3.8.5+
  > Type in your terminal `python --version` to check current version. On absence of its installation, please follow [these instructions](https://www.python.org/downloads/) to proceed.

### Environment Variables

This software depends on environment variables being provisioned to work properly. These variables are defined as referred below:

| Name            | Description                                            | Example                     |
| --------------- | ------------------------------------------------------ | --------------------------- |
| `HOST`          | Server url where run this project.                     | `127.0.0.1`                 |
| `PORT`          | Port on which Python - Flask process would run.        | `5000`                      |
| `DEBUG`         | Decide whether to see log errors.                      | `True`                      |
| `ENVIRONMENT`   | Environment features.                                  | `development`               |

### Installation

1. Clone this repo.
   ```sh
   $ git clone https://github.com/rotcax/sugg-challenge.git
   ```
2. Hop onto the project folder.
   ```sh
   $ cd sugg-challenge
   ```
3. Create virtual environment.
   ```sh
   $ python -m venv envname
   ```
4. Active virtual environment.
   ```sh
   $ source envname/bin/activate
   ```
5. Install Project dependencies.
   ```sh
   $ pip install -r requirements.txt
   ```
6. Copy `.env.example` file as `.env`.
   ```sh
   $ cp .env.example .env
   ```
7. Edit the new file, `.env` with your favorite IDe or editor, to replace and/or add the required environment variables as correspond.
   ```env
   HOST=127.0.0.1
   PORT=5000

   DEBUG=True
   ENVIRONMENT=development
   ```
8. Execute the application.
   ```sh
   $ python run.py
   ```
9. Make request to `http://127.0.0.1:5000/`, replacing the port number by whatever you have provided as the environment variable `PORT`.


### Examples
```json
// Input
{ "items": [1, 2, 3, 4, 5, 6, 7, 8] }

// Output
{ "result": [1, 2, 3, 4, 5, 6, 7, 8] }

// Input 
{ "items": [1, [2, 3], [4, 5], [6], 7, 8] }

// Output
{ "result": [1, 2, 3, 4, 5, 6, 7, 8] }

// Input 
{ "items": [1, [2, 3], [4, 5], [6], 7, 8] }

// Output
{ "result": [1, 2, [3, 4, [5, 6], 7], 8] }
```

> Happy Coding

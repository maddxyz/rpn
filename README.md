# RPN Calculator API

This project implements a Reverse Polish Notation (RPN) calculator as a RESTful API using Flask. It allows users to create and manage multiple stacks, push numerical values onto them, and apply various mathematical operators.

## Features

-   Create and manage multiple independent RPN stacks.
-   Push numerical values onto a specified stack.
-   Apply basic arithmetic operators (+, -, *, /) to the values on a stack.
-   Retrieve the current state of a stack.
-   List all active stacks.
-   Delete a stack.
-   Interactive API documentation via Swagger UI.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

-   Python 3.10+
-   pip (Python package installer)

### Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd rpn
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**

    -   **On Windows:**

        ```bash
        .\venv\Scripts\activate
        ```

    -   **On macOS/Linux:**

        ```bash
        source venv/bin/activate
        ```

4.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

To start the Flask development server:

```bash
python app.py
```

The API will be accessible at `http://127.0.0.1:5000`.

### API Documentation (Swagger UI)

Once the application is running, you can access the interactive API documentation at:

`http://127.0.0.1:5000/swagger/`

This interface allows you to explore all available endpoints and test them directly from your browser.

### Running Tests

To run the unit tests for the project:

```bash
python -m unittest
```

## Project Structure

```
. # Project Root
├── app.py              # Main Flask application entry point
├── config/             # Configuration files
│   ├── operators.py    # Defines supported operators
│   └── swagger_config.py # Swagger UI configuration
├── routes/             # API route definitions (Blueprints)
│   ├── __init__.py
│   ├── op_routes.py    # Operator-related endpoints
│   └── stack_routes.py # Stack management endpoints
├── services/           # Business logic and core functionalities
│   └── stack_manager.py # Manages RPN stack operations
├── tests/              # Unit tests
│   ├── test_app.py
│   ├── routes/
│   │   ├── test_op_routes.py
│   │   └── test_stack_routes.py
│   └── services/
│       └── test_stack_manager.py
├── .gitignore          # Specifies intentionally untracked files to ignore
├── requirements.txt    # Python dependencies
├── roadmap.md          # Future development roadmap
└── todo.md             # List of improvements and technical debt
```

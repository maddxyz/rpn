# RPN Calculator - TODO List

This document outlines potential improvements and shortcuts taken due to time constraints.

## Good Practices Implemented

-   **Modular Project Structure:** The project is well-organized with separate folders for `routes`, `services`, and `config`, promoting maintainability and separation of concerns.
-   **Use of Flask Blueprints:** API endpoints are organized using Flask Blueprints (`op_bp`, `stack_bp`), which enhances modularity and allows for better management of routes.
-   **Unit Testing:** The project includes a `tests` directory with unit tests (`test_op_routes.py`, `test_stack_manager.py`, etc.), demonstrating a commitment to testing and ensuring code correctness.
-   **Configuration Management:** Application configuration (like `SWAGGER_CONFIG` and `OPERATORS`) is externalized into dedicated files within the `config` folder, making it easier to manage and modify settings.
-   **Clear API Endpoints:** The API endpoints are clearly defined and follow a logical structure (e.g., `/rpn/op`, `/rpn/stack`).
-   **Dependency Injection (Implicit):** The `StackManager` is instantiated once and used across routes, which is a form of dependency management.
-   **Singleton Pattern for StackManager:** The `StackManager` is implemented as a singleton, ensuring a single, consistent state for all stack operations across the application.

## Shortcuts & Technical Debt

-   **No Security Implemented:** The application lacks any form of authentication, authorization, or other security measures.
-   **Limited Functionality:** Only basic RPN operations are supported, and stack persistence is not implemented.
-   **AI-Assisted Test Generation:** Initial tests were generated with AI assistance and required manual modification to fit project specifics and ensure correctness.
-   **Enhanced Observability:** Current logging is minimal; expanding it would unlock deeper insights into application behavior and streamline debugging.

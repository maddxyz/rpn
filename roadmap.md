# RPN Calculator - Future Roadmap (Backlog v1.0)

This document outlines potential future functionalities and improvements for the RPN Calculator project, serving as a preliminary backlog.

## Core Functionality Enhancements

### 1. Expanded Operator Set
-   **Power (`^` or `**`):** Add support for exponentiation.
-   **Square Root (`sqrt`):** Implement a square root operator.
-   **Logarithms (`log`, `ln`):** Introduce natural and base-10 logarithm functions.
-   **Trigonometric Functions (`sin`, `cos`, `tan`):** Add basic trigonometric operations.

### 2. Stack Manipulation Commands
-   **Swap (`swap`):** Exchange the top two elements on the stack.
-   **Duplicate (`dup`):** Duplicate the top element on the stack.
-   **Drop (`drop`):** Remove the top element from the stack.
-   **Clear (`clear`):** Empty the entire stack.
-   **Roll (`roll`):** Reorder elements within the stack.

### 3. Stack Persistence
-   **Save Stack:** Implement functionality to save the current state of a stack to a persistent storage (e.g., file, database).
-   **Load Stack:** Allow loading a previously saved stack by its ID.
-   **List Saved Stacks:** Provide an endpoint to list all available saved stacks.

## User Experience & Interface

### 4. Command-Line Interface (CLI) Improvements
-   **Interactive Mode:** Develop a more interactive CLI where users can continuously input operations and see the stack state.
-   **History:** Implement command history for easier recall and re-execution.

### 5. Basic Web User Interface (Optional - if time permits)
-   **Simple Input Field:** A web page with an input field for numbers and operators.
-   **Stack Display:** Dynamically display the current stack contents.
-   **Buttons for Operators:** Visual buttons for common operations.

## Robustness & Error Handling

### 6. Enhanced Input Validation
-   More specific error messages for invalid inputs (e.g., non-numeric input where a number is expected).
-   Handle division by zero gracefully.

### 7. Undo/Redo Functionality
-   Allow users to undo the last operation.
-   Allow users to redo an undone operation.

## Technical Debt & Refactoring

### 8. Code Documentation
-   Add comprehensive docstrings to all functions and classes.
-   Improve inline comments for complex logic.

### 9. Unit Test Coverage
-   Increase unit test coverage for all new and existing functionalities.
-   Implement integration tests for API endpoints.

### 10. Configuration Management
-   Externalize more configuration parameters (e.g., storage paths, default stack size).

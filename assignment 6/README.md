# Simple Calculator

A simple, graphical calculator application built with Python's `tkinter` library. This project provides a user-friendly interface for performing basic arithmetic calculations.

## Features

*   **Standard Arithmetic Operations:** Addition (`+`), Subtraction (`-`), Multiplication (`*`), and Division (`/`).
*   **Clear Functionality:** A 'C' button to clear the current input and results.
*   **Responsive Interface:** The calculator layout is organized in a grid for easy use.
*   **Error Handling:** Displays "Error" for invalid mathematical expressions (e.g., division by zero).

## How to Run

1.  **Prerequisites:** Ensure you have Python 3.x installed on your system. The `tkinter` library is included with most Python installations.
2.  **Execution:** Open your terminal or command prompt, navigate to the project directory, and run the following command:

```bash
python calcu.py
```

A window will open with the calculator interface.

## Code Structure

The application is contained within a single file, `calcu.py`, and uses the `tkinter` library for the GUI.

*   **Initialization:**
    *   `root = Tk()`: Creates the main application window.
    *   `root.geometry()` and `root.configure()`: Sets the window size and background color.
    *   `e = Entry(...)`: Creates the display screen for numbers and results.

*   **Core Functions:**
    *   `button_click(number)`: Appends the clicked number or operator to the display.
    *   `button_clear()`: Clears the entire display.
    *   `button_equal()`: Evaluates the expression in the display using `eval()`. It includes a basic `try...except` block for error handling.

*   **Button Layout:**
    *   A list of tuples `buttons` defines the text, row, and column for each button on the calculator.
    *   A `for` loop iterates through this list to create and place each `Button` widget in the grid layout. Special styling and commands are applied to the '=' and 'C' buttons.

*   **Main Loop:**
    *   `root.mainloop()`: Starts the `tkinter` event loop, which waits for user interaction (e.g., button clicks).

## Contributing

Contributions are welcome! If you have ideas for improvements or find any bugs, feel free to open an issue or submit a pull request.
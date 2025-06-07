# Calculator Project

This project implements a simple calculator application that performs basic arithmetic operations, including addition, subtraction, multiplication, and division. It is part of the "100 Days of Python" challenge.

## Features

- **Basic arithmetic operations:** Addition, subtraction, multiplication, and division.
- **Chaining calculations:** Continue calculations using the result as the starting number.
- **Interactive interface:** User-friendly prompts for entering numbers and selecting operations.
- **Clear display:** Clears the terminal when starting a new calculation session.
- **ASCII Art Logo:** Displays an ASCII art logo on startup (defined in `art.py`).

## How to Run

1. Ensure that Python is installed on your system.
2. Run the application with the following command:

    ```sh
    python main.py
    ```

3. Follow the on-screen prompts to perform your calculations.

## File Structure

- **main.py:** Contains the main logic for the calculator, including functions for arithmetic operations and the calculation flow.
- **art.py:** Contains the ASCII art logo that is displayed when the calculator starts.

## Notes

- Input prompts are minimal (e.g., `float(input(""))`), so ensure you know the expected input.
- Calculations are chained by using the previous result as the starting number of the next operation.

## Acknowledgments

This project is inspired by the "100 Days of Python" challenge.
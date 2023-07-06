# Python OOP Calculator

This project implements a simple calculator using object-oriented programming (OOP) principles in Python. The calculator is capable of performing basic arithmetic operations (addition, subtraction, multiplication, division), as well as some advanced operations (square, square root, power).

## Motivation

The main motivation behind this project was to enhance my Python and OOP skills. I have been learning Python for 2 weeks and wanted to implement a practical project to apply and reinforce the concepts I've learned. A classmate mentioned he had learned a lot from creating a calculator using OOP, and it sounded like a great exercise to me as well.

## Classes Overview

### Calculation

This class holds the logic for the mathematical operations the calculator can perform. Each method in this class performs a specific calculation and updates the `result` attribute.

### InputHandler

This class handles user input for each operation. It uses the methods from the `Calculation` class to perform operations based on user input and manages the calculator's memory.

### Calculator

This class creates an instance of the `InputHandler` and controls the main loop of the application. It displays the menu to the user and calls the appropriate method on the `InputHandler` based on user input.

### TestCalculation

This class contains unit tests for the `Calculation` class. It uses Python's built-in `unittest` library to assert the equality of the expected and actual output of each method in the `Calculation` class.

## How to Run the Project

You can run this calculator by navigating to the directory containing the project files in your terminal and typing `python app.py`.

## Unit Tests

To run the unit tests for this project, navigate to the directory containing the project files in your terminal and type `python test_calculation.py`.

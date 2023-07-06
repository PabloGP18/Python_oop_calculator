
# The Calculation class handles the main math operations of the calculator. 
class Calculation:
    def __init__(self, memory = 0):
        # Initialize result
        self.result = float(memory)

    # basic mathematical operations
    def add(self, number):
        self.result += number
        return self.result
    
    def substract(self, number):
        self.result -= number
        return self.result
    
    def multiply(self, number):
        self.result *= number
        return self.result
    
    def divide(self, number):
        # Handle division by zero
        if number == 0:
            print("Error: Division by zero is not allowed.")
            return
        else:
            self.result /= number
            return self.result
        
    # Perform advanced math operations
    def square(self, number):
        # Handle negative input
        if number < 0:
            print("Error: Square root of negative number is not defined.")
            return
        self.result = number ** 2 
        return self.result
    
    def pow(self, base, exponent):
        self.result = base ** exponent
        return self.result

    
    def sqrt(self, number):
        # Handle negative input
        if number < 0:
            print("Error: Square root of negative number is not possible in real numbers.")
            return
        else:
            self.result = number ** 0.5
            return self.result
    
    # Reset calculator
    def reset_memory(self):
        self.result = 0

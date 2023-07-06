from calculation import Calculation

class InputHandler:
    def __init__(self, memory = 0):
        # Initialize calculation handler
        self.memory = memory
        self.calculation = Calculation(self.memory)
    
    def _handle_input(self, operation):
        # Handle user input for most operations
        while True:
            num = input(f"Enter a number to {operation} ('b' to go back to the menu or 'c' to clear the memory): ")
            if num.lower() == 'b':
                return
            elif num.lower() == 'c':
                self.calculation.reset_memory()
                continue

            # Ensure the user input is a number
            try:
                num = float(num)
            except Exception as e:  # catches all types of exceptions
                print(f"Invalid input.Error {e}. try again.")
                continue

            if operation == 'add':
                result = self.calculation.add(num)
            elif operation == 'substract':
                result = self.calculation.substract(num)
            elif operation == 'multiply':
                result = self.calculation.multiply(num)
            elif operation == 'divide':
                result = self.calculation.divide(num)
            elif operation == 'square':
                result = self.calculation.square(num)
            elif operation == 'square root':
                result = self.calculation.sqrt(num)
            elif operation == 'pow':
                result = self.calculation.pow(num)
            print(f"Current total: {result}")
    
    def _handle_input_pow(self, operation):
        # Handle user input for 'pow' operation
        while True:
            base_num = input(f"Enter the base number to {operation} ('b' to go back to the menu or 'c' to clear the memory): ")
            if base_num.lower() == 'b':
                return 
            elif base_num.lower() == 'c':
                self.calculation.reset_memory()
                continue
            # Ensure the user input is a number
            try:
                base_num = float(base_num)
            except Exception as e:  # catches all types of exceptions
                print(f"Invalid input.Error {e}. try again.")
                continue

            exp_num = input(f"Enter the exponent to {operation} ('b' to go back to the menu or 'c' to clear the memory): ")
            if exp_num.lower() == 'b':
                return
            elif exp_num.lower() == 'c':
                self.calculation.reset_memory()
                continue
            # Ensure the user input is a number
            try:
                exp_num = float(exp_num)
            except Exception as e:  # catches all types of exceptions
                print(f"Invalid input.Error {e}. try again.")
                continue
            if operation == 'pow':
                result = self.calculation.pow(base_num,exp_num)
            print(f"Current total: {result}")

    # Process specific operations
    def add(self):
        self._handle_input('add')

    def substract(self):
        self._handle_input('substract')
    
    def multiply(self):
        self._handle_input('multiply')

    def divide(self):
        self._handle_input('divide')

    def square(self):
        self._handle_input('square')

    def sqrt(self):
        self._handle_input('square root')

    def pow(self):
        self._handle_input_pow('pow')


        
    


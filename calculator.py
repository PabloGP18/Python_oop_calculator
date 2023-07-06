from inputHandler import InputHandler

class Calculator:

    def __init__(self):
        # Initialize input handler
        self.inputHandler = InputHandler()
    
    def run(self):
        # Main calculator loop
        run_program = True
        while run_program:
            print("Welcome to this awesome OOP calculator! Wat kind of calculation do you want to do?")
            choice = input("You can choose between:\n 1. add \n 2. substract \n 3. multiply \n 4. divide \n 5. square \n 6. square root \n 7. power \n 8. exit \n Enter your choice:")

            try:
                choice
            except Exception as e:  # catches all types of exceptions
                print(f"Invalid input.Error {e}. try again.")
                break
            
            # Process user choice
            while True:
                if choice == "1":
                   self.inputHandler.add()
                   break
                elif choice == "2":
                    self.inputHandler.substract()
                    break
                elif choice == "3":
                    self.inputHandler.multiply()
                    break  
                elif choice == "4":
                    self.inputHandler.divide()
                    break
                elif choice == "5":
                    self.inputHandler.square()
                    break
                elif choice == "6":
                    self.inputHandler.sqrt()
                    break
                elif choice == "7":
                    self.inputHandler.pow()
                    break
                # elif choice == "8":
                #     Calculation.reset_memory()
                elif choice == "8":
                    print("Exit calculator program")
                    run_program = False
                    break
                else:
                    print("wrong input. Please try again.")
                    break
 
                                                                                              
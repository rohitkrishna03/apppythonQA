def calculator():
    print("Simple Calculator")
    print("Enter 'C' to clear the calculator.")
    print("Enter 'Q' to quit.")
    
    current_value = 0
    operator = None
    
    while True:
        button = input("Enter a number, operator (+, -, *, /), or command (C, Q): ").strip()
        
        if button.lower() == 'q':
            print("Exiting calculator...")
            break
        
        if button.lower() == 'c':
            current_value = 0
            operator = None
            print("Screen cleared.")
            continue
        
        if button in '+-*/':
            operator = button
        else:
            try:
                value = float(button)
                if operator is None:
                    current_value = value
                else:
                    if operator == '+':
                        current_value += value
                    elif operator == '-':
                        current_value -= value
                    elif operator == '*':
                        current_value *= value
                    elif operator == '/':
                        if value != 0:
                            current_value /= value
                        else:
                            print("Cannot divide by zero!")
                    operator = None
                
                print(f"Screen: {current_value}")
            except ValueError:
                print("Invalid input. Please enter a number or operator.")
    
calculator()

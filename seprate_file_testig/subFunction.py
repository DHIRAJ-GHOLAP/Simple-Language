import os

def Print_function(userl):   
    if "say" in userl:
        print(userl[4:].strip(), "\n")

def Clear_function(userl):
    if "cls" in userl[0:4] or "clear" in userl:
        os.system("clear" if os.name != "nt" else "cls")
        print("""
                                            Welcome to the Simple language
                                            Developed by Dhiraj Gholap
                                            DM Dhiraj For Source code
                                            Instagram id - dhiraj._._._
    """)

def add_numbers():
    while True:
        total = 0
        try:
            num_to_add = int(input("Enter the number to add: "))
            if num_to_add <= 0:
                print("Please enter a positive number.")
                return

            for i in range(num_to_add):
                user_input = input(f"Enter number {i+1}: ")
                try:
                    number = int(user_input)
                    total += number
                except ValueError:
                    print("Invalid input! Please enter a valid number.")
                    return

            print(f"The sum of the entered numbers is: {total}")

        except ValueError:
            print("Invalid input! Please enter a valid number.")

def oprator_function(user, Variable_Dictionary):
    import re
    # Match basic expressions like '10 + 20', 'x * 5', etc.
    match = re.search(r"([a-zA-Z0-9.]+)\s*([\+\-\*/])\s*([a-zA-Z0-9.]+)", user)
    if match:
        left_val = match.group(1).strip()
        op = match.group(2)
        right_val = match.group(3).strip()

        def get_val(v):
            if v.replace(".", "", 1).isdigit():
                if "." in v:
                    return float(v)
                return int(v)
            if v in Variable_Dictionary:
                return Variable_Dictionary[v]
            return None

        val1 = get_val(left_val)
        val2 = get_val(right_val)

        if val1 is None or val2 is None:
            # Maybe it's just a single number/variable, but the regex matched something else or failed
            return

        if op == "+":
            print(val1 + val2)
        elif op == "-":
            print(val1 - val2)
        elif op == "*":
            print(val1 * val2)
        elif op == "/":
            if val2 == 0:
                print("Error: Division by zero")
            else:
                print(val1 / val2)
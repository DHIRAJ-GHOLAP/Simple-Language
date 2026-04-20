import os
import subFunction as tools

"""
        Welcome to the Simple language
        Developed by Dhiraj Gholap
        DM Dhiraj For Source code
        Instagram id - dhiraj._._._
    """

# List_Of_Keywords = {"number input add":0,"variable name is":0,"say":0,"cls":0,"if ":0,"tell value of ":0,"and value is":0}

def variable_assign(line, variables):
    if 'variable name is ' in line:
        variable_info = line.split("variable name is ")[1].split(" and value is ")
        
        variable_name = variable_info[0].strip()
        variable_value = variable_info[1].strip()

        # Check if the input value is an integer
        if variable_value.isdigit():
            variables[variable_name] = int(variable_value)
        # Check if the input value is a float
        elif "." in variable_value and all(char.isdigit() or char == "." for char in variable_value):
            variables[variable_name] = float(variable_value)
        else:
            # If the value is not a number, store it as a string
            variables[variable_name] = variable_value

def say_value_of_variable(line, variables):
    if "tell value of " in line:
        variable_name = line.split("tell value of ")[1].strip()

        if variable_name in variables:
            print(f"The value of the variable {variable_name} is {variables[variable_name]}")
            # print(type(variables[variable_name]))
        else:
            print(f"The variable {variable_name} is not defined.")
# this is main function
def main():
    # Use 'clear' for Linux/Unix and 'cls' for Windows
    os.system("clear" if os.name != "nt" else "cls")
   
    Variable_Dictionary = {}
    Line_Number = 0

##################################################################################
#                          File reading section Section                          # 
##################################################################################

    if not os.path.exists("Demo.simple"):
        print("Error: Demo.simple not found.")
        return

    with open("Demo.simple", "r") as file:
        code_lines = file.readlines()

    for line in code_lines:
        Line_Number += 1
        line = line.strip().lower()

        if not line or line.startswith("#"):
            continue

        if line == "system fad denge":
            break

        if "say" in line:
            tools.Print_function(line)
            continue

        if "cls" in line or "clear" in line:
            tools.Clear_function(line)
            continue

        if "variable name is" in line:
            variable_assign(line, Variable_Dictionary)
            continue

        if "tell value of" in line:
            say_value_of_variable(line, Variable_Dictionary)
            continue

        # If it doesn't match the above, try arithmetic
        if any(op in line for op in ["+", "-", "*", "/"]):
            tools.oprator_function(line, Variable_Dictionary)

if __name__ == "__main__":
    main()
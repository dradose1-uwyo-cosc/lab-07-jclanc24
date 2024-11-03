# Your Name Here
# UWYO COSC 1010
# Submission Date
# Lab XX
# Lab Section: 
# Sources, people worked with, help given to: 
# your
# comments
# here


# Prompt the user for an upper bound 
# Write a while loop that gives the factorial of that upper bound
# This will need to be a positive number
# For this you will need to check to ensure that the user entered a number
    # To do so you can use the methods `.isdigit()` or `.isnumeric()`
    # If a user did not enter a number output a statement saying so
# You will continue to prompt the user until a proper integer value is entered

def factorial(ubound):
    fact_sum = 1
    fact_temp = int(ubound)

    while fact_temp > 0:
        fact_sum *= fact_temp
        fact_temp -= 1

    return fact_sum




def working_sum(isum):
    cumulative_sum = 0
    cumulative_sum += int(isum)

    return cumulative_sum




class calculator:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2
    
    def add(number1, number2):
        return number1 + number2

    def subtract(number1, number2):
        return number1 - number2
    
    def multiply(number1, number2):
        return number1 * number2
    
    def divide(number1, number2):
        return number1 / number2
    
    def remainder(number1, number2):
        return number1 % number2
    



#PROGRAM START
print("*"*75)
print("\t\t\t\tLAB 07")
print("*"*75)
while True:
    upper_bound = (input("Please input the upperbound: "))
    if upper_bound.isdigit():
        if int(upper_bound) > 0:
            output_factorial = factorial(upper_bound)
            break

        elif int(upper_bound) == 0:
            output_factorial = 1
            break

        else:
            print("ERROR: Please enter a positive integer!")
    else:
        print("ERROR: Please enter an integer!")
    
print(f"The factorial value is : {output_factorial}")
print("*"*75)

#PART TWO
output_sum = 0

while True:
    user_sum = (input("Input an arbitraty number of positive or negative integers: "))
    if user_sum.isdigit():
        if int(user_sum) > 0:
            output_sum += working_sum(user_sum)

    elif "-" in user_sum:
            user_sum.rstrip("-")
            sum_temp = int(user_sum)
            sum_temp*-1
            output_sum += working_sum(sum_temp)

    elif user_sum.lower() == "quit" or user_sum.lower() == "exit":
        print(f"Final Sum: {output_sum}")
        break
    
    else: 
        print("Please only enter integers for this program.")

# Create a while loop that prompts a user for input of an integer values
# Sum all inputs. When the user enters 'exit' (regardless of casing) end the loop
# Upon ending the loop print the sum
# Your program should accept both positive and negative input
# Remember all inputs from stdin are strings, so you will need to convert the string to an int first
# Before you convert the number you need to check to ensure that it is a numeric string
    # To do so you can use the methods `.isdigit()` or `.isnumeric()`
    # This will return true if every digit in your string is a numerical character
    # However, that means a string such as `-1` would return false, even though your program should accept negative values
    # This means you will need to have a check to see if `-` is first character of the string before you check if it is numerical
    # If it is in the string you will need to remove the `-` character, and know that it will be a negative number, so a subtraction from the overall sum
    # I recommend checking out: https://www.w3schools.com/python/ref_string_replace.asp to figure out how one may remove a character from a string
# All this together means you will have an intensive while loop that includes multiple if statements, likely with some nesting 
# The sum should start at 0 

#PART THREE

print("*"*75)
print("\t\t\t\tCALCULATOR")
print("*"*75)




# Now you will be creating a two operand calculator
# It will support the following operators: +,-,/,*,% 
# So accepted input is of the form `operand operator operand` 
# You can assume that the user is competent and will only input strings of that form 
# You will again need to verify that the operands are numerical values
# For this assume only positive integers will be entered, no need look for negative numbers 
# You will need to check the string for which operator it contains
# Once you do, you will need to remove the operands from the string
# This can be done in multiple ways:
    # You can go through the string in a loop and create a substring of the characters until an operator is reached
        # Upon reaching the operator you will switch to another substring and add all characters following to the second new string 
    # Alternatively you can use the `.split()` method to split the string around an operator: https://www.w3schools.com/python/ref_string_split.asp
# Your program will need to work with whatever spacing is given  
    # So, it should function the same for `5 + 6` as `5+6`
# Print the result of the equation
# Again, loop through prompting the user for input until `exit` in any casing is input 


numbers= []

while True:
    calc_input = input("Using two numbers, please type your mathematical expression: ")
    calc_output = 0

    if "+" in calc_input:
        calc_temp = calc_input.split("+")
        for num in calc_temp:
            num.strip()
            numbers.append(int(num))
        calc_output = calculator.add(numbers[0],numbers[1])

    elif "-" in calc_input:
        calc_temp = calc_input.split("-")
        for num in calc_temp:
            num.strip()
            numbers.append(int(num))
        calc_output = calculator.subtract(numbers[0],numbers[1])
    
    elif "*" in calc_input:
        calc_temp = calc_input.split("*")
        for num in calc_temp:
            num.strip()
            numbers.append(int(num))
        calc_output = calculator.multiply(numbers[0],numbers[1])

    elif "/" in calc_input:
        calc_temp = calc_input.split("/")
        for num in calc_temp:
            num.strip()
            numbers.append(int(num))
        calc_output = calculator.divide(numbers[0],numbers[1])

    elif "%" in calc_input:
        calc_temp = calc_input.split("%")
        for num in calc_temp:
            num.strip()
            numbers.append(int(num))
        calc_output = calculator.remainder(numbers[0],numbers[1])
    
    elif calc_input.lower() == "quit" or calc_input.lower() == "exit":
        print("Goodbye.")
        break

    else:
        print("Error: You are using mathematical expressions or negative integers that are not defined!\nPlease try again.")

    print(f"Ouput: {calc_output}")
    del numbers[:]
    calc_output = 0






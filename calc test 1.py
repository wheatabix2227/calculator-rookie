# Simple calculator

# Start of addition function
def addition(NumberA, NumberB):
    return NumberA + NumberB
# End of addition function

# Start of subtraction function

def subtraction(NumberA, NumberB):
    return NumberA - NumberB

# End of subtraction function

# Start of multiplication function

def multiplication(NumberA, NumberB):
    return NumberA * NumberB

# End of multiplication function

# Start of division function

def division(NumberA, NumberB):
    return NumberA / NumberB

# End of division function

# Start of DIV function

def DIV(NumberA, NumberB):
    return NumberA // NumberB

# End of DIV function

# Start of MOD function

def MOD(NumberA, NumberB):
    return NumberA % NumberB

# End of MOD function

def main():
# Main program
# Ask users for input
       NumberAInput = float(input("Enter the first number: "))
       NumberBInput = float(input("Enter the second number: "))
       UserChoice = input("To add press 'a', to subtract press 's', to multiply  number press 'm', to divide  number press 'd', to divide  number to closest whole  type 'div',to find remainder type 'mod': ")

       # Call function based on user choice
       UserChoice = UserChoice.upper()
       if UserChoice == "A":
           print(addition(NumberAInput, NumberBInput))
           main()
       elif UserChoice == "S":
           print(subtraction(NumberAInput, NumberBInput))
           main()
       elif UserChoice == "M":
           print(multiplication(NumberAInput, NumberBInput))
           main()
       elif UserChoice == "D":
           print(division(NubmerAInput, NumberBInput))
           main()
       elif UserChoice == "DIV":
           print(DIV(NumberAInput, NumberBInput))
           main()
       elif UserChoice == "MOD":
           print(MOD(NumberAInput, NumberBInput))
           main()
       else:
           main()


main()           

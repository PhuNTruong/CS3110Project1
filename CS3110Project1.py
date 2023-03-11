import time
#According to 2.4.5 Integer literals
#decinteger ::= nonzerodigit (["_"] digit)* | "0"+ (["_"] "0")*
#octinteger ::=  "0" ("o" | "O") (["_"] octdigit)+
#hexinteger ::=  "0" ("x" | "X") (["_"] hexdigit)+


def isDecimalInt(userInput):
    # Checks if the input string is an empty string
    if len(userInput) == 0:
        return False
    
    # Do we need to check for +/- signs?

    # Do we need to check for letters?

    # Checks if the first number is 0, because
    # decinteger is a nonzero number followed by any amount of numbers
    # or 0, followed by any amount of 0's
    # Ex: so input can be 000, but not 001
    if len(userInput) > 1 and userInput[0] == '0' and userInput:
        return False
    # if input is 000, it will be wrong, this needs to be fixed.
    
    # If no checks fail, then it is a valid decimal integer
    return True


test = input("Enter the input string: ")
print(test)

if isDecimalInt(test) == True:
    print("Test is a valid decimal integer")
else:
    print("Test is not a valid decimal integer")

#Example Tests
print(isDecimalInt("")) # False, since its just a space
print(isDecimalInt("12356")) # True
print(isDecimalInt("012345")) # False, because leading 0 followed by nonzeros
print(isDecimalInt("0")) # True
print(isDecimalInt("0000")) # Should be True, but I'm getting false


time.sleep(2) # just so the executable shows the result

import time
#According to 2.4.5 Integer literals
# The alphabet is (+,-,integers 0-9)
#decinteger ::= nonzerodigit (["_"] digit)* | "0"+ (["_"] "0")*
#octinteger ::=  "0" ("o" | "O") (["_"] octdigit)+
#hexinteger ::=  "0" ("x" | "X") (["_"] hexdigit)+

#process : check if empty, remove +/- from string if there, check for letters, check for leading zeros

def isDecimalInt(userInput):
    # Checks if the input string is an empty string
    if len(userInput) == 0:
        return False
    
    # +/- are part of the alphabet
    # but not needed in the literals so remove em
    if userInput[0] == "+" or userInput[0] == "-":
        userInput = userInput[1:] # UserInput is starts at index 1 instead of 0, thus removing +/-

    # Do we need to check for letters?

    # Checks if the first number is 0, because
    # decinteger is a nonzero number followed by any amount of numbers
    # or 0, followed by any amount of 0's
    # Ex: so input can be 000, but not 001
    if len(userInput) > 1 and userInput[0] == '0':
        return False
    
    if userInput[0] == "0":
        for x in userInput:
            if x != 0 or x!= "_":
                return False;

    # if input is 000, it will be wrong, this needs to be fixed.


    
    # If no checks fail, then it is a valid decimal integer
    return True


test = input("Enter the input string: ")

print(test) # Test to print out input string

print(test[0]); # Test to print out first element



if isDecimalInt(test) == True:
    print(test + " is a valid decimal integer")
else:
    print(test + " is not a valid decimal integer")

#Example Tests
print(isDecimalInt("")) # False, since its just a space
print(isDecimalInt("12356")) # True
print(isDecimalInt("+123")) # True
print(isDecimalInt("012345")) # False, because leading 0 followed by nonzeros
print(isDecimalInt("0")) # True
print(isDecimalInt("0000")) # Should be True, but I'm getting false


time.sleep(2) # just so the executable shows the result

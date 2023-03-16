#According to 2.4.5 Integer literals
# The alphabet is (+,-,integers 0-9)
#decinteger ::= nonzerodigit (["_"] digit)* | "0"+ (["_"] "0")*
#decinteger are (1-9)(["_"] 0-9)* or 0+(["_"] "0")*
#Underscores are ignored for determining the numeric value of the literal.
#One underscore can occur between digits
#leading zeros in a non-zero decimal number are not allowed

#process : check if empty, remove +/- from string if there, check for letters, check for leading zeros

def isDecimalInt(userInput):
    # Checks if the input string is an empty string
    if len(userInput) == 0:
        return False
    
    # +/- are part of the alphabet
    # but not needed in the literals so remove em
    if userInput[0] == "+" or userInput[0] == "-":
        userInput = userInput[1:] # UserInput is starts at index 1 instead of 0, thus removing +/-


    #check if 0th element is 0, because
    # we need to check for leading zeros
    # if input is 000, it will be wrong, this needs to be fixed.
    # This is a WIP
    if len(userInput) > 1 and userInput[0] == '0':
        return False
    
    # or if len(UserInput) = 1 and userInput[0] == '0'
    # means that it would only accept the input: "0"
    
    if userInput[0] == "0":
        for x in userInput:
            # if the first digit is 0 then the next characters
            # can only be more 0's or an underscore
            if x != 0 or x!= "_": 
                return False;

        # Need to add if condition to check for multiple underscores in a row like 1__1




    
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


#According to 2.4.5 Integer literals
# The alphabet is ("_" and integers 0-9)
#decinteger ::= nonzerodigit (["_"] digit)* | "0"+ (["_"] "0")*
#decinteger are (1-9)(["_"] 0-9)* or 0+(["_"] "0")*
#Underscores are ignored for determining the numeric value of the literal.
#One underscore can occur between digits
#leading zeros in a non-zero decimal number are not allowed

def isDecimalInt(userInput):
    # Checking for +/- and if the string is empty isn't required
    # We assume the string to be 20 characters or less
    # Switching over to case statements for better formatting

    state = 0; # Start at state 0
    accepted_states = (0,);
    for x in userInput:
        match state:
            case 0: # if input is 0
                if x == '0':
                    state = 1; # then the NFA moves to state 1
                else:
                    state = 0;
            case 1:
                if x == '1': # if input is 0 - 9
                    state = 1; # it remains in state 1

    
    # 1 of 3 routes nfa could go
    # check if 0th element is 0, because
    # we need to check for leading zeros
    #if userInput[0] == "0":
    #    for x in userInput:
    #        # if the first digit is 0 then the next characters
    #        # can only be more 0's or an underscore
     #       if x != 0 or x!= "_": 
     #           return False;


    # 2 of 3 routes nfa could go
    #if userInput[0] == "_":
    #    return False;


    # 3 of 3 routes nfa could go
    #if userInput[0] == [1-9]
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


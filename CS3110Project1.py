1#According to 2.4.5 Integer literals
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
                else: #state 10 is placeholder error state
                    state = 10; # if the input is not 0, then it moves into an error state since its not accepted. 
            case 1: # if input is 1-9
                if x in [(userInput(x) for x in range(0,10))]: 
                    state = 1; # it remains in state 1
                elif x == '0':
                    state = 1;
            case 2: # if input is "_" aka underscore
                if x == '0':
                    state = 9;
            case 3:
                state = 3;
            case 4:
                state = 4;
            case 5:
                state = 5;
    print(state in accepted_states)

    
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

isDecimalInt(test);



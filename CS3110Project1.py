#According to 2.4.5 Integer literals
# The alphabet is ("_" and integers 0-9)
#decinteger ::= nonzerodigit (["_"] digit)* | "0"+ (["_"] "0")*
#decinteger are (1-9)(["_"] 0-9)* or 0+(["_"] "0")*
#Underscores are ignored for determining the numeric value of the literal.
#One underscore can occur between digits
#leading zeros in a non-zero decimal number are not allowed

# Constants using python sets
BIN_DIGIT = {'0', '1'}
OCT_DIGIT = {str(x) for x in range(1, 8)}
DEC_DIGIT = {str(x) for x in range(1, 10)}
HEX_DIGIT = DEC_DIGIT.union({'A', 'B', 'C', 'D', 'E', 'F', 'a', 'b', 'c', 'd', 'e', 'f'})

def isDecimalInt(userInput):
    # Checking for +/- and if the string is empty isn't required
    # We assume the string to be 20 characters or less
    # Switching over to case statements for better formatting

    state = 0; # Start at state 0
    accepted_states = (1,3,);
    for x in userInput:
        match state:
            case 0: 
                # if input is 0, go to q1
                # if input is 1-9, go to q3
                # if input is "_" go to q4
                if x == '0':
                    state = 1;
                elif x in [(userInput(x) for x in range(1,10))]: 
                    state = 3;
                elif x == '_':
                    state = 4;
            
            case 1: 
                # if input is 0, stay in q1
                # if input is 1-9, go to q2
                if x == '0':
                    state = 1;
                elif x in [(userInput(x) for x in range(1,10))]:
                    state = 2;
            
            case 2: 
                # Once here, any input will still remain here
                state = 2;
                
            case 3: 
                # if input is 0-9, stays in q3
                # If input is "_", go to q5
                if x in [(userInput(x) for x in range(0,10))]:
                    state = 3;
                elif x == '_':
                    state = 5;
                
            case 4: 
                # Once here, any input will still remain here
                state = 4;
            
            case 5:
                # if input is 0-9, go to q3
                # if input is "_", go to q4
                if x in [(userInput(x) for x in range(0,10))]:
                    state = 3;
                elif x == '_':
                    state = 4;

    return(state in accepted_states)

# End of isDecimalInt definition

test = input("Enter the input string: ")

if(isDecimalInt(test)) == True:
    print(test + " is a valid Python decimal integer literal.")
else:
    print(test + " is not a valid Python decimal integer literal.")



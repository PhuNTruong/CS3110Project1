#According to 2.4.5 Integer literals
# The alphabet is ("_" and integers 0-9)
#decinteger ::= nonzerodigit (["_"] digit)* | "0"+ (["_"] "0")*
#decinteger are (1-9)(["_"] 0-9)* or 0+(["_"] "0")*
#Underscores are ignored for determining the numeric value of the literal.
#One underscore can occur between digits
#leading zeros in a non-zero decimal number are not allowed

# Constants using python sets
BIN_DIGIT = {'0', '1'}
OCT_DIGIT = {str(x) for x in range(0, 8)}
NON_ZERO_DEC_DIGIT = {str(x) for x in range(1, 10)}
DEC_DIGIT = NON_ZERO_DEC_DIGIT.union({'0'})
HEX_DIGIT = DEC_DIGIT.union({'A', 'B', 'C', 'D', 'E', 'F', 'a', 'b', 'c', 'd', 'e', 'f'})

def isDecimalInt(userInput):
    # Checking for +/- and if the string is empty isn't required
    # We assume the string to be 20 characters or less
    # Switching over to case statements for better formatting

    state = 0   # Start at state 0
    accepted_states = {1, 3}   # set of accepted states
    for x in userInput:
        match state:
            case 0:
                # if input is 0, go to q1
                # if input is 1-9, go to q3
                # otherwise reject
                if x == '0':
                    state = 1
                elif x in NON_ZERO_DEC_DIGIT:
                    state = 3
                else:
                    state = 'null'
            case 1:
                # stay in 1 if x is 0
                # go to 2 if underscore
                # otherwise reject
                if x == '0':
                    state = 1
                elif x == '_':
                    state = 2
                else:
                    state = 'null'
            case 2:
                # go back to 1 if x is 0
                # otherwise reject
                if x == '0':
                    state = 1
                else:
                    state = 'null'
            case 3:
                # if input is 0-9, stays in q3
                # If input is "_", go to q5
                # reject anything else
                if x in DEC_DIGIT:
                    state = 3
                elif x == '_':
                    state = 5
                else:
                    state = 'null'
            case 5:
                # if input is 0-9, go to q3
                # if input is "_", reject
                if x in DEC_DIGIT:
                    state = 3;
                elif x == '_':
                    state = 'null';
                else:
                    state = 'null'
            case 'null':
                # null state, do nothing
                pass

    return(state in accepted_states)

# End of isDecimalInt definition


# since the NFAs for binary, octal, and hexadecimal are structurally
# identical (the only difference being the accepted chars), we have
# decided to merge them into one method that checks for all 3
def isBinOctHexInt(userInput: str):
    if isNInt(userInput, BIN_DIGIT, {'b', 'B'}):
        return 'binary'
    elif isNInt(userInput, OCT_DIGIT, {'o', 'O'}):
        return 'octal'
    elif isNInt(userInput, HEX_DIGIT, {'x', 'X'}):
        return 'hexadecimal'
    else:
        return ''


def isNInt(userInput: str, digits: set, keyChars: set):
    state = 0
    accepted_states = {3}
    for x in userInput:
        match state:
            case 0:
                # if 0 go to state 1 (bin/oct/hex int has to start with 0)
                # if anything else go to null state
                if x == '0':
                    state = 1
                else:
                    state = 'null'
            case 1:
                # if key char (eg 'o', 'B', or 'x') go to next state
                # if anything else go to null state
                if x in keyChars:
                    state = 2
                else:
                    state = 'null'
            case 2:
                # if we get a valid digit go to 3 (accept state)
                # otherwise reject
                if x in digits:
                    state = 3
                else:
                    state = 'null'
            case 3:
                # if we get a valid digit stay in 3 (accept state)
                # if underscore go to state 2 (need another valid digit
                #   after to be accepted
                # reject if other chars
                if x in digits:
                    state = 3
                elif x == '_':
                    state = 2
                else:
                    state = 'null'
            case 'null':
                # do nothing
                pass

    return state in accepted_states


test = input("Enter the input string: ")

if(isDecimalInt(test)) == True:
    print(test + " is a valid Python decimal integer literal ✅")
else:
    print(test + " is not a valid Python decimal integer literal ❌")

binOctHex = isBinOctHexInt(test)

if binOctHex == 'binary':
    print(test + " is a valid Python binary integer literal ✅")
else:
    print(test + " is not a valid Python binary integer literal ❌")

if binOctHex == 'octal':
    print(test + " is a valid Python octal integer literal ✅")
else:
    print(test + " is not a valid Python octal integer literal ❌")

if binOctHex == 'hexadecimal':
    print(test + " is a valid Python hexadecimal integer literal ✅")
else:
    print(test + " is not a valid Python hexadecimal integer literal ❌")


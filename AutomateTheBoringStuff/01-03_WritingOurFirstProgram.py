# This program says hello and asks for my name
# pound signs (#) is the symbol used to add comments. Anything after will not be ran as code.
print('Hello world!') # the print function prints all text in parenthesis.
# ask for their name
print('What is your name?')
myName = input() # the input() function waits for an input and enter and the variable will evaluate to the input
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName)) # len-gth takes the string arguement and evaluates to the integer value of the string.
# ask for their age
print('What is your age?') 
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')
# str-ing function converts its values into text i.e. str(1234) will be text value '1234'
# int-egar function converts its values into integers i.e. int('1234') will be integar value 1234
# float function converts its values into floating numbers

# print cannot use integers or floating values without converting into string values (text)

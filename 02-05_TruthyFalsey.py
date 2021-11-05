print('Enter a name.')
name = input()
if name != '': # int(0) and float(0.0) is falsey, everything else is truthy
    print('Thank you for entering a name')
else:
    print('You did not enter a name') # blank string is falsey, everytrhing else is truthy

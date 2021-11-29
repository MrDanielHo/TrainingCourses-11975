# def div42by(divideBy):
#     try:
#         return 42/divideBy
#     except ZeroDivisionError:
#         print('Error you cannot divide by zero.')

# print(div42by(2))
# print(div42by(15))
# print(div42by(0))
# print(div42by(6))

numCats = input('How many cats do you have?\n')
try:
    if int(numCats) >= 4: # if entering an alphabetical string, it will return a ValueError
        print('That is a lot of cats.')
    else:
        print('That is not many cats.')
except ValueError: # this will run the below if the error is encountered.
    print('Please enter a number.')
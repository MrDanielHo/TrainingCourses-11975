spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue
    print('spam is ' + str(spam))
# The continue line returns the program to the beginning of the loop.
# ''spam is 3'' does not get printed.
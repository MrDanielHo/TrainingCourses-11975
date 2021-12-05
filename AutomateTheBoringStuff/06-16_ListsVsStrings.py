'''
Similarities between
Lists and Strings
'''

# greetings = 'Hello!'
# print(list(greetings))
# print(greetings[2:4])
# print('ll' in greetings)
# for letter in greetings:
#     print(letter)

'''
Lists are mutable - can be changed

Strings are immutable - cannot be changed.
New strings can be greated that add a previous string with more detail
'''

# name = 'Daniel a human'
# print(name)

# newName = name[0:5] + ' the ' + name[9:]
# print(newName)

'''
The difference between immutable and mutable comes up with "references"
'''
# Strings are immutable. When cheese is equal to spam, the string value of cheese does not change when spam is changed:

# spam = 42
# cheese = spam
# spam = 100

# print(spam)
# print(cheese)


# Lists are mutable: when cheese is equal to the list spam and we make changes to cheese, it will change the list, referenced in memory:

# spam = [0,1,2,3,4,5]
# cheese = spam
# cheese [1] = 'Hello!'
# print(spam)

'''
Passing lists in Function calls.
Though the below function is in a local scope, it makes changes in the memory at the global scale.
'''

# def eggs(cheese):
#     cheese.append('Hello')

# spam = [1,2,3,4,5]
# eggs(spam)
# print(spam)

'''
With the copy module, we can create a new memory reference to a list, instead of using the same memory reference.
This allows us to copy a list and make changes to it, without changing the original list. 
'''

# import copy
# spam = ['A','B','C','D']
# cheese = copy.deepcopy(spam)
# cheese[1] = 42

# print(spam)
# print(cheese)

'''
Line Continuation
'''
spam = ['apples',
        'pears',
        'bananas',
        'berries']

print(spam)

# The below forward slash tells the code to ignore the new line and indentations.
print('Four score and '+\
    'seven years')


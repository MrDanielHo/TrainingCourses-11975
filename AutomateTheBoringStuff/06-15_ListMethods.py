'''
Methods, and the List Methods:
index(), append(), insert(), remove(), sort()
'''

spam = ['hello', 'hi', 'howdy', 'heya']
# print(spam.index('hello')) # find where the word 'hello' is in the variable spam

spam.append('bonjour') # Adds to the end
print(spam)

spam.insert(2,'Guten Tag') # Adds to the corresponding index
print(spam)

spam.remove('hello')
print(spam)

del spam [2]
print(spam)

spam.sort() # Sorts the list ASCII-betical meaning upper case first. Will not sort with integers.
print(spam)

spam.sort(reverse=True)
print(spam)

spam.sort(key=str.lower) # Sorts list after passing the strings in lower case.
print(spam)
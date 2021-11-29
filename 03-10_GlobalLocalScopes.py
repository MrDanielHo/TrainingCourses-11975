'''
1. Code in the global scope cannot use any local variables
2. Code in a local scope can access global variables.
3. Code in one function's local scope cannot use variables from another local scope.
4. The same names for variables can be used in one local scope without affecting a different local scope.
'''
spam = 42 # global variable
eggs = "scrambled" # global variable
def ham():
    spam = "Mearning of life" # local variable 
    global eggs # global variable
    eggs = "sunny"

print(spam)
print(eggs)
ham()
print(spam)
print(eggs)
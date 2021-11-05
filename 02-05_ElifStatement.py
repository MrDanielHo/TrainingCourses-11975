name = 'Bob'
age = 3000
if name == 'Alice': # if name is not Alice move to next condition
    print('Hi Alice')
elif age < 12: # if age is less than 12
    print('You\'re not Alice, child')
elif age > 1000: # if age is greater than 12 and is also greater than 1000
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100: # if age is less than 12 and less than 1000
    print('You are not Alice, gramps.')

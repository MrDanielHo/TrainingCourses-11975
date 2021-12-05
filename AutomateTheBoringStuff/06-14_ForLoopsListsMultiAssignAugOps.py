'''
for Loops with Lists
Multiple Assignment
Augmented Assignment Operators
'''

# for i in range (4):
#     print(i)

# for i in [0,1,2,3]:
#     print (i)


# list4 = range(4)
# for i in list4:
#     print (i)

# guessList = ['Bobby', 'Derek', 'Kath', 'Pidgeon', 'Geoff']
# for i in guessList:
#     print(f'Hello {i}!\n')

# supplies = ['pens','gun', 'staplers', 'paperclips', 'binders']
# for i in range(len(supplies)):
#     print(f'Index {i} in supplies is: {supplies[i]}')

# cat = ['fat', 'orange', 'loud']
# print(cat)
# size, colour, disposition = cat
# print(size)
# print(colour)
# print(disposition)
'''
The above code can be longform written as:
size = cat[0]
colour = cat[1]
disposition = cat[2]
'''
# size, colour, disposition = 'Skinny', 'Black', 'Quiet'
# print(size)
# print(colour)
# print(disposition)

'''
Swapping variables is as easy as the below:
'''

aaa = 'AAA'
bbb = 'BBB'

print(aaa)
print(bbb)

aaa, bbb = bbb, aaa

print(aaa)
print(bbb)
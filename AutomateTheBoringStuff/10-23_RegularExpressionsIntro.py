'''
Regular expressions are equivalent to using CTRL+F.
Except they search for a pattern of text rather than something specific.
e.g. a telelphone number.
'''

import re

# Example: A non-regular expression

# def isPhoneNumber(text):
#     if len(text) != 12:
#         return False #  not a US/Can phone number
#     for i in range(0,3):
#         if not text[i].isdecimal():
#             return False # no area code
#     if text[3] != '-':
#         return False # missing dash
#     if i in range (4,7):
#         if not text[i].isdecimal():
#             return False # no first 3 digits
#     if text[7] != '-':
#         return False # missing second dash
#     for i in range(8,12):
#         if not text[i].isdecimal():
#             return False # missing last 4 digits
#     return True            

# print(isPhoneNumber('415-555-1234'))

message = 'call me at 415-555-1011 tomorrow, or at 415-555-9999 today.'
# message = 'call me at 415-555-101 tomorrow, or at 415-55-9999 today.'

# foundNumber = False
# for i in range(len(message)):
#     chunk = message[i:i+12]
#     if isPhoneNumber(chunk):
#         print(f'phone number found: {chunk}')
#         foundNumber = True
# if not foundNumber:
#     print('Could not find a phone number')


phoneNumberRegularExpression = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
matchedObject = phoneNumberRegularExpression.search(message) # for first instance
print(matchedObject.group())

print(phoneNumberRegularExpression.findall(message)) # for all instances


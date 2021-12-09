import re

# message01 = 'my number is 415-555-4242'

# phoneNumberRegularExpression = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# matchedObject = phoneNumberRegularExpression.search(message01)
# print(matchedObject.group())

# phoneNumberRegularExpression = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)') # Use parenthesis to mark groups from your regular expressions.
# matchedObject = phoneNumberRegularExpression.search(message01)
# print(matchedObject.group(1,2))


# message02 = 'my number is (415) 555-4242'

# phoneNumberRegularExpressionDash = re.compile(r'\(\d\d\d\) (\d\d\d-\d\d\d\d)') # Searching for numbers in format: (415) 555-7891
# matchedObject = phoneNumberRegularExpressionDash.search(message02)
# print(matchedObject.group())

'''
Using the Pipe "|" character
'''

batRegeX = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegeX.search('Batmobile lost a wheel')
print(mo.group())

mo = batRegeX.search('Batcycle lost a wheel')
print(mo.group())
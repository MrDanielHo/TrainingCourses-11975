'''
Matching a certain number of repetitions i.e. 1 or more, 7 or less, etc.
? = None or once
* = None or more
+ = Once or more
{x} = Exactly x amount
{x,y} = between x and y occurances - longest string possible
{x,} = minimum of x occurances
{,y} = maximum of y occurances
{x,y}? = non-greedy match - shortest string possible
'''

import re

# We are looking for either Batman or Batwoman.
# The question mark (?) denotes the string in parenthesis to be optional.
# It can appear once or not at all.
# If searching for a "?", we use the escape character (\), producing r'Dinner\?'

# batRegeX = re.compile(r'Bat(wo)?man')
# mo = batRegeX.search('The Adventures of Batwoman')
# print(mo.group())


# We are looking for an North American Number with optional region code

# phoneRegeX = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
# mo = phoneRegeX.search('My number is 415-555-1234. Call me.')
# print(mo.group())
# mo = phoneRegeX.search('My number is 555-1234. Call me.')
# print(mo.group())


# Looking for either Batman or Batwoman.
# But the "wo" part we are looking for 0 or multiple times, we use *
# If searching for a "*", we use the escape character (\), producing r'\*'

# batRegeX = re.compile(r'Bat(wo)*man')
# mo = batRegeX.search('The Adventures of Batwowowowowowoman')
# print(mo.group())


# If we want to looking for one or more times, we use the "+"

# batRegeX = re.compile(r'Bat(wo)+man')
# mo = batRegeX.search('The Adventures of Batwowowowowowoman')
# print(mo.group())


# Escaping characters
# regex = re.compile(r'\+\*\?')
# mo = regex.search('I learned about +*? regex syntax')
# print(mo.group())

# regex = re.compile(r'(\+\*\?)+')
# mo = regex.search('I learned about +*?+*?+*? regex syntax')
# print(mo.group())

# mo = regex.search('I learned about ?+*? regex syntax')
# print(f"Does the message contain more than one repetition of '?+*'? {mo.group() == False}")


# Exact number of repetitions with the expression {x}

# haRegex = re.compile(r'(Ha){3}')
# mo = haRegex.search('He said "HaHaHa"')
# print(mo.group())

# phoneRegeX = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')
# mo = phoneRegeX.search('My numbers are 555-157-8888,555-158-9999,555-156-7777')
# print(mo.group())


# Range of repetitions with the expression {x,y}

# haRegex = re.compile(r'(Ha){3,5}')

# mo = haRegex.search('He said "HaHaHaHaHa"')
# print(mo.group())

# mo = haRegex.search('He said "HaHaHaHa"')
# print(mo.group())

# mo = haRegex.search('He said "HaHaHa"')
# print(mo.group())

# haRegex = re.compile(r'(Ha){3,}')
# mo = haRegex.search('He said "HaHaHaHaHaHaHaHaHaHa"')
# print(mo.group())


# The below is a greedy match.
# The search will try to match with the maximum number if possible.

# digitRegeX = re.compile(r'(\d){3,5}')
# mo = digitRegeX.search('123456789')
# print(mo.group())


# The below is a non-greedy match.

# digitRegeX = re.compile(r'(\d){3,5}?')
# mo = digitRegeX.search('123456789')
# print(mo.group())
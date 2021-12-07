# spam = 'Hello World!'
# print(spam.upper())
# print(spam.lower())
# print(spam)

'''
Strings are case sensitive.
'''
# answer = 'YES'
# print(answer == 'yes')
# print(answer.lower() == 'yes')
# print(f'Is variable "answer" islower()? {answer.islower()}')
# print(f'Is variable "answer" isupper()? {answer.isupper()}')

# print(f'''The return value of the string ' "hello".upper().isupper ' is {"hello".upper().isupper()} ''')

'''
isalpha()   letters only
isalnum()   letters and numbers only
isdecimal() numbers only
isspace()   whitespace only
istitle()   titlecase only
'''
# movieName = "It's a wonderful wORLD"
# print(movieName.title())
# print(movieName)

'''
startswith('string')
endswith('string')
'''
# contactNumber = "01908555555"
# print(f'''UK region codes starts with 0. Does our contact number begin with an 0? {contactNumber.startswith('0')}''')

'''
the join() method
the split() method
'''
# print(', '.join(['cats','bats','rats']))
# print("Hello it's me".split('i'))

'''
ljust()
center()
rjust()
'''
# print(f"{'hello?'.ljust(15,'+')}{'hello?'.center(8)}{'hello?'.rjust(15,'-')}")

'''
strip()     removes all outer white space
rstrip()    removes outer right white space
lstrip()    removes outer left white space
'''
hello = 'greetings and salutations'.center(50)
print(f"{hello.strip()}")

userName = "                    TheGreek                    "
print("|" + userName.strip() + "|")
print("|" + userName.lstrip() + "|")
print("|" + userName.rstrip() + "|")

print("5321432145Hello12354Goodbye5123542135154".strip("12345"))

print("5321432145Hello12345Goodbye5123542135154".replace("12345","ABCDE"))


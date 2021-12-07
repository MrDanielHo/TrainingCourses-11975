'''
String Formatting
'''
name = 'Alice'
place = 'Main Street'
time = '6 pm'
food = 'burgers'
# print('Hello ' + name + ', you are invited to a party at ' + place + ' at ' + time + '. Please bring ' + food + '.' )

# Using conversion specifiers
print('Hello %s, you are invited to a party at %s at %s. Please bring %s.' % (name, place, time, food))

# Using format print
print(f'Hello {name}, you are invited to a party at {place} at {time}. Please bring {food}.')
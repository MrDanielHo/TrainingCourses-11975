# cat = {'name': 'Alfred', 'age': 5, 'colour': 'yellow'}
# allCats = []
# allCats.append({'name': 'Alfred', 'age': 5, 'colour': 'yellow'})
# allCats.append({'name': 'Paris', 'age': 4, 'colour': 'ginger'})
# allCats.append({'name': 'Skinny-P', 'age': 9, 'colour': 'white'})
# allCats.append({'name': '???', 'age': 0, 'colour': 'black'})
# print(allCats)

'''
Tic-Tac-Toe
'''
import pprint

def printBoard(board):
    print(f'''{board["topLeft"]}|{board["topMiddle"]}|{board["topRight"]}''')
    print('-+-+-')
    print(f'''{board["middleLeft"]}|{board["middleMiddle"]}|{board["middleRight"]}''')
    print('-+-+-')
    print(f'''{board["bottomLeft"]}|{board["bottomMiddle"]}|{board["bottomRight"]}''')

theBoard = {'topLeft': ' ', 'topMiddle': ' ', 'topRight': ' ','middleLeft': ' ', 'middleMiddle': ' ', 'middleRight': ' ','bottomLeft': ' ', 'bottomMiddle': ' ', 'bottomRight': ' ',}
theBoard['middleMiddle'] = 'X'
theBoard['topLeft'] = 'X'
theBoard['topMiddle'] = 'O'
theBoard['topRight'] = 'O'
theBoard['middleLeft'] = 'O'
theBoard['bottomRight'] = 'X'

printBoard(theBoard)

print(f'''42 is a {type(42)}''')
print(f'''Word is a {type('Word')}''')
print(f'''theBoard is a {type(theBoard)}''')
print(f'''theBoard['topLeft'] is a {type(theBoard['topLeft'])}''')
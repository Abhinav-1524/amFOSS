
pieces = {'wking':1,'wqueen':1, 'wpawn':8 , 'wbishop': 2, 'wknight':2, 'wrook':2,'bking':1,'bqueen':1, 'bpawn':8 , 'bbishop': 2, 'bknight':2, 'brook':2}
chess_board={}
for i in range (1,9):
    for j in range(8):
        chess_board.setdefault(str(i)+ str(chr(97 + j)),pieces)

board =  {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
board_keys=list(board)
board_values=list(board.values())

 

def isValidChessBoard():
    for a in range(len(board_keys)-1):
        if (board_keys[a]==board_keys[a+1]):
            return False
    for b in range(len(board_values)-1):
        if(board_values[b]==board_values[b+1]):
            return False
    
    for i in board :
        if (i in chess_board):
            return True
        else:
            return False

    
isValidChessBoard()
print(isValidChessBoard())










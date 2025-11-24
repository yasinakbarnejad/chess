Board = [['R', 'N', 'B', 'Q', 'K', 'B', 'N','R'],
         ['P', 'P', 'P', 'P', 'P', 'P', 'P','P'],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
         ['P', 'P', 'P', 'P', 'P', 'P', 'P','P'],
         ['R', 'N', 'B', 'Q', 'K', 'B', 'N','R'],
         ]
numberize = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
def Translate(text:str):
    noted = [0, 0]
    if(text[0] in numberize):
        noted[1]= numberize[text[0]]
    else:
        print(text[0])
        raise NameError
    noted[0]=int(text[1])
    return tuple(noted)
def Update_board(text1:str, text2: str):
    start, finish = Translate(text1), Translate(text2) 
    Board[8-finish[0]][finish[1]-1] = Board[8-start[0]][start[1]-1]
    Board[8-start[0]][start[1]-1] = ' '
def piece_name(pos:tuple):
    piece = Board[8-pos[0]][pos[1]-1]
    return piece
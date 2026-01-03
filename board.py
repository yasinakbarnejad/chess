import pieces as pi  
Board = []
def make_board():
    global Board
    Board = [[pi.Rook("black", (8,1)), pi.Knight("black",(8,2)), pi.Bishop("black",(8,3)), pi.Queen("black", (8,4)), pi.King("black", (8,5)), pi.Bishop("black",(8,6)), pi.Knight("black",(8,7)),pi.Rook("black", (8,8))],
            [pi.Pawn("black", (7,1)), pi.Pawn("black", (7,2)), pi.Pawn("black", (7,3)), pi.Pawn("black", (7,4)), pi.Pawn("black", (7,5)), pi.Pawn("black", (7,6)), pi.Pawn("black", (7,7)),pi.Pawn("black", (7,8))],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
            [pi.Pawn("white", (2,1)), pi.Pawn("white", (2,2)), pi.Pawn("white", (2,3)), pi.Pawn("white", (2,4)), pi.Pawn("white", (2,5)), pi.Pawn("white", (2,6)), pi.Pawn("white", (2,7)),pi.Pawn("white", (2,8))],
            [pi.Rook("white",(1,1)), pi.Knight("white",(1,2)), pi.Bishop("white",(1,3)), pi.Queen("white", (1,4)), pi.King("black", (1,5)), pi.Bishop("white",(1,6)), pi.Knight("white",(1,7)),pi.Rook("white",(1,8))],
            ]
numberize = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
def Translate(text:str):
    noted = [0, 0]
    if(text[0] in numberize):
        noted[1]= numberize[text[0]]
    else:
        raise NameError
    noted[0]=int(text[1])
    return tuple(noted)
def Update_board(text1:str, text2: str):
    global Board
    start, finish = Translate(text1), Translate(text2) 
    Board[8-finish[0]][finish[1]-1] = Board[8-start[0]][start[1]-1]
    Board[8-start[0]][start[1]-1] = ' '
    
def piece_name(pos:tuple):
    global Board
    piece = Board[8-pos[0]][pos[1]-1]
    return piece
def validate(turn):
    global Board
    white_moves = []
    black_moves = []
    for row in Board:
        for square in row:
            if square!=" ":
                li = square.make_move()
                if square.color=="white":
                    white_moves.extend(li)
                else:
                    black_moves.extend(li)
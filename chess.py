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
def Move(start:str, finish:str):
    temp = Board[int(finish[1])-1][numberize[finish[0]]-1]
    Board[int(finish[1])-1][numberize[finish[0]]-1] = Board[int(start[1])-1][numberize[start[0]]-1]
    Board[int(start[1])-1][numberize[start[0]]-1] = temp
print(Board)
Move("a2","a4")
Move("e8", "d4")
print(Board)
    
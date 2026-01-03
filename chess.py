import legal_move
import board
On = True
board.make_board()
turn = 0
turns = {0: "white", 1:"black"}
board.validate(turns[turn])
while(On):
    text = input()
    if(text=="quit"):
        On=False
        break
    notation = tuple(text.split())
    if(legal_move.is_Legal(notation[0],notation[1], turns[turn]) == True):
        board.Update_board(notation[0], notation[1])
        turn = 1-turn
        board.validate(turn)
        
    for lines in board.Board:
        print(lines)

    

    
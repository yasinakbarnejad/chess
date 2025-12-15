import legal_move
import board
On = True
while(On):
    text = input()
    if(text=="quit"):
        On=False
        break
    notation = tuple(text.split())
    if(legal_move.is_Legal(notation[0],notation[1]) == True):
        board.Update_board(notation[0], notation[1])
    for lines in board.Board:
        print(lines)

    

    
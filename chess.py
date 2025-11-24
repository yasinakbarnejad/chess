from legal_move import pieces
import board
On = True
game = pieces()
while(On):
    text = input()
    if(text=="quit"):
        On=False
        break
    notation = tuple(text.split())
    if(game.is_Legal(notation[0],notation[1])):
        board.Update_board(notation[0], notation[1])
    for lines in board.Board:
        print(lines)

    

    
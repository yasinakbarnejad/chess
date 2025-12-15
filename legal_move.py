import board
import pieces as pi
def is_Legal(pos1, pos2):
    pos1, pos2 = board.Translate(pos1), board.Translate(pos2)
    if not(1<=pos1[0]<=8 and 1<=pos1[1]<=8 and 1<= pos2[0]<=8 and 1<=pos2[1]<=8):
            return "Invalid position"
    piece_kind = board.piece_name(pos1)
    if type(piece_kind) in [pi.Rook, pi.Bishop, pi.Knight, pi.Queen, pi.King, pi.Pawn]:
        if pos2 in piece_kind.moves:
            piece_kind.move(pos2)
            return True
    else:
        return "Invalid piece"
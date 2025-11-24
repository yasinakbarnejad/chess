import board
class pieces:
    def __init__(self) -> None:
        self.piece_keys = {'P' : self.pawn_move, 
                           'R' : self.rook_move,
                           'B' : self.bishop_moves,
                           'N' : self.knight_moves,
                           'Q' : self.queen_moves,
                           'K' : self.king_moves}
    def king_moves(self, position):
        row, col = position
        moves = []
        direction = [(1,-1),(1,0), (1,1), (0,-1), (0,1), (-1,-1), (-1,0), (-1, 1)]
        for drow, dcol in direction:
            newrow, newcol = row+drow, col+dcol
            if(1<=newrow<=8 and 1<=newcol<=8):
                moves.append((newrow,newcol))
        return moves
    def pawn_move(self, position):
        row, col = position
        moves =[]
        if row>1 and row<8:
            moves.append((row+1, col+1))
            moves.append((row+1, col-1))
        else:
            return "wrong"
        return moves
    def rook_move(self, position):
        row, col = position
        moves =[]
        i =1
        while(0<i<9):
            if(i!=row):
                moves.append((i, col))
            i+=1
        i=1
        while(0<i<9):
            if(i==col):
                i+=1
                continue
            moves.append((row, i))
            i+=1
        return moves
    def bishop_moves(self, position):
        row, col = position
        moves =[]
        direction = [(1,1), (1, -1), (-1, 1), (-1, -1)]
        for dcol, drow in direction:
            for i in range(1,8):
                newrow, newcol = row +drow*i , col + dcol*i
                if(0<newrow<9 and 0<newcol<9):
                    moves.append((newrow,newcol))
                else:
                    break
        return moves
    def knight_moves(self, position):
        row, col = position
        moves =[]
        Lmove = [(2,1), (2, -1), (-2, 1), (-2, -1),(1, 2), (-1, 2), (1, -2), (-1, -2)]
        for mrow, mcol in Lmove:
            newrow, newcol = row+mrow, col+mcol
            if(0<newrow<9 and 0<newcol<9):
                moves.append((newrow, newcol))
        return moves
    def queen_moves(self,position):
        moves = self.rook_move(position) + self.bishop_moves(position)
        return moves
    def get_moves(self, piece_kind, position):
             moves = self.piece_keys[piece_kind](position)
             return moves
    def is_Legal(self,pos1, pos2):
        pos1, pos2 = board.Translate(pos1), board.Translate(pos2)
        piece_kind = board.piece_name(pos1)
        if not(1<=pos1[0]<=8 and 1<=pos1[1]<=8 and 1<= pos2[0]<=8 and 1<=pos2[1]<=8):
            return "Invalid position"
        if piece_kind in self.piece_keys:
            valid_checks = self.get_moves(piece_kind, pos1)
        else:
            return "Invalid piece"
        if valid_checks!= "wrong":
            return pos2 in valid_checks
        else:
            return "Invalid position"
import board
class Pieces():
    def __init__(self, color, position) -> None:
        self.moves = []
        self.color = color
    def move(self,newpos):
        self.row, self.col = newpos
class Rook(Pieces):
    def __init__(self, color, position) -> None:
        super().__init__(color,position)
        self.row, self.col = position
    def __repr__(self) -> str:
        return f"R{self.color[0]}"
    def make_move(self):
        moves = []
        direction = [(1,0), (1, 0), (0, 1), (0, -1)]
        for dcol, drow in direction:
            newrow, newcol = self.row +drow , self.col + dcol
            while 0<newrow<9 and 0<newcol<9:
                boxpiece = board.piece_name((newrow,newcol)) 
                if boxpiece==" ":
                    moves.append((newrow,newcol))
                    newrow+=drow
                    newcol+=dcol
                else:
                    if boxpiece.color!= self.color:
                        moves.append((newrow,newcol))
                    break
        return moves
class Bishop(Pieces):
    def __init__(self, color, position) -> None:
        super().__init__(color,position)
        self.row, self.col = position
    def __repr__(self) -> str:
        return f"B{self.color[0]}"
    def make_move(self):
        moves =[]
        direction = [(1,1), (1, -1), (-1, 1), (-1, -1)]
        for dcol, drow in direction:
            newrow, newcol = self.row +drow , self.col + dcol
            while 0<newrow<9 and 0<newcol<9:
                boxpiece = board.piece_name((newrow,newcol)) 
                if boxpiece==" ":
                    moves.append((newrow,newcol))
                    newrow+=drow
                    newcol+=dcol
                else:
                    if boxpiece.color== self.color:
                        moves.append((newrow,newcol))
                    break
        return moves
class Knight(Pieces):
    def __init__(self, color, position) -> None:
        super().__init__(color,position)
        self.row, self.col = position
    def __repr__(self) -> str:
        return f"N{self.color[0]}"
    def make_move(self):
        moves =[]
        Lmove = [(2,1), (2, -1), (-2, 1), (-2, -1),(1, 2), (-1, 2), (1, -2), (-1, -2)]      
        for dcol, drow in Lmove:
            newrow, newcol = self.row +drow , self.col + dcol
            boxpiece = board.piece_name((newrow,newcol)) 
            if boxpiece==" " or boxpiece.color != self.color:
                moves.append((newrow,newcol))
        return moves
class Queen():
    def __init__(self, color, position) -> None:
        super().__init__(color,position)
        self.row, self.col = position
    def __repr__(self) -> str:
        return f"N{self.color[0]}"
    def make_move(self):
        moves = []
        direction = [(1,1), (1, -1), (-1, 1), (-1, -1)]
        for dcol, drow in direction:
            newrow, newcol = self.row +drow , self.col + dcol
            while 0<newrow<9 and 0<newcol<9:
                boxpiece = board.piece_name((newrow,newcol)) 
                if boxpiece==" ":
                    moves.append((newrow,newcol))
                    newrow+=drow
                    newcol+=dcol
                else:
                    if boxpiece.color== self.color:
                        moves.append((newrow,newcol))
                    break
        direction = [(1,0), (1, 0), (0, 1), (0, -1)]
        for dcol, drow in direction:
            newrow, newcol = self.row +drow , self.col + dcol
            while 0<newrow<9 and 0<newcol<9:
                boxpiece = board.piece_name((newrow,newcol)) 
                if boxpiece==" ":
                    moves.append((newrow,newcol))
                    newrow+=drow
                    newcol+=dcol
                else:
                    if boxpiece.color!= self.color:
                        moves.append((newrow,newcol))
                    break
        return moves
import board as bo
class Pieces():
    def __init__(self, color, position) -> None:
        self.moves = []
        self.color = color
    def move(self,newpos):
        self.row, self.col = newpos
        if type(self) in [Pawn]:
            print(self.moved)
            self.moved = True
class Rook(Pieces):
    def __init__(self, color, position) -> None:
        super().__init__(color,position)
        self.row, self.col = position
    def __repr__(self) -> str:
        return f"R{self.color[0]}"
    def make_move(self):
        self.moves = []
        direction = [(1,0), (1, 0), (0, 1), (0, -1)]
        for dcol, drow in direction:
            newrow, newcol = self.row +drow , self.col + dcol
            while 0<newrow<9 and 0<newcol<9:
                boxpiece = bo.piece_name((newrow,newcol)) 
                if boxpiece==" ":
                    self.moves.append((newrow,newcol))
                    newrow+=drow
                    newcol+=dcol
                else:
                    if boxpiece.color!= self.color:
                        self.moves.append((newrow,newcol))
                    break
        return self.moves
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
                boxpiece = bo.piece_name((newrow,newcol)) 
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
            if 0<newrow<9 and 0<newcol<9:
                boxpiece = bo.piece_name((newrow,newcol))
                if boxpiece==" " or boxpiece.color != self.color:
                    moves.append((newrow,newcol))
        return moves
class Queen(Pieces):
    def __init__(self, color, position) -> None:
        super().__init__(color,position)
        self.row, self.col = position
    def __repr__(self) -> str:
        return f"Q{self.color[0]}"
    def make_move(self):
        moves = []
        direction = [(1,1), (1, -1), (-1, 1), (-1, -1)]
        for dcol, drow in direction:
            newrow, newcol = self.row +drow , self.col + dcol
            while 0<newrow<9 and 0<newcol<9:
                boxpiece = bo.piece_name((newrow,newcol)) 
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
                boxpiece = bo.piece_name((newrow,newcol)) 
                if boxpiece==" ":
                    moves.append((newrow,newcol))
                    newrow+=drow
                    newcol+=dcol
                else:
                    if boxpiece.color!= self.color:
                        moves.append((newrow,newcol))
                    break
        return moves
class King(Pieces):
    def __init__(self, color, position) -> None:
        super().__init__(color,position)
        self.row, self.col = position
    def __repr__(self) -> str:
        return f"K{self.color[0]}"
    def make_move(self):
        moves = []
        direction = []
        direction = [(1,-1),(1,0), (1,1), (0,-1), (0,1), (-1,-1), (-1,0), (-1, 1)]
        for drow, dcol in direction:
            newrow, newcol = self.row+drow, self.col+dcol
            if(1<=newrow<=8 and 1<=newcol<=8):
                boxpiece = bo.piece_name((newrow,newcol))
                if boxpiece==" " or boxpiece.color != self.color:
                    moves.append((newrow,newcol))
        return moves
class Pawn(Pieces):
    def __init__(self, color, position) -> None:
        super().__init__(color,position)
        self.row, self.col = position
        self.moved = False
        self.moves = []
    def __repr__(self) -> str:
        return f"P{self.color[0]}"
    def make_move(self):
        self.moves = []
        if self.color=="white":
            forward = 1
            if self.row==5:
                self.checksides()
        else:
            forward = -1
            if self.row==4:
                self.checksides()
        print(self.row+(1*forward), self.col)
        boxpiece = bo.piece_name((self.row+(1*forward), self.col))
        if boxpiece == " ":
            self.moves.append((self.row+(1*forward), self.col))
        if not self.moved and boxpiece== " " and bo.piece_name((self.row+(2*forward), self.col)) == " ":
            self.moves.append((self.row+(2*forward),self.col))
        for i in (-1,1):
                boxpiece = bo.piece_name((self.row+1,self.col+i))
                if boxpiece!=" " and boxpiece.color!=self.color:
                    self.moves.append((self.row+1,self.col+i))
        return self.moves
    def checksides(self):
            for i in (-1, 1):
                boxpiece = bo.piece_name((self.row,self.col+i))
                if boxpiece!=" " and boxpiece.color!=self.color:
                    self.moves.append((self.row,self.col+i))
        
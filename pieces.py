import pygame

PIECE_SIZE = 60

class Board:
    def __init__(self):
        # initialize and add all pieces to board
        self.white_pieces = [Pawn(0,360,'white'), Pawn(60,360,'white'), 
                             Pawn(120,360,'white'), Pawn(180,360,'white'), 
                             Pawn(240,360,'white'), Pawn(300,360,'white'), 
                             Pawn(360,360,'white'), Pawn(420,360,'white'), 
                             Rook(0,420,'white'), Rook(420,420,'white'), 
                             Knight(60,420,'white'), Knight(360,420,'white'), 
                             Bishop(120,420,'white'), Bishop(300,420,'white'), 
                             Queen(180,420,'white'), King(240,420,'white')]



        self.black_pieces = [Pawn(0,60,'black'), Pawn(60,60,'black'), 
                             Pawn(120,60,'black'), Pawn(180,60,'black'), 
                             Pawn(240,60,'black'), Pawn(300,60,'black'), 
                             Pawn(360,60,'black'), Pawn(420,60,'black'), 
                             Rook(0,0,'black'), Rook(420,0,'black'), 
                             Knight(60,0,'black'), Knight(360,0,'black'), 
                             Bishop(120,0,'black'), Bishop(300,0,'black'), 
                             Queen(180,0,'black'), King(240,0,'black')]

    def move(self, piece, x, y):
        for piece2 in self.white_pieces:
            piece2.find_unfiltered_moves()
        for piece2 in self.black_pieces:
            piece2.find_unfiltered_moves()
        for piece2 in self.white_pieces:
            self.find_allowed_moves(piece2)
        for piece2 in self.black_pieces:
            self.find_allowed_moves(piece2)
        for move in piece.allowed_moves:
            if x == move[0] and y == move[1]:
                piece.x = x
                piece.y = y
                piece.rect = pygame.Rect(piece.x, piece.y, PIECE_SIZE, PIECE_SIZE)
                piece.has_moved = True
                piece.selected = False
                if piece.color == 'black':
                    for piece2 in self.white_pieces:
                        if piece2.x == x and piece2.y == y:
                            self.white_pieces.remove(piece2)
                else:
                    for piece2 in self.black_pieces:
                        if piece2.x == x and piece2.y == y:
                            self.black_pieces.remove(piece2)


    def find_allowed_moves(self, piece):
        piece.allowed_moves = piece.unfiltered_moves
        for move in piece.allowed_moves:
            # check if one of our pieces is in that spot
            if piece.color == 'white':
                for piece2 in self.white_pieces:
                    if move == (piece2.x, piece2.y):
                        piece.allowed_moves.remove(move) 
            else:
                for piece2 in self.black_pieces:
                    if move == (piece2.x, piece2.y):
                        piece.allowed_moves.remove(move)
            # specific piece checks
        for move in piece.allowed_moves:
            if piece.type == 'pawn':
                if piece.color == 'white':
                    if move[0] == piece.x + 60:
                        tag = False
                        for piece2 in self.black_pieces:
                            if piece2.x == move[0] and piece2.y == move[1]:
                                tag = True
                        if tag == False:
                            piece.allowed_moves.remove(move)
                    if move[0] == piece.x - 60:
                        tag = False
                        for piece2 in self.black_pieces:
                            if piece2.x == move[0] and piece2.y == move[1]:
                                tag = True
                        if tag == False:
                            piece.allowed_moves.remove(move)
                else:
                    if move[0] == piece.x + 60:
                        tag = False
                        for piece2 in self.white_pieces:
                            if piece2.x == move[0] and piece2.y == move[1]:
                                tag = True
                        if tag == False:
                            piece.allowed_moves.remove(move)
                    if move[0] == piece.x - 60:
                        tag = False
                        for piece2 in self.white_pieces:
                            if piece2.x == move[0] and piece2.y == move[1]:
                                tag = True
                        if tag == False:
                            piece.allowed_moves.remove(move)

            ##if piece.type == 'bishop' or piece.type == 'queen':

            # if piece.type == 'rook' or piece.type == 'queen' or piece.type == 'pawn':
            #     if move[1] > piece.y + 60:
            #         for i in range(piece.y, move[1], 60):
            #             for piece2 in self.white_pieces:
            #                 if piece2.x == move[0] and piece2.y == i:
            #                     piece.allowed_moves.remove(move)
            #             for piece2 in self.black_pieces:
            #                 if piece2.x == move[0] and piece2.y == i:
            #                     piece.allowed_moves.remove(move)
        



class Pawn:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.type = 'pawn'
        if self.color == 'white':
            self.image = pygame.image.load('Pieces/Chess_plt60.png')
        else:
            self.image = pygame.image.load('Pieces/Chess_pdt60.png')
        self.rect = pygame.Rect(self.x, self.y, PIECE_SIZE, PIECE_SIZE)
        self.selected = False
        self.has_moved = False
        self.allowed_moves = []
        self.unfiltered_moves = []
        self.find_unfiltered_moves()

    def find_unfiltered_moves(self):
        self.unfiltered_moves = []
        if self.color == 'white':
            if self.has_moved == False:
                self.unfiltered_moves.append((self.x, self.y-120))
            self.unfiltered_moves.append((self.x+60, self.y-60))
            self.unfiltered_moves.append((self.x, self.y-60))
            self.unfiltered_moves.append((self.x-60, self.y-60))
        else:
            if self.has_moved == False:
                self.unfiltered_moves.append((self.x, self.y+120))
            self.unfiltered_moves.append((self.x+60, self.y+60))
            self.unfiltered_moves.append((self.x, self.y+60))
            self.unfiltered_moves.append((self.x-60, self.y+60))

    def draw(self, win):
        win.blit(self.image, self.rect)



class Bishop:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.type = 'bishop'
        if self.color == 'white':
            self.image = pygame.image.load('Pieces/Chess_blt60.png')
        else:
            self.image = pygame.image.load('Pieces/Chess_bdt60.png')
        self.rect = pygame.Rect(self.x, self.y, PIECE_SIZE, PIECE_SIZE)
        self.selected = False
        self.allowed_moves = []
        self.unfiltered_moves = []
        self.find_unfiltered_moves()  

    def find_unfiltered_moves(self):
        self.unfiltered_moves = []
        for i in range(1,8):
            if self.x + i*60 <= 420 and self.y + i*60 <= 420:
                self.unfiltered_moves.append((self.x+i*60, self.y+i*60))
            if self.x - i*60 >= 0 and self.y + i*60 <= 420:
                self.unfiltered_moves.append((self.x-i*60, self.y+i*60))
            if self.x + i*60 <= 420 and self.y - i*60 >= 0:
                self.unfiltered_moves.append((self.x+i*60, self.y-i*60))
            if self.x - i*60 >= 0 and self.y - i*60 >= 0:
                self.unfiltered_moves.append((self.x-i*60, self.y-i*60))        

    def draw(self, win):
        win.blit(self.image, self.rect)



class Knight:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.type = 'knight'
        if self.color == 'white':
            self.image = pygame.image.load('Pieces/Chess_nlt60.png')
        else:
            self.image = pygame.image.load('Pieces/Chess_ndt60.png')
        self.rect = pygame.Rect(self.x, self.y, PIECE_SIZE, PIECE_SIZE)
        self.selected = False
        self.allowed_moves = []
        self.unfiltered_moves = []
        self.find_unfiltered_moves()

    def find_unfiltered_moves(self):
        self.unfiltered_moves = []
        for i in range(4):
            if i == 0 and self.x - 120 >= 0 and self.x - 120 <= 420:
                if self.y - 60 >= 0 and self.y - 60 <= 420:
                    self.unfiltered_moves.append((self.x-120, self.y-60))
                if self.y + 60 >= 0 and self.y + 60 <= 420:
                    self.unfiltered_moves.append((self.x-120, self.y+60))
            elif i == 1 and self.x - 60 >= 0 and self.x - 60 <= 420:
                if self.y - 120 >= 0 and self.y - 120 <= 420:
                    self.unfiltered_moves.append((self.x-60, self.y-120))
                if self.y + 120 >= 0 and self.y + 120 <= 420:
                    self.unfiltered_moves.append((self.x-60, self.y+120))
            elif i == 2 and self.x + 60 >= 0 and self.x + 60 <= 420:
                if self.y - 120 >= 0 and self.y - 120 <= 420:
                    self.unfiltered_moves.append((self.x+60, self.y-120))
                if self.y + 120 >= 0 and self.y + 120 <= 420:
                    self.unfiltered_moves.append((self.x+60, self.y+120))
            elif i == 3 and self.x + 120 >= 0 and self.x + 120 <= 420:
                if self.y - 60 >= 0 and self.y - 60 <= 420:
                    self.unfiltered_moves.append((self.x+120, self.y-60))
                if self.y + 60 >= 0 and self.y + 60 <= 420:
                    self.unfiltered_moves.append((self.x+120, self.y+60))

    def draw(self, win):
        win.blit(self.image, self.rect)



class Rook:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.type = 'rook'
        if self.color == 'white':
            self.image = pygame.image.load('Pieces/Chess_rlt60.png')
        else:
            self.image = pygame.image.load('Pieces/Chess_rdt60.png')
        self.rect = pygame.Rect(self.x, self.y, PIECE_SIZE, PIECE_SIZE)
        self.selected = False
        self.has_moved = False
        self.allowed_moves = []
        self.unfiltered_moves = []
        self.find_unfiltered_moves()

    def find_unfiltered_moves(self):
        self.unfiltered_moves = []
        for i in range(1,8):
            if self.x + i*60 <= 420:
                self.unfiltered_moves.append((self.x+i*60, self.y))
            if self.x - i*60 >= 0:
                self.unfiltered_moves.append((self.x-i*60, self.y))
            if self.y + i*60 <= 420:
                self.unfiltered_moves.append((self.x, self.y+i*60))
            if self.y - i*60 >= 0:
                self.unfiltered_moves.append((self.x, self.y-i*60))


    def draw(self, win):
        win.blit(self.image, self.rect)



class Queen:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.type = 'queen'
        if self.color == 'white':
            self.image = pygame.image.load('Pieces/Chess_qlt60.png')
        else:
            self.image = pygame.image.load('Pieces/Chess_qdt60.png')
        self.rect = pygame.Rect(self.x, self.y, PIECE_SIZE, PIECE_SIZE)
        self.selected = False
        self.allowed_moves = []
        self.unfiltered_moves = []
        self.find_unfiltered_moves()

    def find_unfiltered_moves(self):
        self.unfiltered_moves = []
        for i in range(1,8):
            if self.x + i*60 <= 420 and self.y + i*60 <= 420:
                self.unfiltered_moves.append((self.x+i*60, self.y+i*60))
            if self.x - i*60 >= 0 and self.y + i*60 <= 420:
                self.unfiltered_moves.append((self.x-i*60, self.y+i*60))
            if self.x + i*60 <= 420 and self.y - i*60 >= 0:
                self.unfiltered_moves.append((self.x+i*60, self.y-i*60))
            if self.x - i*60 >= 0 and self.y - i*60 >= 0:
                self.unfiltered_moves.append((self.x-i*60, self.y-i*60))
            if self.x + i*60 <= 420:
                self.unfiltered_moves.append((self.x+i*60, self.y))
            if self.x - i*60 >= 0:
                self.unfiltered_moves.append((self.x-i*60, self.y))
            if self.y + i*60 <= 420:
                self.unfiltered_moves.append((self.x, self.y+i*60))
            if self.y - i*60 >= 0:
                self.unfiltered_moves.append((self.x, self.y-i*60))

    def draw(self, win):
        win.blit(self.image, self.rect)



class King:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.type = 'king'
        if self.color == 'white':
            self.image = pygame.image.load('Pieces/Chess_klt60.png')
        else:
            self.image = pygame.image.load('Pieces/Chess_kdt60.png')
        self.rect = pygame.Rect(self.x, self.y, PIECE_SIZE, PIECE_SIZE)
        self.selected = False
        self.has_moved = False
        self.allowed_moves = []
        self.unfiltered_moves = []
        self.find_unfiltered_moves()

    def find_unfiltered_moves(self):
        if self.x + 60 <= 420 and self.y + 60 <= 420:
            self.unfiltered_moves.append((self.x+60, self.y+60))
        if self.x - 60 >= 0 and self.y + 60 <= 420:
            self.unfiltered_moves.append((self.x-60, self.y+60))
        if self.x + 60 <= 420 and self.y - 60 >= 0:
            self.unfiltered_moves.append((self.x+60, self.y-60))
        if self.x - 60 >= 0 and self.y - 60 >= 0:
            self.unfiltered_moves.append((self.x-60, self.y-60))
        if self.x + 60 <= 420:
            self.unfiltered_moves.append((self.x+60, self.y))
        if self.x - 60 >= 0:
            self.unfiltered_moves.append((self.x-60, self.y))
        if self.y + 60 <= 420:
            self.unfiltered_moves.append((self.x, self.y+60))
        if self.y - 60 >= 0:
            self.unfiltered_moves.append((self.x, self.y-60))

    def draw(self, win):
        win.blit(self.image, self.rect)
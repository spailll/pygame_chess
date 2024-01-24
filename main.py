import pygame

WIDTH, HEIGHT = 480, 480
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")

WHITE = (255, 255, 255)
FPS = 60

BLACK_PAWN = pygame.image.load('Pieces/Chess_pdt60.png')
WHITE_PAWN = pygame.image.load('Pieces/Chess_plt60.png')
BLACK_BISHOP = pygame.image.load('Pieces/Chess_bdt60.png')
WHITE_BISHOP = pygame.image.load('Pieces/Chess_blt60.png')
BLACK_ROOK = pygame.image.load('Pieces/Chess_rdt60.png')
WHITE_ROOK = pygame.image.load('Pieces/Chess_rlt60.png')
BLACK_KNIGHT = pygame.image.load('Pieces/Chess_ndt60.png')
WHITE_KNIGHT = pygame.image.load('Pieces/Chess_nlt60.png')
BLACK_QUEEN = pygame.image.load('Pieces/Chess_qdt60.png')
WHITE_QUEEN = pygame.image.load('Pieces/Chess_qlt60.png')
BLACK_KING = pygame.image.load('Pieces/Chess_kdt60.png')
WHITE_KING = pygame.image.load('Pieces/Chess_klt60.png')

PIECE_SIZE = 60

SQUARE_SIZE = (60,60)
BLACK_SQUARE = pygame.Surface(SQUARE_SIZE)
BLACK_SQUARE.fill((211,211,211))

def draw_window(pieces,):
    WIN.fill(WHITE)

    for i in range(8):
        for j in range(8):
            if (i+j) % 2 == 0:
                WIN.blit(BLACK_SQUARE, (i*60,j*60))

    i = 0
    for piece in pieces:
        if i < 8:
            image = WHITE_PAWN
        elif i < 16:
            image = BLACK_PAWN
        elif i < 18:
            image = WHITE_ROOK
        elif i < 20:
            image = BLACK_ROOK
        elif i < 22:
            image = WHITE_KNIGHT
        elif i < 24:
            image = BLACK_KNIGHT
        elif i < 26:
            image = WHITE_BISHOP
        elif i < 28:
            image = BLACK_BISHOP
        elif i < 29:
            image = WHITE_QUEEN
        elif i < 30:
            image = BLACK_QUEEN
        elif i < 31:
            image = WHITE_KING
        else:
            image = BLACK_KING
        WIN.blit(image, piece)
        i += 1
    pygame.display.update()

def main():
    pawnW1 = pygame.Rect(0,360, PIECE_SIZE, PIECE_SIZE) 
    pawnB1 = pygame.Rect(0,60, PIECE_SIZE, PIECE_SIZE)
    pawnW2 = pygame.Rect(60,360, PIECE_SIZE, PIECE_SIZE) 
    pawnB2 = pygame.Rect(60,60, PIECE_SIZE, PIECE_SIZE)
    pawnW3 = pygame.Rect(120,360, PIECE_SIZE, PIECE_SIZE) 
    pawnB3 = pygame.Rect(120,60, PIECE_SIZE, PIECE_SIZE)
    pawnW4 = pygame.Rect(180,360, PIECE_SIZE, PIECE_SIZE) 
    pawnB4 = pygame.Rect(180,60, PIECE_SIZE, PIECE_SIZE)
    pawnW5 = pygame.Rect(240,360, PIECE_SIZE, PIECE_SIZE) 
    pawnB5 = pygame.Rect(240,60, PIECE_SIZE, PIECE_SIZE)
    pawnW6 = pygame.Rect(300,360, PIECE_SIZE, PIECE_SIZE) 
    pawnB6 = pygame.Rect(300,60, PIECE_SIZE, PIECE_SIZE)
    pawnW7 = pygame.Rect(360,360, PIECE_SIZE, PIECE_SIZE) 
    pawnB7 = pygame.Rect(360,60, PIECE_SIZE, PIECE_SIZE)
    pawnW8 = pygame.Rect(420,360, PIECE_SIZE, PIECE_SIZE) 
    pawnB8 = pygame.Rect(420,60, PIECE_SIZE, PIECE_SIZE)
    rookW1 = pygame.Rect(0,420, PIECE_SIZE, PIECE_SIZE)
    rookB1 = pygame.Rect(0,0, PIECE_SIZE, PIECE_SIZE)
    rookW2 = pygame.Rect(420,420, PIECE_SIZE, PIECE_SIZE)
    rookB2 = pygame.Rect(420,0, PIECE_SIZE, PIECE_SIZE)
    knightW1 = pygame.Rect(60,420, PIECE_SIZE, PIECE_SIZE)
    knightB1 = pygame.Rect(60,0, PIECE_SIZE, PIECE_SIZE)
    knightW2 = pygame.Rect(360,420, PIECE_SIZE, PIECE_SIZE)
    knightB2 = pygame.Rect(360,0, PIECE_SIZE, PIECE_SIZE)
    bishopW1 = pygame.Rect(120,420, PIECE_SIZE, PIECE_SIZE)
    bishopB1 = pygame.Rect(120,0, PIECE_SIZE, PIECE_SIZE)
    bishopW2 = pygame.Rect(300,420, PIECE_SIZE, PIECE_SIZE)
    bishopB2 = pygame.Rect(300,0, PIECE_SIZE, PIECE_SIZE)
    queenW = pygame.Rect(180,420, PIECE_SIZE, PIECE_SIZE)
    queenB = pygame.Rect(180,0, PIECE_SIZE, PIECE_SIZE)
    kingW = pygame.Rect(240,420, PIECE_SIZE, PIECE_SIZE)
    kingB = pygame.Rect(240,0, PIECE_SIZE, PIECE_SIZE)


    pieces = [pawnW1, pawnW2, pawnW3, pawnW4, pawnW5, pawnW6, pawnW7, pawnW8, pawnB1, pawnB2, pawnB3, pawnB4, pawnB5, pawnB6, pawnB7, pawnB8, rookW1, rookW2, rookB1, rookB2, knightW1, knightW2, knightB1, knightB2, bishopW1, bishopW2, bishopB1, bishopB2, queenW, queenB, kingW, kingB]

    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window(pieces)

    pygame.quit()

if __name__ == "__main__":
    main()
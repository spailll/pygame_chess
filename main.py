import pygame

from pieces import Pawn, Bishop, Knight, Rook, Queen, King, Board

WIDTH, HEIGHT = 480, 480
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")

WHITE = (255, 255, 255)
FPS = 10

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
BLACK_SQUARE.fill((211,211,211))    # Light Grey

def draw_window(board):
    WIN.fill(WHITE)

    for i in range(8):
        for j in range(8):
            if (i+j) % 2 == 1:
                WIN.blit(BLACK_SQUARE, (i*60,j*60))

    i = 0
    for piece in board.white_pieces:
        piece.draw(WIN)
    for piece in board.black_pieces:
        piece.draw(WIN)
    pygame.display.update()

def handle_click(pos, board):
    x, y = pos
    x = x // 60 * 60
    y = y // 60 * 60
    piece_is_selected = False
    for piece in board.white_pieces:
        if piece.selected:
            piece_is_selected = True
            selected_piece = piece
    for piece in board.black_pieces:
        if piece.selected:
            piece_is_selected = True
            selected_piece = piece
    if piece_is_selected:
        if board.move(selected_piece,x, y):
            return
        else:
            selected_piece.selected = False
    for piece in board.white_pieces:
        if piece.x == x and piece.y == y:
            piece.selected = True
    for piece in board.black_pieces:
        if piece.x == x and piece.y == y:
            piece.selected = True

def main():
    board = Board()
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                handle_click(mouse_pos, board)                
               
        draw_window(board)

    pygame.quit()

if __name__ == "__main__":
    main()
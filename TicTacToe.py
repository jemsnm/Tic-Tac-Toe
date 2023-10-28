import sys
import pygame

game = True
background_colour = (15, 14, 14)
line_colour = (38, 38, 38)
screen_width = 600
screen_height = 600
cell_size = screen_width / 3
o_colour = (125,18,255)
x_colour = (242, 58, 193)
white_colour = (252, 247, 251)
game_board = []
player_char = 'X'

pygame.init()
font_char = pygame.font.Font(None, 255)
font_msg = pygame.font.Font(None, 43)

screen = pygame.display.set_mode((screen_width, screen_height), 0, 34)
screen.fill(background_colour)
pygame.display.set_caption('Tic-Tac-Toe')

def set_board():
    global game
    global game_board
    game = True
    game_board = [[0]*3, [0]*3, [0]*3]
    screen.fill(background_colour)

def set_game():
    set_board()

    # vertical lines
    pygame.draw.line(screen, line_colour,
                    (screen_width / 3, 0),
                    (screen_width / 3, screen_height), 7)
    pygame.draw.line(screen, line_colour,
                    (screen_width / 3 * 2, 0),
                    (screen_width / 3 * 2, screen_height), 7)

    # horizontal lines
    pygame.draw.line(screen, line_colour,
                    (0, screen_height / 3),
                    (screen_width, screen_height / 3), 7)
    pygame.draw.line(screen, line_colour,
                    (0, screen_height / 3 * 2),
                    (screen_width, screen_height / 3 * 2), 7)

def move():
    x, y = pygame.mouse.get_pos()
    row = int(y // cell_size)
    column = int(x // cell_size)
    if game_board[row][column] == 0:
        game_board[row][column] = player_char
        draw_xo(row, column)
    else:
        return False

def messages(player, draw = False):
    global game
    msg = ""
    if draw:
        msg += "It's a draw!"
        game = False
    else:
        msg += f"{player} won!"
        game = False 

    screen.blit(font_msg.render('Press R to play again', 1, white_colour, line_colour), (150, 230))
    screen.blit(font_msg.render(msg, 1, white_colour, line_colour), (240, 270))

def draw_xo(row, column):
    global player_char
    position_x = ((screen_width / 3) * column) + (cell_size / 5.5)
    position_y = ((screen_height / 3) * row) + (cell_size / 7.5)

    if player_char == 'X':
        screen.blit(font_char.render('X', 1, x_colour), (position_x, position_y))
        winner()
        player_char = 'O'
    else:
        screen.blit(font_char.render('O', 1, o_colour), (position_x, position_y))
        winner()
        player_char = 'X'

def winner():
    global game_board
    for i in range(3):
        # row wins
        if game_board[i][0] == game_board[i][1] == game_board[i][2] != 0:
            pygame.draw.line(screen, white_colour,
                        (0, (i + 1) * screen_height / 3 - screen_height / 6),
                        (screen_width, (i + 1) * screen_height / 3 - screen_height / 6),
                        3)
            messages(player_char)
        # column wins
        elif game_board[0][i] == game_board[1][i] == game_board[2][i] != 0:
            pygame.draw.line(screen, white_colour,
                        ((i + 1) * screen_width / 3 - screen_width / 5.5, 0),
                        ((i + 1) * screen_width / 3 - screen_width / 5.5, screen_height),
                        3)
            messages(player_char)

    # diagonal wins
    if game_board[0][0] == game_board[1][1] == game_board[2][2] != 0: 
        pygame.draw.line(screen, white_colour, (50, 50), (550,550), 3)
        messages(player_char)
    elif game_board[0][2] == game_board[1][1] == game_board[2][0] != 0:
        pygame.draw.line(screen, white_colour, (550, 50), (50,550), 3)
        messages(player_char)
    
    #  draw
    if not any(0 in board for board in game_board):
        messages(player_char, True)

def start():
    global game
    set_game()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and game:
                move()
            elif event.type == pygame.KEYDOWN and not game:
                if event.key == pygame.K_r:
                    set_game()

        pygame.display.update()

start()
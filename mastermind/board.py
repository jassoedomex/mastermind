def create_new_board():
    board = [[" " for _ in range(3)] for _ in range(10)]
    verification = [[" " for _ in range(3)] for _ in range(10)]
    return board, verification

def number_of_lines(quantity, color):
    pass
def number_of_holes(quantity, color):
    pass
def number_of_tries(color):
    pass
def code (win, lose):
    pass
def you_won (screen):
    pass
def you_lose(screen):
    pass
def print_board(board, verification):
    print(
        f"""
{board[0][0]} | {board[0][1]} | {board[0][2]} | {verification[0][0]}{verification[0][1]}{verification[0][2]}
{board[1][0]} | {board[1][1]} | {board[1][2]} | {verification[1][0]}{verification[1][1]}{verification[1][2]}
{board[2][0]} | {board[2][1]} | {board[2][2]} | {verification[2][0]}{verification[2][1]}{verification[2][2]}
{board[3][0]} | {board[3][1]} | {board[3][2]} | {verification[3][0]}{verification[3][1]}{verification[3][2]}
{board[4][0]} | {board[4][1]} | {board[4][2]} | {verification[4][0]}{verification[4][1]}{verification[4][2]}
{board[5][0]} | {board[5][1]} | {board[5][2]} | {verification[5][0]}{verification[5][1]}{verification[5][2]}
{board[6][0]} | {board[6][1]} | {board[6][2]} | {verification[6][0]}{verification[6][1]}{verification[6][2]}
{board[7][0]} | {board[7][1]} | {board[7][2]} | {verification[7][0]}{verification[7][1]}{verification[7][2]}
{board[8][0]} | {board[8][1]} | {board[8][2]} | {verification[8][0]}{verification[8][1]}{verification[8][2]}
{board[9][0]} | {board[9][1]} | {board[9][2]} | {verification[9][0]}{verification[9][1]}{verification[9][2]}
"""
    )

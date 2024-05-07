def change_pins(color,location, board):
    print("color changed")
    board[location[0]][location[1]]= color


def move (board):
    for i in range(0,10):
        board[i]
    print("Next road")

def correct(code, current_row, board):
    row = board[current_row]
    verification_code = []
    for code_color, board_color in zip(code, row):
        if code_color == board_color:
            verification_code.append("c")
        else:
            verification_code.append("i")
    return verification_code

def check_winner(verification_code):
    return verification_code == "ccc"

def check_loser(current_row):
    return current_row == 9
#Took from chat GPT
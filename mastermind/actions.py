def change_pins(color,location, board):
    print("color changed")
    board[location[0]][location[1]]= color

def select(color,location, board):
    print("set color")

def move (board):
    print("Next road")

def correct(code, board):
    verication_code = code
    for code_color, board_color in zip(code, row):
        if code_color == board_color:
            colors = True
            pint("you can mov eto the next row")
        else:
            colors = False
            print ("you need to try something new")
    return verication_code

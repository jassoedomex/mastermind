from mastermind.board import create_new_board
from mastermind.actions import change_pins, select, move, correct


def test_change_pins():
    board, verification = create_new_board()
    board[0][0] = "B"
    change_pins("G", [0, 0], board)

    new_board, verification = create_new_board()
    new_board[0][0] = "G"

    assert board == new_board


def test_select():
    print("set color")
    board, verification = create_new_board()
    select("B",[1,0], board )
    assert board[1][0] == "B"


def test_move():
    print("Next road")
    board, verification = create_new_board()
    current_row = move(board)
    assert current_row == 0




def test_correct():
    print("Result")
    board, verification = create_new_board()
    answer = correct("BYW", board)
    assert "III" == answer

from board import create_new_board, number_of_lines, number_of_holes, number_of_tries, code, you_won, you_lose, print_board
from actions import change_pins, select, move, correct
from random import choices

def check_win(verification_code):
    return all(pin == "c" for pin in verification_code)

def check_loss(current_row):
    return current_row == 9

name = input("tell me your name")
print("Nice to meet you", name)
with open('README.md', 'r') as f:
  print(f.read())
board, verification = create_new_board()
colors = ["r", "b", "g"]
code = choices(colors,k=3)
current_row = 0
while True:
    print_board(board, verification)
    command = input ("Enter a command:")
    if command == "q":
      exit()
    elif command == "change color":
       color = input("Select a color of pin")
       location = input("Select the location of the pin")
       location = int(location)
       change_pins(color,[current_row, location],board)
    elif command == "next":
       verification_code = correct(code, current_row, board)
       print(verification_code)
       if check_win(verification_code):
            you_won(board)
            break
       elif check_loss(current_row):
            you_lose(board)
            break
       current_row += 1
else:
 print("I did not understand this command.")     
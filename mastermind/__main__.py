from board import create_new_board, number_of_holes, number_of_lines, number_of_tries, print_board, you_won, you_lose
from actions import change_pins, move, correct, check_loser, check_winner
from random import choices

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
       if check_winner(verification_code):
            you_won(board)
            break
       elif check_loser(current_row):
            you_lose(board)
            break
       current_row += 1
    else:
        print("I did not understand this command.")
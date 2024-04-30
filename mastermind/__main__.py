from board import create_new_board, number_of_lines, number_of_holes, number_of_tries, code, you_won, you_lose, print_board
from actions import change_pins, select, move, correct
from random import choices

name = input("tell me your name")
print("Nice to meet you", name)
with open('README.md', 'r') as f:
  print(f.read())
board, verification = create_new_board()
colors = [r, b, g]
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
       
       current_row = move(None,None,board)
    elif command == "result":
       select(None,None,board)
    else :
      print("I did not understand this command.")        



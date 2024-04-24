from board import create_new_board, number_of_lines, number_of_holes, number_of_tries, code, you_won, you_lose, print_board
from actions import change_pins, select, move, correct

name = input("tell me your name")
print("Nice to meet you", name)
with open('README.md', 'r') as f:
  print(f.read())
board, verification = create_new_board()
while True:
    print_board(board, verification)
    command = input ("Enter a command:")
    if command == "q":
      exit()
    elif command == "change color":
       change_pins(None,None,None)
    elif command == "color":
       select(None,None,None)
    elif command == "next":
       move(None,None,None)
    elif command == "result":
       select(None,None,None)
    else :
      print("I did not understand this command.")        



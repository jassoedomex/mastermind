from board import create_new_board, number_of_lines
from board import number_of_holes
from board import number_of_tries
from board import code
from board import you_won
from board import you_lose
from actions import change_pins
from actions import select
from actions import move
from actions import correct
from board import print_board

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



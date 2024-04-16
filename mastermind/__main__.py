from board import create_new_board
from board import number_of_lines
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
  while True:
    command = input ("Enter a command:")
    if command == "start":
      create_new_board()
    elif command == "q":
      exit()
    else :
      print("I did not understand this command.")        

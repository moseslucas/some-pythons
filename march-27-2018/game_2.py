import math
import os

def clear_screen():
  os.system("cls")
  os.system("clear")

def guess(game):
  g = game
  middle = g["roof"]/2
  guess = middle
  while g["guessed"] == False:
    print "Is your number", guess, "?"
    answer = raw_input("Type h for Higher, l for Lower, y for Correct number: ").lower()
    if (answer == "y"):
      print("---------------------------")
      print "Guessed your number: ", guess
      print "With a total rounds of :", len(g["rounds"])
      print("---------------------------")
      break
    elif (answer == "h"):
      clear_screen()
      g["ground"] = guess + 1
      guess = (g["roof"] + g["ground"])/2
      g["rounds"].append({"guess": guess, "correctness": "too low"})
      continue
    elif (answer == "l"):
      clear_screen()
      g["roof"] = guess
      guess = (g["roof"] + g["ground"])/2
      g["rounds"].append({"guess": guess, "correctness": "too high"})
      continue
    else:
      clear_screen()
      print "Invalid Input"
      continue

def start():
  clear_screen()
  print("******* Guessing Game *****")
  Game = {
    "rounds": [],
    "ground": 1,
    "roof": 100,
    "guessed": False
  }
  Game = guess(Game)

#
start()

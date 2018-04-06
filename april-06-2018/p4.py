
def start():
  pokemons = [
    "Charmeleon",
    "Geodude",
    "Gyarados",
    "Butterfree",
    "Mankey"
  ]
  my_pokemon = "Pikachu"
  print "Exchange", my_pokemon
  user_input = None
  while(user_input is not 0):
    print "*", my_pokemon
    print "  ".join(pokemons)
    user_input = input("Choose pokemon name (or 0 to exit) : ")
    if (user_input is 0):
      break
    elif (user_input < 0 or user_input > len(pokemons)):
      print "Pokemon order does not exist"
    else:
      swap = pokemons[user_input-1]
      pokemons[user_input-1] = my_pokemon
      my_pokemon = swap
# start
start()

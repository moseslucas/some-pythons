def is_automorphic(user_input):
  square = user_input * user_input
  return (user_input == int(str(square)[-1]))
def start():
  user_input = input("Input a number: ")
  if (is_automorphic(user_input)):
    print "Automorphic"
  else:
    print "Not Automorphic"
# start
start()

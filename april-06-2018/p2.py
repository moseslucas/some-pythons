def countTriplets(user_input):
  w = user_input
  triplets = 0
  for i in range(len(w)-2):
    if (w[i] == w[i+1] and w[i] == w[i+2]):
      triplets += 1
  return triplets

def start():
  user_input = raw_input("Input a string: ")
  print "Output: ", countTriplets(user_input)

# start
start()

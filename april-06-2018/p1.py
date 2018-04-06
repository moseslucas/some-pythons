def process(user_input):
  processedWord = ""
  for i in range (0, len(user_input)):
    processedWord+= user_input[0:i+1].capitalize()
  return processedWord

def start():
  user_input = raw_input("Input String: ")
  print(process(user_input))


# start
start()

def omitApostrophe(word):
  deduct = 0
  if (word[0] == '"'):
    deduct+=1
  if (word[-1] == '"'):
    deduct+=1
  return deduct

def countIt(words):
  words = words.split(" ")
  words_count = []
  for word in words:
    words_count.append(len(word) - omitApostrophe(word))
  return words_count
  
def start():
  words = raw_input("Input: ")
  print(countIt(words))
# 
start()

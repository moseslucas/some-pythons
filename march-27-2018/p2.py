def countIt(words):
  words = words.split(" ")
  words_count = []
  for word in words:
      words_count.append(len(word))
  return words_count
  
def start():
  words = raw_input("Input: ")
  print(countIt(words))
# 
start()

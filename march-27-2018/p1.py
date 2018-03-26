def reverseIt(n):
  n = n.split(" ")
  n.reverse()
  n = " ".join(n)
  return n
  
def start():
  N = raw_input("Input: ")
  print(reverseIt(N))
# 
start()

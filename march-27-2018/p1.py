def reverseIt(num):
  num = num.split(" ")
  num.reverse()
  num = " ".join(num)
  return num
  
def start():
  N = raw_input("Input: ")
  print(reverseIt(N))
# 
start()

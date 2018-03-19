def isValid(num):
  return (num > 1 and (num%5 == 0))

def start():
  while True:
    N = input("N: ")
    if (isValid(N)):
      print(N/5)
    else:
      print(-1)

# 
start()

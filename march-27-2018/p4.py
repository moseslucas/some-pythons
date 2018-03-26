import datetime

def compute(y,m,d):
  return datetime.date(y,m,d).strftime("%A")
  
def start():
  D = input("Day: ")
  M = input("Month: ")
  Y = input("Year: ")
  print(compute(Y,M,D))
# 
start()

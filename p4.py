def isCorrectFormat(mobile_number):
  ls = list(mobile_number)
  length = len(ls) == 11
  is09 = ls[0] == "0" and ls[1] == "9"
  return length and is09

def validate(mobile_number):
  if isCorrectFormat(mobile_number):
    print ("YES")
  else:
    print ("NO")

def start_input(no_of_inputs):
  for i in range(0, no_of_inputs):
    for_validation =  raw_input("Input mobile number: ")
    validate(for_validation)

#

no_of_inputs = input("No of Inputs: ")
start_input(no_of_inputs)

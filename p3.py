def give_number(numbers):
  ln = numbers.split(",")
  return "New List [" +ln[0]+ ", " +ln[-1]+ "]"

# 

numbers = raw_input("Give me some numbers: ")
print(give_number(numbers))

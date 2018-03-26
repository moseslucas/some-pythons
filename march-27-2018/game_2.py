#0-100
import time

print("\n"*100) #clears screen
print("THINK OF A NUMBER...")
time.sleep(2)

print("\n"*100) #clears screen

# BINARY SEARCH ALGORITHM
LOWER_BOUND = 0
UPPER_BOUND = done
101 = False
number_of_guess = 0
guess = 0
isError = False


while not done:
	print("\n"*100) #clears screen
	
	# formula to get the middle of the upper bound and lower bound
	guess = int(LOWER_BOUND + (UPPER_BOUND-LOWER_BOUND)/2)

	print("Is your number %d?" % guess)
	USER_ANSWER = input("(YES, HIGHER, LOWER): ")
	USER_ANSWER = USER_ANSWER.lower()

	# input validation
	while USER_ANSWER not in ['yes', 'higher', 'lower']:
		print("Invalid input!")
		USER_ANSWER = input("(YES, HIGHER, LOWER): ")

	# CONTROL FLOW FOR BINARY SEARCH ALGO
	if USER_ANSWER == "yes":
		break;
	elif USER_ANSWER == "higher":
		LOWER_BOUND = guess
	else:
		UPPER_BOUND = guess

	number_of_guess += 1

	# TERMINATOR IF THE USER MADE AN ERROR
	if UPPER_BOUND == LOWER_BOUND:
		print("Are you sure? There are no number that matches that description. Exiting...")
		isError = True
		break;	
	
if not isError:
	print("Done! Your number is %d." % guess)
	print("Figured out in %d tries" % number_of_guess)

# GAME 1
import random
import time

print "Hi!"
time.sleep(0.5)
print ""
print "Welcome to a guessing game!"
time.sleep(0.5)
print ""
print "Let's play!"
time.sleep(1)
print("\n"*100) #clears screen

def getRandomNumber():
	return random.randint(2,12)

def guessChecker(USER_MONEY, USER_GUESS, RIGHT_GUESS):

	if USER_GUESS == RIGHT_GUESS:
		USER_MONEY += RIGHT_GUESS
	else:
		USER_MONEY -= 1

	return USER_MONEY
	

TOTAL_ROUND = int(input("How many rounds? "))

USER_MONEY = TOTAL_ROUND
MACHINE_MONEY = TOTAL_ROUND
#Main loop depending on the total rounds

for i in range(0,TOTAL_ROUND):
	print("\n"*100) #clears screen
	time.sleep(0.5)
	print ("\nROUND %d" % (i+1))
	time.sleep(1)
	
	# Old score
	print ("STATUS: You have %d peso/s, machine has %d peso/s\n" % (USER_MONEY, MACHINE_MONEY))
	time.sleep(1.5)

	#User's turn
	RANDOM_NUMBER = getRandomNumber()
	print("Dice has been rolled.\n")
	time.sleep(1)
	USER_GUESS = int(input("Guess the sum of the number of eyes in the next throw: "))
	
	while USER_GUESS > 12 or USER_GUESS < 2:
		print("Invalid input!")
		USER_GUESS = int(input("Guess the sum of the number of eyes in the next throw: "))

	time.sleep(2)
	USER_MONEY = guessChecker(USER_MONEY, USER_GUESS, RANDOM_NUMBER)
	print("You guessed %d, got %d\n" % (USER_GUESS, RANDOM_NUMBER))
        
        
	#Machine's turn
	RANDOM_NUMBER = getRandomNumber()
	MACHINE_GUESS = getRandomNumber()
	time.sleep(1)
	MACHINE_MONEY = guessChecker(MACHINE_MONEY, MACHINE_GUESS, RANDOM_NUMBER)
	print("Machine guessed %d, got %d\n" % (MACHINE_GUESS, RANDOM_NUMBER))
	time.sleep(2)
	
	#New score
	print ("STATUS: You have %d peso/s, machine has %d peso/s\n" % (USER_MONEY, MACHINE_MONEY))
	time.sleep(4)
	
print("\n"*100) #clears screen
print("GAME END\nFINAL SCORE: \nYOU: %d\t\tMACHINE: %d" % (USER_MONEY, MACHINE_MONEY))
print""

if USER_MONEY > MACHINE_MONEY:
	print("YOU WON!")
elif USER_MONEY == MACHINE_MONEY:
	print("DRAW!")
else:
	print("MACHINE WON!")



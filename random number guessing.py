import random
numofguesses = 0

name = input("Hello, What is your name? ")

number = random.randint(1, 20)
print("Number I'am thinking of is between 1 and 20 ,name")

while numofguesses < 6:
	print("Take a guess... ")
	guess = input()
	guess = int(guess)

	numofguesses = numofguesses + 1
	if guess < number:
		print("Number is to Low")
	if guess > number:
		print("Number is too High")
	if guess == number:
		break

	if guess == number:
		numofguesses = str(numofguesses)
	print("Well Done!!! " ,name,"You guessed the number is" ,numofguesses)

	if guess != number:
		number = str(number)
		print("Wrong! Unlucky, The Numbe Was: ,number")

import random

number = random.randint(1,100)
tries = 0


print ("I'm thinking of a number between 1 and 100")

while True:
	guess = int(input("what's your guess?:"))
	tries = tries + 1

	if tries >= 7:
		print ("no, man, just no,",tries,"tries? really? it's over, you lose")
		break

	if guess < number:
		print ("too low")
	elif guess > number:
		print ("too high")
	else:
		print ("that was it!",guess,"was correct, it only took you",tries,"tries!")
		break


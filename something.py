import random 
numer = int (input("whats the maximum?"))
ran=random.randint(1, numer)
while True:
	guess=int(input("guess"))
	if guess== ran:
		print("yay!you won!")
	elif guess < ran:
		print("hey its too low")

	elif guess > ran:
		print("hey its too high")
	else:
		print ("try again")
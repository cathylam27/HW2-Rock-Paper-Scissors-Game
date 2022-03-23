from random import randint

choices = ["rock", "paper", "scissors"]

player_lives = 3
computer_lives = 3
total_lives = 3

player_choice = False

def winorlose(status):
	print("You", status, " Hey~ Would you like to kill the Monster again?")
	choice = input("Y / N? ")

	if choice == "N" or choice =="n":
		print("You chose to quit! See you next time!｡^‿^｡")
		exit()
	elif choice == "Y" or choice == "y":
		global player_lives
		global computer_lives
		global total_lives

		player_lives = total_lives
		computer_lives = total_lives
	else:
		print("Please choose - Y or N")
		choice = input("Y / N? ")

while player_choice is False:
	print("!!==================!!!!! (Σ( ° △ °|||)You meet a Monster !!!!!==================!!")
	print("(-`д´-)You are a Monster Hunter!! Please kill the Monster!!")
	print("The Monster HP:", computer_lives, "/", total_lives)
	print("Monster Hunter HP:", player_lives, "/", total_lives)
	print("=======================================================================")

	print("Choose your weapon to kill the Monster!!! Or type quit to exit\n")

	player_choice = input("Choose rock, paper, or scissors: \n")

	if player_choice == "quit":
		print("You chose to quit")
		exit()

	print("The Monster Hunter chose: " + player_choice)

	computer_choice = choices [randint(0, 2)]

	print("The Monster chose: " + computer_choice)

	if computer_choice == player_choice:
		print("Draw!!====><====")

	elif computer_choice == "rock":
		if player_choice == "scissors":
			print("BOOM!!!!!!!=====>OMG! You lose!(>_<)")
			player_lives -= 1
		else:
			print("COOOOOOOOOOOOL(*≧▽≦)WOW!!! You win!")
			computer_lives -= 1

	elif computer_choice == "paper":
		if player_choice == "scissors":
			print("COOOOOOOOOOOOL(*≧▽≦)WOW!!! You win!")
			computer_lives -= 1
		else:
			print("BOOM!!!!!!!=====>OMG! You lose!(>_<)")
			player_lives -= 1

	elif computer_choice == "scissors":
		if player_choice == "paper":
			print("BOOM!!!!!!!=====>OMG! You lose!(>_<)")
			player_lives -= 1
		else:
			print("COOOOOOOOOOOOL(*≧▽≦)WOW!!! You win!")
			computer_lives -= 1

	if player_lives == 0:
		winorlose("are dead by the monster(×_×;）")

	if computer_lives == 0:
		winorlose("killed the Monster!!! You save the world!!!٩(●˙▿˙●)۶…⋆ฺ")
		
	print("Monster Hunter HP:", player_lives)
	print("The Monster HP:", computer_lives)

	player_choice = False


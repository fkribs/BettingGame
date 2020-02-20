def play_with_bets(starting_balance=1000):
	def play():
		value = random.randint(0,9)
		attempts = 0
		while True:
			attempts += 1
			try:
				guess = int(input("Guess: "))
			except:
				print("Invalid guess, must be number")
				attempts -= 1
				continue
			if guess < 0 or guess > 9:
				print("Guess must be between 0 and 9")
				attempts -= 1
				continue
			if guess > value:
				message = "Too high"
			elif guess < value:
				message = "Too low"
			else:
				message = "You got it!"
			print(message)
			if guess == value or attempts == 3:
				print("It was {}".format(value))
				return guess == value
	balance = starting_balance
	high = balance
	bets = []
	bets_as_percent_of_balance = []
	rounds = 0
	wins = 0
	while True:
		print("Balance: ${}".format(balance))
		bet = input("Bet: ")
		if bet == '':
			print("Started with ${}".format(starting_balance))
			print("Finished with ${}".format(balance))
			knew_to_quit = "(You really knew when to quit!)" if balance == high else ""
			print("Highest balance: ${} {}".format(high, knew_to_quit))
			print("Win rate: {}%".format(wins / rounds * 100))
			print("Average bet: ${}".format(sum(bets) / len(bets)))
			print("Average bet as percentage of balance: {}%".format(sum(bets_as_percent_of_balance) / len(bets_as_percent_of_balance) * 100))
			return
		try:
			bet = int(bet)
		except:
			print("Invalid bet")
			continue
		if bet > balance:
			print("You cannot bet more than your balance of ${}".format(balance))
			continue
		rounds += 1
		bets.append(bet)
		bets_as_percent_of_balance.append(bet / balance)
		if play():
			balance += bet
			wins += 1
		else:
			balance -= bet
		if balance > high:
			high = balance

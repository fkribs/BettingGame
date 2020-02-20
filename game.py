def play_with_bets(starting_balance=1000):
	import math
	import random
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
				return (guess == value, attempts)
	balance = starting_balance
	high = balance
	bets = []
	bets_as_percent_of_balance = []
	rounds = 0
	wins = 0
	all_ins = 0
	while True:
		print("Balance: ${}".format(balance))
		bet = ''
		if balance != 0:
			bet = input("Bet (or leave empty to end game): ")

		if bet == '':
			print("\n-----GAME OVER-----")
			if rounds == 0:
				return
			print("Started with ${}".format(starting_balance))
			print("Finished with ${}".format(balance))
			knew_to_quit = "(You really knew when to quit!)" if balance == high else ""
			print("Highest balance: ${} {}".format(high, knew_to_quit))
			print("Win rate: {0:.2f}%".format(wins / rounds * 100))
			print("Average bet: ${0:.2f}".format(sum(bets) / len(bets)))
			print("Average bet as percentage of balance: {0:.2f}%".format(sum(bets_as_percent_of_balance) / len(bets_as_percent_of_balance) * 100))
			dare_devil = ". What a dare devil!" if all_ins == rounds else "."
			dare_devil = dare_devil + " (Didn't work out though, did it?)" if balance < starting_balance and all_ins == rounds else dare_devil
			dare_devil = " COWARD!" if all_ins == 0 else "."
			print("You went 'all-in' {1:.2f}% of the time ({0} {3}){2}".format(all_ins, all_ins / rounds * 100, dare_devil, "time" if all_ins == 1 else "times"))
			return
		try:
			bet = int(bet)
		except:
			print("Invalid bet")
			continue
		if bet > balance:
			print("You cannot bet more than your balance of ${}".format(balance))
			continue
		if bet < 0:
			print("You cannot bet a negative amount!")
			continue
		if bet == balance:
			all_ins += 1
		rounds += 1
		bets.append(bet)
		bets_as_percent_of_balance.append(bet / balance)
		round_results = play()
		if round_results[0]:
			attempts = round_results[1]
			bonus = 0
			if attempts == 2:
				bonus = math.ceil(bet * .1)
			if attempts == 1:
				bonus = math.ceil(bet * .5)
			if bonus != 0:
				print("LEFTOVER BONUS +{}!!! (You guessed correctly in {} {}!)".format(bonus, attempts, "try" if attempts == 1 else "tries"))
			balance += (bet + bonus)
			wins += 1
		else:
			balance -= bet
		if balance > high:
			high = balance

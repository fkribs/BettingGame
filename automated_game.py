import math
import random
class BetterBot():
	last_guess = -1
	last_result = 0
	def __init__(self, wait_between):
		self.wait_between = wait_between
	def Get_Guess(self):
		if self.last_guess == -1:
			self.last_guess = 5
		elif self.last_result == 1:
			if self.last_guess == 5:
				self.last_guess = 8
			elif self.last_guess == 8:
				self.last_guess = 9
			elif self.last_guess == 3:
				self.last_guess = 4
			else:
				self.last_guess = -1
		elif self.last_result == -1:
			if self.last_guess == 5:
				self.last_guess = 3
			elif self.last_guess == 8:
				self.last_guess = 7
			elif self.last_guess == 3:
				self.last_guess = 2
			else:
				self.last_guess = -1
		elif self.last_result == 0:
			self.last_guess = -1
		print(last_guess)
		return self.last_guess

	def Send_Guess_Result(self, message):
		if message == "Too high":
			last_result = 1
		elif message == "Too low":
			last_result = -1
		else:
			last_result = 0
	def Get_Bet(self, balance):
		if self.wait_between:
			wait= input(": ")
		bet = math.ceil(balance * .3)
		print("{:0,}".format(bet))
		return bet

	
def play_with_bets_bot(starting_balance=1000):
	bot = BetterBot(True)
	def play_bot():
		value = random.randint(0,9)
		attempts = 0
		while True:
			attempts += 1
			try:
				print("Guess: ")
				guess = bot.Get_Guess()
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
			bot.Send_Guess_Result(message)
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
		print("Balance: ${:0,.2f}".format(balance))
		bet = ''
		if balance != 0:
			print("Bet (or leave empty to end game): ")
			bet = bot.Get_Bet(balance)
		if bet == '':
			print("\n-----GAME OVER-----")
			if rounds == 0:
				return
			print("Started with ${:0,.2f}".format(starting_balance))
			print("Finished with ${:0,.2f}".format(balance))
			knew_to_quit = "(You really knew when to quit!)" if balance == high else ""
			print("Highest balance: ${:0,.2f} {}".format(high, knew_to_quit))
			print("Win rate: {0:.2f}%".format(wins / rounds * 100))
			print("Average bet: ${:0,.2f}".format(sum(bets) / len(bets)))
			print("Average bet as percentage of balance: {0:.2f}%".format(sum(bets_as_percent_of_balance) / len(bets_as_percent_of_balance) * 100))
			dare_devil = ". What a dare devil!" if all_ins == rounds else "."
			dare_devil = dare_devil + " (Didn't work out though, did it?)" if balance < starting_balance and all_ins == rounds else dare_devil
			dare_devil = " COWARD!" if all_ins == 0 else dare_devil
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
		round_results = play_bot()
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

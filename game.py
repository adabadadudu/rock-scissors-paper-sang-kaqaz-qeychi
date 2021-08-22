# Import block
import random

# Persian language definition
R"""Define alternative of following objects
in a particular language. Perisan by default
"""
rock = "سنگ"
paper = "کاغذ"
scissors = "قیچی"
selections = [rock, paper, scissors]

r"""Define alternative of game states (
equal,user won, system won) in a specifc
language. Persian by default
"""
user_won = "کاربر برد"
system_won = "سیستم برد"
equal_wonno = "برابر"

########################################
# user and system parameters are input #
# of user and system random choice     #
########################################


def who_is_winner(user,system):
	r"""Get user,system selection and return winner
	if user won it returns True and if system won
	it returns false else.

	NOTE: Don't use this function without checking
	arguments!
	"""
	if user == rock:
		return system == scissors
	elif user == scissors:
		return system == paper
	elif user == paper:
		return system == rock

def return_winner(user,system):
	R"""Check equal case
	this function uses who_is_winner function
	to find out who is winner or game is equal

	This functoin return + if user won and
	return - if system won else return =
	"""
	if user == system:
		return "="
	else:
			result = who_is_winner(user,system)
			if result == True:
				return "+"
			elif result == False:
				return "-"


def print_winner(user,system):
	R"""Print winner
	Get user and system choices
	and print game result"""
	won = return_winner(user,system)

	if won == '=': print(equal_wonno)
	if won == '+': print(user_won)
	if won == '-': print(system_won)

def help():
	"Print help message"
	print (r"""
	Enter sang or kaqaz or cheychi to match
	or enter Ctrl+D or Ctrl+C to exit
	sang: rock
	qeychi: scissors
	kaqaz: paper

	You can find more document and help  in README.md
	""")

help()

while True:
	user = input ('-'.join(selections)+': ').lower()
	system = random.choice(selections)
	print_winner(user,system)

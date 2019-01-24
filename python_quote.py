import random
import sys

quotes = ("It's just a flesh wound.", 
		  "He's not the Messiah. He's a very naughty boy!",
          "THIS IS AN EX-PARROT!!")

def random_python_quote():
	rand_ind = random.randint(0, len(quotes) - 1)
	return quotes[rand_ind]


def rearange_input():
	'''
		append all users input items into a list
		randomly append item to a new array and remove it from the one you are looping through
		OR random.randint
	'''
	array = sys.argv[1:]


	result_array = []
	for i in range(1, len(sys.argv)):
		item = random.choice(array)
		result_array.append(item)
		array.remove(item)
	return result_array





if __name__ == '__main__':
	quote = random_python_quote()
	print(quote)
	rearange = rearange_input()
	print(rearange)
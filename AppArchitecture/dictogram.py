
from __future__ import division, print_function # Python 2 and 3 compatibility

class Dictogram(dict):
	'''Dictogram is a histgram implemented as a subclass of dict type'''

	def __init__(self, word_list=None):
		'''initialize histogram as a new dict and count given words'''
		super(Dictogram, self).__init__()
		self.types = 0
		self.tokens = 0
		# count word in given list, if any
		if word_list is not None:
			for word in word_list:
				self.add_count(word)


	def add_count(self, word, count=1):
		'''increase frequency count by given count amount'''
		# TODO: increase word frequency by count
		if word in self:
			self[word] += count
			self.tokens += 1

		else: 
			self[word] = 1
			self.types += 1
			self.tokens += 1

	def frequency(self, word):
		'''return frequency count of gien word, or 0 if word is not found'''
		if word in self:
			return self[word]
		else:
			return 0


def print_histogram(word_list):
	print('word list: {}'.format(word_list))
	# create a dictogram and display its content
	histogram = Dictogram(word_list)
	print('dictogram: {}'.format(histogram))
	print('{} tokens, {} types'.format(histogram.tokens, histogram.types))
	for word in word_list[-2:]:
		freq = histogram.frequency(word)
		print('{!r} occurs {} times'.format(word, freq))
	print()


def main():
	import sys
	arguments = sys.argv[1:]
	if len(arguments) >= 1:
		print_histogram(arguments)
	else:
		# test histogram on letters in a word
		string = 'abracadabra'
		print_histogram(list(string))

		# test histogram on a set of words
		fish_text = 'one fish two fish green fish blue fish'
		print_histogram(fish_text.split())

		# test histogram on a long repetetive sentence
		wood_chuck_text = 'how much wood would a wood chuck chuck if a wood chuck could chuck wood'
		print_histogram(wood_chuck_text.split())


if __name__ == "__main__":
	main()




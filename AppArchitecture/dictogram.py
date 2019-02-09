
from __future__ import division, print_function # Python 2 and 3 compatibility

class Dictogram(file):
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
			self[word] += 1
			self.tokens += 1
		else: 
			self[word] = 1
			self.types += 1
			self.tokens += 1

	def frequency(self, word):
		'''return frequency count of gien word, or 0 if word is not found'''
		if word in self:
			return self[dict]
		else:
			return 0

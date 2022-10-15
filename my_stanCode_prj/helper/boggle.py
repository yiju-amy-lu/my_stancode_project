"""
File: boggle.py
Name: Yi-Ju Lu
----------------------------------------
To make a 4*4 boggle game
find every possible word from letters that user key in
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	1. To make a 4*4 game, we need regulate input time (4)
	2. Make lists to hold all input words, finding words
	3. find_boggle: used input_list to find words in the dictionary
	4. find_boggle_helper: Used helper function to check if finding words were involved in dict
	"""

	####################
	n = 0  # to calculate how many times we input words
	input_lst = []  # 4*4 list for input words

	while n < 4:  # user input words
		letters = input(f'{n+1} rows of letters: ')
		letters = letters.lower()  # case-insensitive
		letter_lst = letters.split()
		if len(letters) != 7:  # total letters + space != 7 -> break
			print("Illegal format")
			break
		else:
			input_lst.append(letter_lst)  # make 4*4 list ->[[...], [...], [...], [...]]
			n += 1
	# print(input_lst)

	start = time.time()
	find_boggle(input_lst)  # use input_lst to find words
	end = time.time()
	####################

	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def find_boggle(input_lst):
	"""
	1. use input_list to find every word
	2. create a word_lst to hold all words in dictionary
	3. use helper to check possible words
	:param input_lst: searching list
	:return: None
	"""
	word_list = read_dictionary()  # to hold all words in dict
	counter = [0]  # calculate how many words are found
	found_lst = []  # to hold all words found in the dict

	for i in range(len(input_lst)):
		for j in range(len(input_lst[i])):
			letter = input_lst[i][j]  # each searching letter in the input_lst
			find_boggle_helper(input_lst, word_list, found_lst, [(i, j)], i, j, letter, counter)
	print("There are ", str(counter[0]), "words in total.")


def find_boggle_helper(input_lst, word_list, found_lst, pos_lst, i, j, letter, counter):
	"""
	:param input_lst: all input words
	:param word_list: all words in dict
	:param found_lst: all words from input_lst were found in the dict
	:param pos_lst: position to hold the position of  the neighbor word
	:param i: position of searching letter
	:param j: position of searching letter
	:param letter: searching letter
	:param counter: counter for each words found in the dict
	:return: None
	"""

	if len(letter) >= 4:  # base case
		# Check
		if letter in word_list and letter not in found_lst:
			print("found: ", letter)
			found_lst.append(letter)
			counter[0] += 1

	for x in range(-1, 2):  # to check neighbor letter
		for y in range(-1, 2):
			if has_prefix(letter, word_list):
				# Append
				if 0 <= i+x < len(input_lst) and 0 <= j+y < len(input_lst[x]):
					if (i+x, j+y) not in pos_lst:
						letter += input_lst[i+x][j+y]
						pos_lst.append((i+x, j+y))  # used location of each neighbor letter
						# Explore
						find_boggle_helper(input_lst, word_list, found_lst, pos_lst, i+x, j+y, letter, counter)
						# Un-choose
						letter = letter[0:len(letter)-1]
						pos_lst.pop()


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""

	word_list = []
	with open(FILE, 'r') as f:
		for word in f:
			words = word.strip()
			word_list.append(words)
		return word_list


def has_prefix(sub_s, word_list):
	"""
	:param word_list:
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in word_list:
		if word.startswith(sub_s):  # if sub_s in list, then return true and keep tracking
			return True
	return False


if __name__ == '__main__':
	main()

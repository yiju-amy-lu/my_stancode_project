"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time  # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'  # This is the filename of an English dictionary
EXIT = '-1'  # Controls when to stop the loop


def main():
    """
    1. use while loop for user to input searching word
    2. find anagram
        use recursion to check each char in dictionary list
    """

    ####################

    print('Welcome to stanCode "Anagram Generator"(or -1 to quit)')
    while True:
        anagram = input('Find anagrams for: ')
        start = time.time()
        if anagram == EXIT:
            break
        else:
            print("Searching...")
            find_anagrams(anagram)
            end = time.time()
    ####################

    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end - start} seconds.')


def read_dictionary():
    """
    1. dict: first letter, length ex: {first letter: {length: [words]}}
    2. set
    3. sorted

    """

    word_dict = {}  # dict is not ordered-type, can reduce searching time
    with open(FILE, 'r') as f:
        for word in f:
            words = word.strip()
            word_dict[words] = 0  # set all value as constant
        return word_dict

    # word_lst = []
    # with open(FILE, 'r') as f:
    #     for word in f:
    #         words = word.strip()
    #         word_lst.append(words)
    #     return word_lst


def find_anagrams(s):
    """
    :param s: input word
    :return: none
    """
    word_dict = read_dictionary()  # new arg to hold dictionary
    counter = [0]  # initialize counter
    anagrams_lst = []  # empty list to hold every anagram word
    find_anagrams_helper(s, '', '', len(s), counter, word_dict, anagrams_lst)  # create a helper func
    print(str(counter[0]), 'anagram:', anagrams_lst)  # when searching completed, print result

    # word_lst = read_dictionary()  # word lst to hold dictionary list
    # counter = [0]                 # initialize counter
    # anagrams_lst = []             # empty list to hold every anagram word
    # find_anagrams_helper(s, '', '', len(s), counter, word_lst, anagrams_lst)  # create a helper func
    # print(str(counter[0]), 'anagram:', anagrams_lst)  # when searching completed, print result


def find_anagrams_helper(s, current_str, used_location, ans_len, counter, word_dict, anagrams_lst):
    """
    :param s: searching word
    :param current_str: empty str to hold every ch
    :param used_location: empty str to hold every digit => used for check each ch in string
    :param ans_len: target length
    :param counter: used for calculate how many words are found
    :param word_dict: list of dictionary
    :param anagrams_lst: empty list to hold every anagram word
    """
    # base case
    if len(current_str) == ans_len:
        # check: str in keys and not in ana_lst
        if current_str in word_dict.keys() and current_str not in anagrams_lst:
            anagrams_lst.append(current_str)
            counter[0] += 1
            print('Found: ' + current_str)
            print('Searching...')

    else:  # recursion
        for i in range(len(s)):
            # early stopping
            if has_prefix(current_str, word_dict.keys()):
                # Append
                if str(i) not in used_location:
                    current_str += s[i]
                    used_location += str(i)
                    # Explore
                    find_anagrams_helper(s, current_str, used_location, ans_len, counter, word_dict, anagrams_lst)
                    # Un-choose
                    current_str = current_str[0:len(current_str) - 1]
                    used_location = used_location[0:len(used_location) - 1]

    # base case
    # if len(current_str) == ans_len:
    #     # check
    #     if current_str in word_lst and current_str not in anagrams_lst:
    #         anagrams_lst.append(current_str)
    #         counter[0] += 1
    #         print('Found: ' + current_str)
    #         print('Searching...')
    #
    # else:
    #     for i in range(len(s)):
    #         # early stopping
    #         if has_prefix(current_str, word_lst) is False:
    #             pass
    #         else:
    #             # Append
    #             if str(i) not in used_location:
    #                 current_str += s[i]
    #                 used_location += str(i)
    #                 # Explore
    #                 find_anagrams_helper(s, current_str, used_location, ans_len, counter, word_lst, anagrams_lst)
    #                 # Un-choose
    #                 current_str = current_str[0:len(current_str)-1]
    #                 used_location = used_location[0:len(used_location)-1]


def has_prefix(sub_s, word_dict):
    """
    :param word_dict:
    :param sub_s: sub str of searching word
    :return: boolean
    """

    for word in word_dict:
        if word.startswith(sub_s):  # if sub_s in dict, then return true and keep tracking
            return True
    return False


if __name__ == '__main__':
    main()

"""
File: largest_digit.py
Name: Yi-Ju Lu
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: searching number
	:return: largest digit
	"""
	# Make int all positive
	if n < 0:
		n = -n
	# use helper function to run recursion
	return find_largest_digit_helper(n, 0)
	# return max_digit


def find_largest_digit_helper(n, max_num):
	# base case
	if n == 0:
		return max_num
	else:
		# to find the largest digit
		ans = n % 10
		if max_num < ans:
			max_num = ans
		return find_largest_digit_helper(n//10, max_num)


if __name__ == '__main__':
	main()

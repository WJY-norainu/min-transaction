from random import randint
from transaction_calculator import *
import os

def run():
	file_path = input("Enter the path to store this test case into:\n")
	if os.path.exists(file_path):
		is_overwrite = input("%s already exists. Overwrite? (y/n):\n" % file_path)
		if is_overwrite.lower() not in ('y', 'yes'):
			return
	N = int(input("Enter the number of people:\n"))
	T = int(input("Enter the number of transactions:\n"))
	
	generate_test_case(file_path, N, T)


def generate_test_case(file_path, N, T):
	transactions = list()
	total_amt = 0
	for i in range(T):
		# made transaction amount divisible by number of people to avoid floating point precision issues
		amt = randint(1, 100) * N
		transactions.append("%d %d" % (i%N, amt))
		total_amt += amt

	if total_amt != (total_amt / N) * N:
		generate_test_case(file_path, N, T)

	with open(file_path, 'w') as writer:
		writer.write("%d %d\n" % (N, T))
		writer.write('\n'.join(transactions))

if __name__ == "__main__":
	run()

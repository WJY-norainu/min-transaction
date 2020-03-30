import sys
from test import read_in_file
from transaction_calculator import *


if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage: python runner.py <file path>")
		exit()
	file_path = sys.argv[1]
	transactions, names = read_in_file(file_path)
	print(calculate(transactions, names))

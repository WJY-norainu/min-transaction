from math import isclose

'''
Inputs:
transactions:
[
	["Alice", 60],
	["Bob", 120],
	["Charlie", 30]
]
names:
["Alice", "Bob", "Charlie"]

Outputs:
assignments:
[
	["Alice", "Bob", 10.0], # this means Alice pays Bob 10
	["Charlie", "Bob", 40.0]
]
'''
def calculate(transactions, names=[]):
	input_size = len(transactions) + len(names)
	if not names:
		print("WARNING: no names have been entered. Program will proceeed assuming that every person has appeared in transactions")
	lenders, borrowers = get_net(transactions, names)
	if len(lenders) + len(borrowers) >= 10:
		print("The algorithm runs in O((X+Y)!^2), where X is the number of net borrowers and Y is the number of net lenders")
		print("Large test case can take long to run or encounter MaximumRecursionDepthExceed error")
	return subroutine(lenders, borrowers, [])


def get_net(transactions, names=[]):
	amt_by_person = dict()
	total = 0
	for name, amt in transactions:
		amt_by_person[name] = amt_by_person.get(name, 0) + amt
		total += amt
	
	if not names:
		names = amt_by_person.keys()
	amt_to_pay = total / len(names)
	if total != amt_to_pay * len(names):
		print("floating precision issue encountered. terminating program...")
		exit()

	lenders = dict()
	borrowers = dict()
	for name in names:
		net = amt_by_person.get(name, 0) - amt_to_pay
		if net > 0:
			lenders[name] = net
		elif net < 0:
			borrowers[name] = -net
		# 0 can be ignored

	return lenders, borrowers

# need to justify a greedy move where each time we pay, we pay as much as we can
def subroutine(lenders, borrowers, assignments):
	total_lent_amt = sum(lenders.values())
	total_borrowed_amt = sum(borrowers.values())
	if total_lent_amt != total_borrowed_amt:
		print(total_lent_amt, total_borrowed_amt)
	assert total_lent_amt == total_borrowed_amt, "the net amt lent should be equal to net amt borrowed"
	if not lenders and not borrowers:
		return assignments

	# try all possible assignments
	answer = []
	for lender in lenders.copy():
		lent_amt = lenders.pop(lender)
		for borrower in borrowers.copy():
			borrowed_amt = borrowers.pop(borrower)
			assignments.append([borrower, lender, min(lent_amt, borrowed_amt)])
			# if amts match, recurse without the current lender and borrower
			if lent_amt == borrowed_amt:
				curr_ans = subroutine(lenders, borrowers, assignments)
			# if borrowed_amt not fully paid for, add remaining to borrowers and recurse
			elif lent_amt < borrowed_amt:
				new_borrowed_amt = borrowed_amt - lent_amt
				borrowers[borrower] = new_borrowed_amt
				curr_ans = subroutine(lenders, borrowers, assignments)
				borrowers.pop(borrower)
			# if lent_amt not fully paid to, add remaining to lenders and recurse
			else:
				new_lent_amt = lent_amt - borrowed_amt
				lenders[lender] = new_lent_amt
				curr_ans = subroutine(lenders, borrowers, assignments)
				lenders.pop(lender)

			if (not answer) or (len(answer) > len(curr_ans)):
				answer = curr_ans.copy()
			assignments.pop() 
			borrowers[borrower] = borrowed_amt
		lenders[lender] = lent_amt
	return answer


if __name__ == "__main__":
	transactions = [
		["Alice", 60],
		["Bob", 120],
		["Charlie", 30]
	]
	names = ["Alice", "Bob", "Charlie"]
	print(calculate(transactions, names))

	transactions = [
		["Ali", 10],
		["Zack", 30]
	]
	names = ["Ali", "Zack"]
	print(calculate(transactions, names))

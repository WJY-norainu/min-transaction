'''
Input format:
[
	["Alice", 60],
	["Bob", 120],
	["Charlie", 30]
]

Output format:
[
	["Alice", "Bob", 10],
	["Charlie", "Bob", 40]
]
'''
def calculate(transactions):
	lenders, borrowers = calculate_net_lenders_borrowers(transactions)
	return subroutine(lenders, borrowers, [])


def calculate_net_lenders_borrowers(transactions):
	amt_by_person = dict()
	total = 0
	for name, amt in transactions:
		amt_by_person[name] = amt_by_person.get(name, 0) + amt
		total += amt
	
	amt_to_pay = total / len(amt_by_person)
	lenders = dict()
	borrowers = dict()
	for name in amt_by_person:
		net = amt_by_person[name] - amt_to_pay
		if net > 0:
			lenders[name] = net
		elif net < 0:
			borrowers[name] = -net
		# 0 can be ignored

	return lenders, borrowers

# need to justify a greedy move where each time we pay, we pay as much as we can
def subroutine(lenders, borrowers, assignments):
	assert sum(lenders.values()) == sum(borrowers.values()), "the net amt lent should be equal to net amt borrowed"
	if not lenders and not borrowers:
		return assignments

	# try all possible assignments
	answer = []
	for lender in lenders:
		lent_amt = lenders.pop(lender)
		for borrower in borrowers:
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

transactions = [
	["A", 16],
	["B", 18],
	["C", 3],
	["D", 3],
	["E", 0]
]
transactions = [
	["Alice", 60],
	["Bob", 120],
	["Charlie", 30]
]
#print(calculate(transactions))

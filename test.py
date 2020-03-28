from transaction_calculator import *


'''
calculate_net_lenders_borrowers
'''

'''
subroutine
'''
def is_legal_assignment(lenders, borrowers, assignments):
	lent_amt = sum(lenders.values())
	borrowed_amt = sum(borrowers.values())
	if borrowed_amt != lent_amt:
		print("Borrowed amount and lent amount don't match")
		return False
	for borrower, lender, amt in assignments:
		borrowers[borrower] -= amt
		lenders[lender] -= amt
	if sum(borrowers.values()) != sum(lenders.values()):
		print("Assigned amount doesn't match borrowed/lent amount")
		return False
	return True

def test1():
	lenders = {
		'C': 5,
		'D': 5,
		'E': 8
	}
	borrowers = {
		'A': 8,
		'B': 10
	}
	
	expected_length = 3
	assignments = subroutine(lenders, borrowers, [])
	if len(assignments) != 3:
		print("test1 failed")
	if is_legal_assignment(lenders, borrowers, assignments):
		print("test1 passed")
	else:
		print("test1 failed")

def test2():
	borrowers = {}
	lenders = {}
	expected_length = 0
	assignments = subroutine(lenders, borrowers, [])
	if assignments != []:
		print("test2 failed")
	else:
		print("test2 passed")

'''
calculate
'''


test1()
test2()
# min-transcation

## setup
Python 3.6 or above

## scripts
* `run.py` supports running scripts from command line
	* running `python run.py <file path>` outputs the answer for the inputs specified `<file path>`
	* eg: `python run.py random.in`
	* for file inputs, the first line should contain 2 space-separated numbers, N and T. N is the number of people. T is the number of transactions. Each of the following T lines has 2 space-speratated components: name of the payer (which will be read as a String), amount paid (which will be read as an integer). Refer to `random.in` for example
* `transaction_calculator.py` contains the implemented solution and documentation for input and output format
	* running `python transcation_calculator.py` will print out answers for the examples in email
* `test.py` contains test cases
	* running `python test.py` will print out the result of running tests
* `test_generator.py` is a utility script to generate random test cases
	* running `python test_generator.py` will launch an interactive session to generate test case according to specified number of people and transactions

## proof of correctness
The solution involves a greedy move where each time a person is chosen to pay, he or she pays as much as possible, which is determined by taking a min between the remaining net to receive of the lender and the remaining net to pay of the borrower. 

For example, if A, who need to pay 10 net, is chosen to pay B, who need to receive 20 net, then A will pay all 10. If A need to pay 10 net and is chosen to pay someone who need to receive 5 net, then A will pay 5.

Intuition: without loss of generality, assume A has borrowed less than B has lent. If we don't let A pay as much as possible, then the remaining part need to go through one more transaction to be allocated to some person. We could have reduced the need of 1 extra transaction by letting A pay to B in full in the first place.

## note on complexity
The implemented solution runs O((X+Y)!^2), where X is the number of net borrowers and Y is the number of net lenders.

## proof of NP-completeness
TBD

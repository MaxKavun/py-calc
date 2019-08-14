import calculator

def test_multiplication():
	if calculator.main(2,2) == 4:
		print("Unit test is OK/WORKS")
	else:
		print("Unit test was FAILED/ERROR")
test_multiplication()

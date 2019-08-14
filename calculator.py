import sys

def main(num1, num2):
	summ = int(num1) * int(num2)
	print(summ)
	return summ

if len(sys.argv) == 3:
	main(sys.argv[1],sys.argv[2])
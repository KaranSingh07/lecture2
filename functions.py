def square(x):
	return x*x

def main():
	for i in range(10):
		print("{} squared is {}".format(i,square(i)))	#print(f"{i} squared is {square(i)}")

if __name__ == "__main__":
	main()

		# This tells the python interpreter that if this file is being executed, run the main() function.
		# And if the function square() is imported by any other file, then run only the square() function. [For instance view the modules.py]
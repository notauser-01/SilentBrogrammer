def square(x):
	return x * x

print("Pick a decimal number to square:")
somenumber = eval(input())

while type(somenumber)==int:
	print("That is not a decimal number, please try again.")
	somenumber = eval(input())

print(square(somenumber))
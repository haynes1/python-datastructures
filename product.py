def multiply(a,b):
	product = 0

	if b < 0:
		a = multiply(a,-1)
		b = abs(b)

	for i in range(0,b):
		product = product + a

	return product


print "multiply 2 * 3 ", multiply(2,3)
print "multiply -2 * 3", multiply(-2,3)
print "multiply 2 * -3", multiply(2,-3)
print "multiply -2 * -3", multiply(-2,-3)
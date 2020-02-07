def memoize(f):
	memo = {}

	def helper(x):
		if x not in memo:
			memo[x] = f(x)
		return memo[x]

	return helper


@memoize
def Fib(lim):
	if lim <= 1:
		return lim
	else:
		return Fib(lim-1)+Fib(lim-2)


def Sum(lim):
	total = 0
	if lim %2 == 0:
		total += lim
		return total
	return Sum()

print('Fibonacci = ', Fib(10))
print('Sum = ', Sum)

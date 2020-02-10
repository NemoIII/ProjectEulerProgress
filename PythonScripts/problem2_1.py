def memoize(f):
	memo = {}

	def helper(x):
		if x not in memo:
			memo[x] = f(x)
		return memo[x]

	return helper


@memoize
def Fib(n):
	if n <= 1:
		return n
	else:
		return Fib(n-1)+Fib(n-2)


def Sum(lim):
	n=Fib(0)
	i = 0
	total = 0
	while n < lim:
		i += 1
		n = Fib(i)
		if n %2 == 0:
			total += n

	return total


print('Fibonacci = ', Fib(10))
print('Sum = ', Sum(4000000))

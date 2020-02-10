def fib(lim):
	after, before = 0, 1
	counter=0
	while before<lim:
		if before%2==0:
			counter+=before
		after, before = before, after+before
		print(before)
	print("-" * 31)
	print("Soma dos valores par = %s" % counter)

fib(4000000)

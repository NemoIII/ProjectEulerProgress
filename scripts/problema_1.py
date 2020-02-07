def f(x): return x%3==0 or x%5==0
print(sum(filter(f, range(1, 1000))))

'''Using the formula 1 + 2 + 3 + ... + n = n*(n+1)/2.

Sum of all numbers <1000 divisible by 3:
3 + 6 + 9 + ... + 999 = 3 * (1 + 2 + 3 + ... + 333) = 3 * 333*334/2 = 166833

Sum of all numbers <1000 divisible by 5:
5 + 10 + 15 + ... + 995 = 5 * (1 + 2 + 3 + ... + 199) = 5 * 199*200/2 = 99500

Adding these up, those numbers divisible by 3*5 = 15 are counted double. Therefore need to subtract these once:

Sum of all numbers <1000 divisible by 15:
15 + 30 + 45 + ... + 990 = 15 * (1 + 2 + 3 + ... + 66) = 15 * 66*67/2 = 33165

Thus getting the result 166833 + 99500 - 33165 = 233168.'''
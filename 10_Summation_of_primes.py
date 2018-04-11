# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

def isprime(x):
    if x <= 1:
        return False
    elif x == 2:
        return True
    else:
        for i in range(2, x):
            if x % i == 0:
                return False
        return True


total = 0
for i in range(2000000):
    if isprime(i) == True:
        total += i
print(total)

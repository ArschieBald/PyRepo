# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
n = 600851475143
pf = 2
while n != 1:
    pf += 1
    while n % pf == 0:
        n /= pf

print(pf)

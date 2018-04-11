# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

def isprime(x): # Asal sayı olup olmadığını bulan bir fonksiyon tanımladım.
    if x <= 1:
        return False
    if x == 2:
        return True
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


counter = 0
n = 1
while True:
    if isprime(n) == True: # n sayısı asal ise sayacı artıracak ve sayaç 10001 olunca programı durdurup n'i bastıracak.
        counter += 1
    if counter == 10001:
        print(n)
        break
    n += 1

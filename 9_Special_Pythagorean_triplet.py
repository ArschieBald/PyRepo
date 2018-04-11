# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a**2 + b**2 = c**2
# For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# Tembelce bir çözüm oldu :)
a = 3
b = 4
c = 5
while True:
    while a + b + c < 1000:
        a += 3
        b += 4
        c += 5
    if a + b + c == 1000:
        print(a * b * c)
        break
    else:
        a = 5
        b = 12
        c = 13
    while a + b + c < 1000:
        a += 5
        b += 12
        c += 13
    if a + b + c == 1000:
        print(a * b * c)
        break
    else:
        a = 8
        b = 15
        c = 17
    while a + b + c < 1000:
        a += 8
        b += 15
        c += 17
    if a + b + c == 1000:
        print(a * b * c)
        break
    else:
        a = 7
        b = 24
        c = 25
    while a + b + c < 1000:
        a += 7
        b += 24
        c += 25
    if a + b + c == 1000:
        print(a * b * c)
        break

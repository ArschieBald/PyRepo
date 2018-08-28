def F(n):
    if n == 1 or n == 2:
        return 1
    elif n == 3:
        return 2
    a = 1
    b = 1
    counter = 3
    while True:
        a, b = b, a + b
        counter += 1
        if n == counter:
            break
    return a + b


i = 3
while True:
    x = F(i)
    x = str(x)
    if len(x) == 1000:
        break
    i += 1
print(i)

t = 1
total = 0
for i in range(2,101): # 100! sayısını bulduk.
    t *= i
str_t = str(t) # String'e çevirdik.
for i in range(len(str_t)):
    total += int(str_t[i]) # String'in her bir basamağını int'e çevirip total değişkeninde topladık.
print(total)
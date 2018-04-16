# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.

counter = 0
for i in range(1, 1000000):
    new_counter = 1  # Kendisini de saymak için sayacı 1'den başlattım.
    start_number = i
    while i != 1:
        if i % 2 == 0:
            for j in range(10, 0, -1):  # 10 sayısını rastgele verdim.
                if i % (2 ** j) == 0:  # 2'nin üslerinden en büyük olana bölersem işlemi kısaltırım.
                    i /= (2 ** j)
                    new_counter += j
        else:  # Tek sayı 3*i+1 işlemine girdikten sonra kesin olarak çift olacağından 2'ye böldüm.
            i = (3 * i + 1) / 2
            new_counter += 2
    if new_counter > counter:
        counter = new_counter
        n = start_number
print(counter)
print(int(n))

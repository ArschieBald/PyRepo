# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#
#
# How many such routes are there through a 20×20 grid?

triangle_list = [1, 1]
# Pascal üçgeninin n * 2. adımında, ortadaki sayı, nxn'lik ızgaradaki bütün olasılıkların sayısını verir.
for n in range(39):  # Dizilerde indisler 0'dan başladığı için 40. adım 39. indis demektir.
    new_list = [1, 1]
    for i in range(1, len(triangle_list)):
        new_list.insert(i, triangle_list[i - 1] + triangle_list[i])
    triangle_list = new_list
triangle_list.sort(reverse=True)  # Büyükten küçüğe sıralayıp ilk elemanı bastırdım.
print(triangle_list[0])

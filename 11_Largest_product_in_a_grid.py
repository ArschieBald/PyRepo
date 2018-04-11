# In the 20×20 grid below, four numbers along a diagonal line have been marked in red.
#
# 08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
# 49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
# 81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
# 52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
# 22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
# 24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
# 32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
# 67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
# 24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
# 21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
# 78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
# 16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
# 86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
# 19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
# 04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
# 88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
# 04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
# 20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
# 20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
# 01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
#
# The product of these numbers is 26 × 63 × 78 × 14 = 1788696.
#
# What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?

line = "08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08"
line1 = "49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00"
line2 = "81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65"
line3 = "52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91"
line4 = "22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80"
line5 = "24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50"
line6 = "32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70"
line7 = "67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21"
line8 = "24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72"
line9 = "21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95"
line10 = "78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92"
line11 = "16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57"
line12 = "86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58"
line13 = "19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40"
line14 = "04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66"
line15 = "88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69"
line16 = "04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36"
line17 = "20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16"
line18 = "20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54"
line19 = "01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"
matrix = [line.split(), line1.split(), line2.split(), line3.split(), line4.split(), line5.split(), line6.split(),
          line7.split(), line8.split(), line9.split(), line10.split(), line11.split(), line12.split(), line13.split(),
          line14.split(), line15.split(), line16.split(), line17.split(), line18.split(), line19.split()]
# Satırlardaki her bir sayıyı matrisin satırlarına string olacak şekilde tanımladım.

list0 = list()
product = 1
for i in matrix:
    for j in range(len(i)):
        i[j] = int(i[j]) # String şekilde tanımlanmış matrisi, int'e çevirdim.

# Yatay kısımdaki çarpımları bulmak için aşağıdaki kodları yazdım.(60-66)
for i in matrix:
    for j in range(len(i)):
        if j == 17:
            break
        new_product = i[j] * i[j + 1] * i[j + 2] * i[j + 3]
        if new_product > product:
            product = new_product

# Dikey kısımdaki çarpımları bulmak için aşağıdaki kodları yazdım.(69-75)
for j in range(len(matrix)):
    for i in range(len(matrix[j])):
        if i == 17:
            break
        new_product = matrix[i][j] * matrix[i + 1][j] * matrix[i + 2][j] * matrix[i + 3][j]
        if new_product > product:
            product = new_product

# Matris köşegeninin alt kısmındaki çaprazların çarpımını bulmak için aşağıdaki kodları yazdım.(78-84)
for k in range(17, 0, -1):
    for i in range(len(matrix)):
        if i == k:
            break
        new_product = matrix[i + 17 - k][i] * matrix[i + 18 - k][i + 1] * matrix[i + 19 - k][i + 2] * matrix[i + 20 - k][i + 3]
        if new_product > product:
            product = new_product

# Matris köşegeninin üst kısmındaki çaprazların çarpımını bulmak için aşağıdaki kodları yazdım.(87-93)
for k in range(17, 0, -1):
    for i in range(len(matrix)):
        if i == k:
            break
        new_product = matrix[i][i + 17 - k] * matrix[i + 1][i + 18 - k] * matrix[i + 2][i + 19 - k] * matrix[i + 3][i + 20 - k]
        if new_product > product:
            product = new_product

# Matris ters köşegeninin alt kısmındaki çaprazların çarpımını bulmak için aşağıdaki kodları yazdım.(96-102)
for k in range(19, 2, -1):
    for i in range(len(matrix)):
        if (i + 19 - k) == 17:
            break
        new_product = matrix[i + 19 - k][19 - i] * matrix[i + 20 - k][18 - i] * matrix[i + 21 - k][17 - i] * matrix[i + 22 - k][16 - i]
        if new_product > product:
            product = new_product

# Matris ters köşegeninin üst kısmındaki çaprazların çarpımını bulmak için aşağıdaki kodları yazdım.(105-111)
for k in range(19, 2, -1):
    for i in range(len(matrix)):
        if (k - i) == 2:
            break
        new_product = matrix[i][k - i] * matrix[i + 1][k - i - 1] * matrix[i + 2][k - i - 2] * matrix[i + 3][k - i - 3]
        if new_product > product:
            product = new_product
print(product)

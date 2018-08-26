dic = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26}
total = 0
with open("p022_names.txt", "r") as file:  # Soruda verilen dosyayı açtım fakat dosyadaki ilk tırnak işareti ile en sondaki tırnak işaretini sildim.
    content = file.read()
    list0 = content.split('","')  # split ile gereksiz yerleri atıp listenin elemanlarına ayırdım.
    list0.sort()  # Alfabetik sıraladım.
    for i in list0:
        summation = 0
        for j in i:
            summation += dic[j]  #Listedeki adların her birinin harfini sözlükteki sayısal karşılığı ile topladım.
        total += (list0.index(i) + 1) * summation  # index ile elemanın hangi indexte olduğunu buldum fakat indexler 0'dan başladığı için 1 ekledim.
    print(total)

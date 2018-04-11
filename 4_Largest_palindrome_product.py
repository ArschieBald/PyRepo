# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

def palindrome(x): #Bir sayının palindrom olup olmadığını belirleyen bir fonksiyon oluşturdum.
    y = list(str(x)) #Sayının rakamlarını stringler halinde listenin elemanlarına çevirdim.
    first = 0
    last = -1
    for k in range(int(len(y) / 2)): #Sayının rakamlarının adedinin tek sayı gelme ihtimali olduğundan
        if y[first] != y[last]:      #ikiye bölündükten sonra int sayıya çevirdim.
            return False
        first += 1
        last -= 1
    return True


def Lpf():
    plist = list()
    list1 = list(range(999, 99, -1))
    for i in range(999, 99, -1):
        for j in list1:
            n = i * j
            if palindrome(n) == True:
                plist.append(n)
        list1.pop(0) #Listenin ilk elemanını çıkarmamın sebebi işlem kalabalığını engellemek.
    plist.sort(reverse=True) #Oluşan yeni listeyi büyükten küçüğe sıraladım.
    print(plist[0])


Lpf()

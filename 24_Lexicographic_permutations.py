import math

digit_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
all_list = list()  # 1.000.000 sayısının bulunduğu bölgeyi araştırmak için liste oluşturdum.
digits = ''  # Örneğin ilk basamak 3. bölgede olduğundan listenin 3. sayısı olup 2'dir.1000000 sayısı, 725760 ile 1088649 sayıları arasındadır.
# Her bulduğum sayıyı string'e çevirip digits değişkenine ekledim.
for i in range(0, math.factorial(10) + 1, math.factorial(9)):  # İlk liste 0 ile 10! arasındadır ve 10 parça halindedir.
    all_list.append(i)
while True:
    k = 0  # k değişkenini hangi aralıkta olduğunu bulmak için kullandım.
    while all_list[k] < 1000000:
        k += 1
    digits += str(digit_list.pop(k - 1))  # k değişkenine göre bulduğum aralıktan hangi sayıyı çıkarıp digits değişkenine eklemem gerektiğini buluyorum.
    if len(digits) == 10:  # Eğer digits değişkeninin boyu 10'a ulatıysa istediğim sayıya ulaştım demektir, dolayısıyla programı sonlandırıyorum.
        break
    x = all_list[k - 1]  # Bulduğum yeni aralığın alt ve üst sınırlarını buluyorum ve daha sonra listeyi sıfırlıyorum.
    y = all_list[k]
    all_list = []
    for i in range(x, y + 1, math.factorial(len(digit_list) - 1)):  # Yeni aralğımı bulup parçalıyorum ve 1000000 sayısının bulunduğu aralığı seçip devam ediyorum.
        all_list.append(i)
print(digits)

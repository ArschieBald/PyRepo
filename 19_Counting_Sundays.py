year_dic = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}  # Normal yıl ve artık yılları sözlük olarak yazdım.
leap_year_dic = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
counter = 0  # Ay başında pazar olunca artacak sayaç
tuesday = 0  # Günlerin hepsini bir sayıya atadım bu sayılar 7'ye bölümünden kalan olacak şekildedir.Salı 0 ile başlıyor çünkü 1 Ocak 1901 Salı günüdür.
wednesday = 1
thursday = 2
friday = 3
saturday = 4
sunday = 5
monday = 6
rest_of_days = 25 * 366 + 75 * 365  # 25 tane artık yıl ve 75 tane normal yıl olduğundan bu şekilde tanımladım.
previous_remainder = tuesday  # Bu değişkeni yeni kalan güncellendiği zaman eskisine ihtiyacımız olacağından dolayı tanımladım.
for i in range(1901, 2001):
    if i % 4 == 0:
        for j in range(1, 13):  # Her yılın tüm aylarını temsil ediyor.
            rest_of_days = rest_of_days - leap_year_dic[
                j]  # Toplam günü belirlenen yılın belirlenen ayındaki gün sayısından çıkardım ve kalan toplam günleri güncelledim.
            remainder = leap_year_dic[j] % 7  # Güncellenen kalan sayısı sonraki ayın ilk gününü belirleyecek.
            remainder2 = (
                                     previous_remainder + remainder) % 7  # Önceki kalanı da unutmamak lazım, eğer hep sıfırdan başlarsa yanlış sonuçlar elde ederiz.
            previous_remainder += remainder
            if remainder2 == sunday:  # remainder2 değişkeni sonraki ayın ilk gününü temsil ediyor ve bunu sunday değişkeni ile kıyaslayıp koşul doğruysa sayacı artırmasını sağladım.
                counter += 1
    else:  # Bu kısımda da ilk şartla aynı durumlar geçerlidir.
        for j in range(1, 13):
            rest_of_days = rest_of_days - year_dic[j]
            remainder = year_dic[j] % 7
            remainder2 = (previous_remainder + remainder) % 7
            previous_remainder += remainder
            if remainder2 == sunday:
                counter += 1
print(counter)

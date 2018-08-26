def sod(n):  # 1'den n'e kadar olan (n dahil değil) sayıların toplamını bulan fonksiyonu tanımladım.
    total = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            total += i
    return total


t = 0
for i in range(1, 10001):
    m = sod(i)
    if m != i and sod(
            m) == i:  # Fonksiyondan çıkan sonuç ile fonksiyona girdi olarak verilen i sayısı aynı olmamalı ve girdi ile çıktının fonksiyonu girdiye eşit olmalı.
        t += i
print(t)

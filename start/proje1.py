print("---- Hesap Makinesi ----")
print("1- Toplama")
print("2- Çıkarma")
print("3- Çarpma")
print("4- Bölme")
print("5- Mod (Kalan)")
print("6- Üs Alma")

secim = int(input("Seçim yap: "))

x = float(input("Birinci sayı: "))
y = float(input("İkinci sayı: "))

if secim == 1:
    print("Sonuç:", x + y)
elif secim == 2:
    print("Sonuç:", x - y)
elif secim == 3:
    print("Sonuç:", x * y)
elif secim == 4:
    if y == 0:
        print("Hata: 0'a bölünemez!")
    else:
        print("Sonuç:", x / y)
elif secim == 5:
    print("Sonuç:", x % y)
elif secim == 6:
    print("Sonuç:", x ** y)
else:
    print("Geçersiz seçim!")

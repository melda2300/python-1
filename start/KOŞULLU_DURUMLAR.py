# if → tek koşul
# if–else → iki durum
# elif → birden fazla durum
# iç içe if → koşul içinde koşul
# mantıksal operatörler: and, or, not
# ilişkisel operatörler: <, >, <=, >=, ==, !=
# ternary ifade → tek satırlık koşul
# pass → boş bırakmak için
# kayan nokta eşitliği → abs(a-b) < tolerans

print(" Akıllı koşul sistemi uygulamasına hoş geldiniz ")

# boolean - yaş kontrolü
yas = int(input("yaşınızı giriniz: "))
if yas < 18:
    print("yaşınız reşit deyil.")
elif 18 <= yas <= 35:
    print("Durum: genc bir yetişkinsin")
else:
    print("  Durum: yetişkinsin :  ")

print(" ")
print("--------------------")
print("")

# ilişkisel operotör - Boy kontrol

boy = int(input("boy:"))
if boy < 150:
    print("Ağacın boyu uzun demek ki!")
else:
    print("Ağacın boyu kısa.")

# -----------------------------
# 3. İç içe if – Aralık kontrolü
# -----------------------------
sayi = int(input("0 ile 10 arasında bir sayı girin: "))

if sayi >= 0:
    if sayi <= 10:
        print("Sayı aralıkta ✔")
    else:
        print("Sayı 10'dan büyük ✖")
else:
    print("Sayı negatif ✖")

# -----------------------------
# 4. Çok yönlü koşul – Yazıyla sayı
# -----------------------------
deger = int(input("0–5 arası bir değer girin: "))

if deger < 0:
    print("çok küçük")
elif deger == 0:
    print("sıfır")
elif deger == 1:
    print("bir")
elif deger == 2:
    print("iki")
elif deger == 3:
    print("üç")
elif deger == 4:
    print("dört")
elif deger == 5:
    print("beş")
else:
    print("çok büyük")

# -----------------------------
# 5. Mantıksal Operatörler – and / or / not
# -----------------------------
a = int(input("a değerini girin: "))
b = int(input("b değerini girin: "))

if a > 0 and b > 0:
    print("İki sayı da pozitif ✔")
elif a > 0 or b > 0:
    print("Sayıların en az biri pozitif.")
else:
    print("Hiçbiri pozitif değil.")

# -----------------------------
# 6. pass kullanımı
# -----------------------------
x = int(input("x değerini girin: "))
if x == 5:
    print("x = 5")
else:
    pass  # hiçbir şey yapma

# -----------------------------
# 7. Ternary (Tek Satırlık Koşul)
# -----------------------------
n = int(input("Mutlak değer alınacak sayıyı girin: "))
mutlak = (-n if n < 0 else n)
print("|", n, "| =", mutlak)

# -----------------------------
# 8. Kayan Nokta Eşitlik Problemi
# -----------------------------
d1 = 1.11 - 1.10
d2 = 2.11 - 2.10

print("d1 =", d1, " d2 =", d2)
print("Sonuç:", ("EŞİT" if abs(d1 - d2) < 1e-9 else "FARKLI"))

# -----------------------------
# 9. Mini Menü Sistemi (Zincirleme koşul)
# -----------------------------
print("\nMENÜ")
print("1 - Toplama")
print("2 - Çıkarma")
print("3 - Bölme")
print("4 - Çıkış")

secim = int(input("Seçiminiz: "))

if secim == 1:
    a = int(input("Sayı 1: "))
    b = int(input("Sayı 2: "))
    print("Sonuç:", a + b)

elif secim == 2:
    a = int(input("Sayı 1: "))
    b = int(input("Sayı 2: "))
    print("Sonuç:", a - b)

elif secim == 3:
    a = int(input("Bölünen: "))
    b = int(input("Bölen: "))
    if b != 0:
        print("Sonuç:", a / b)
    else:
        print("Sıfıra bölme yapılamaz!")

elif secim == 4:
    print("Programdan çıkılıyor...")

else:
    print("Geçersiz seçim!")

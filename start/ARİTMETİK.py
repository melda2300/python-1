# Sabit Değerler ve Değişkenler
# Sabit değer: 34
# Değişken: x
# kullanıcıdan değer alma:
deger = int(input("sayı: "))

# Aritmetik Operatörler

# +	Toplama / string birleştirme
# -	Çıkarma
# *	Çarpma; "Metin" * 3 → metni tekrarlar
# /	Ondalıklı bölme
# //	Tam bölme (bölümün tam kısmı)
# %	Mod (kalan)
# **	Üs alma
print(25 // 4)   # 6
print(25 % 4)    # 1
print(25 / 4)    # 6.25

# KARIŞIK TÜRLER
# Tam + ondalık → sonuç ondalıklı olur.
x=10
y=16.5
print(x+y) # 26.5

# Operatör Önceliği
# 1. **
# 2. *, /, //, %
# 3. +, -
print(3 + 2 * 5)      # 13
print((3 + 2) * 5)    # 25

#6. Hata Türleri
# Söz Dizimi Hatası (SyntaxError)
# print("Merhaba' )
# Çalışma Zamanı Hatası (Runtime)
#  10 / 0   # ZeroDivisionError
# Mantık Hatası
# Kod çalışır ama yanlış sonuç verir.

# Kısa Atama Operatörleri
# Yazım	    |     Uzun Hali
# x += 5	|     x = x + 5
# x *= 3	|     x = x * 3
# x -= 2	|     x = x - 2

s = int(input("Saniye: "))
saat = s // 3600
s = s % 3600
dk = s // 60
sn = s % 60
print(saat, "sa", dk, "dk", sn, "sn")









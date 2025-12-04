# "4" str, 4 int → tamamen farklı tür.
# + operatörü türlere göre çalışır → string birleştirir, sayıyı toplar.
# x = 5 Python’da eşitlik değil atamadır, sol taraf sağdaki değeri alır.
# float ile int arasındaki fark: kesir içerir.
#int() keser, round() yuvarlar.
#Çoklu atama: a, b = 5, 10
# Tırnak karışırsa → SyntaxError.

print("=== Mini hesaplama ve dönüştürme uygulaması ===")

# tam sayı alma
sayi1=int(input("tam sayı girin: "))
print("Girdiğiniz tam sayı : ", sayi1, " Türü : ",type(sayi1))

# string (dizi) alma
metin=input("\n bir metini girin: ")
print("Girdiğiniz metin: ", metin, " TÜrü : ",type(metin))

# String olarak sayı alma ve tam sayıya cevirme
string_sayi=input("\n String olarak i sayı girin (ÖR: '45' ):")
if string_sayi.isdigit():
    tam_sayi=int(string_sayi)
    print("String sayı int oldu : ", tam_sayi)
else:
    print("bu string tam sayıya cevrilemez. ")


# Tam sayıyı stringe cevirme
str_sayi=str(sayi1)
print("\n Tam sayı stringe cevrildi: ",str_sayi, " TÜrü : ",type(str_sayi))

# + oporutör farkı
print(" Toplama (int) :",sayi1+10)
print("Birleştirme (str ):", str_sayi + " 10")

# coklu atama
x,y,z=100,-30,120
print("colklu atama sonucları -> x:",x, "y:" ,y , "z:",z )

# Float ile işlem
pi=3.14159
yaricapi=float(input(" Dairenin yarıcapını giriniz: "))
alam=pi*yaricapi*yaricapi
print("\nDairenin yarıcapı :" , alam )

# yuvarlama & kesma
print("\nYuvarlanmış : ",round(alam))
print("\nKesilmiş: " ,int(alam))

# type() ile kontrol
print("\n Alan deyişkenini tipi ", type(alam))

# del ile deyişken silme
a=5
print("\n silme işleminden önce a:",a)
del a
try:
    print(a)
except:
    print("a deyişkeni silindi , artık tanımlı deyil.")
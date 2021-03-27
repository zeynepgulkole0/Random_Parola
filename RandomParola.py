#Parola, bir sisteme girmemiz için belirlediğimiz harflerden, rakamlardan ve özel karakterlerden oluşan sözcüktür, metindir.

import random

harfler = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
rakamlar = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
isaretler = ['!', '.', '_', '%', '&', ',', '*', '+' , '-', '?', ':', '#', '<', '>', '$', '=', '?', '/' ]

#f"" ifadeleri f-string olarak geçiyor.

print("Selam. Rasgele parola üretimi!!")
harf_Sayisi = int(input("Parolanda kaç harf olsun? \n"))
rakam_Sayisi = int(input(f"Parolanda kaç rakam olsun? \n"))
isaret_Sayisi = int(input(f"Parolanda kaç sembol olsun? \n"))


Parola = ""

#Belirli bir sayıda kodla döngü yapmak için range() fonksiyonunu kullanabiliriz.
#Range() fonksiyonu 0’dan başlayan ve 1’er artan (varsayılan olarak) ve belirtilen sayıda biten bir sayı dizisi döndürür.


for z in range(harf_Sayisi):
    Parola += random.choice(harfler)

for z in range(isaret_Sayisi):
    Parola += random.choice(isaretler)

for z in range(rakam_Sayisi):
    Parola += random.choice(rakamlar)

#Sample(liste,değer)
#Verdiğimiz bir listeden verdiğimiz değer kadar rastgele eleman seçer ve bize liste olarak döndürür.
#Pythonda join() metodu string tipi elemanı dizinin elemanları ile birleştirir.  Temel kullanımı str.join(sequence) şeklindedir.
    
parola = "".join(random.sample(Parola, len(Parola)))

#f"" ifadeleri f-string olarak geçiyor.

print(f"Sizin için olusturulan parola: {Parola}")
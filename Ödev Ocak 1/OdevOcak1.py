isim = input("Adınızı girin: ")
yaş = int(input("Yaşınızı girin: "))
doğum_yılı = int(input("Doğum yılınızı girin: "))

print(f"Merhaba {isim}! {yaş} yaşındasın ve {doğum_yılı} yılında doğmuşsun.")

sayı1 = float(input("Birinci sayıyı girin: "))
sayı2 = float(input("İkinci sayıyı girin: "))

toplam = sayı1 + sayı2
fark = sayı1 - sayı2
çarpım = sayı1 * sayı2
bölüm = sayı1 / sayı2 if sayı2 != 0 else "Tanımsız"

print(f"Toplam: {toplam}")
print(f"Fark: {fark}")
print(f"Çarpım: {çarpım}")
print(f"Bölüm: {bölüm}")
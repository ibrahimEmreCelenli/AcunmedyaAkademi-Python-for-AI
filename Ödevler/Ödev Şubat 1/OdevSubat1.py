def hesap_makinesi(sayi1, sayi2):
    toplam = sayi1 + sayi2
    fark = sayi1 - sayi2
    carpim = sayi1 * sayi2
    bolum = sayi1 / sayi2 if sayi2 != 0 else "Tanımsız"
    return toplam, fark, carpim, bolum

sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))
sonuclar = hesap_makinesi(sayi1, sayi2)
print(f"Toplam: {sonuclar[0]}, Fark: {sonuclar[1]}, Çarpım: {sonuclar[2]}, Bölüm: {sonuclar[3]}")


def palindrom_kontrol(kelime):
    return kelime == kelime[::-1]

kelime = input("Bir kelime girin: ")
if palindrom_kontrol(kelime):
    print(f"'{kelime}' bir palindromdur.")
else:
    print(f"'{kelime}' bir palindrom değildir.")


def yas_hesapla(yas):
    return 100 - yas if yas < 100 else 0

yas = int(input("Yaşınızı girin: "))
kalan_yil = yas_hesapla(yas)
print(f"100 yaşına ulaşmanıza {kalan_yil} yıl kaldı.")

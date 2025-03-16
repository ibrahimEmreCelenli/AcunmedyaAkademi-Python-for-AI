def hesapla(sayi1,sayi2,islem):
    if islem == "+":
        return sayi1+sayi2
    elif islem == "-":
        return sayi1-sayi2
    elif islem == "*":
        return sayi1*sayi2
    elif islem == "/":
        if sayi2 != 0:
            return sayi1/sayi2
        else:
            print("Bölme işlemi için ikinci sayı 0 olamaz!")
    else:
        print("Geçersiz işlem türü!")


sayi1 = int(input("Birinci sayıyı giriniz: "))
sayi2 = int(input("İkinci sayıyı giriniz: "))
islem = input("İşlemi giriniz: ")
print(hesapla(sayi1,sayi2,islem))

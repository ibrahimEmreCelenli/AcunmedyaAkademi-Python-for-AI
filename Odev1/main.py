import alisveris_listesi

def main():
    liste = alisveris_listesi.AlisverisListesi()

    while True:
        print("\nMenü:")
        print("1. Ürün Ekle")
        print("2. Son Ürünü Çıkar")
        print("3. Toplam Tutarı Görüntüle")
        print("4. Çıkış")

        secim = input("Seçiminizi yapın (1-4): ")

        if secim == "1":
            isim = input("Ürün adı: ")
            fiyat = float(input("Fiyatı: "))
            liste.urun_ekle(isim, fiyat)
            print(f"Ürün eklendi: {isim} - {fiyat} TL")

        elif secim == "2":
            urun = liste.urun_cikar()
            if urun:
                print(f"Çıkarılan ürün: {urun['isim']} - {urun['fiyat']} TL")
            else:
                print("Liste zaten boş!")

        elif secim == "3":
            toplam = liste.toplam_tutar()
            print(f"Toplam tutar: {toplam:.2f} TL")

        elif secim == "4":
            print("Çıkış yapılıyor...")
            break

        else:
            print("Geçersiz seçim, tekrar deneyin!")

if __name__ == "__main__":
    main()

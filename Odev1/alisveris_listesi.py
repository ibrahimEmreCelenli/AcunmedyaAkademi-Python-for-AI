def toplam_fiyat(urunler):
    return sum(urun['fiyat'] for urun in urunler) if urunler else 0

class AlisverisListesi:
    def __init__(self):
        self.urunler = []
    
    def urun_ekle(self, isim, fiyat):
        self.urunler.append({"isim": isim, "fiyat": fiyat})
    
    def urun_cikar(self):
        if self.urunler:
            return self.urunler.pop()
        return None
    
    def toplam_tutar(self):
        return toplam_fiyat(self.urunler)

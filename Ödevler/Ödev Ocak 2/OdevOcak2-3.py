yas = int(input("Yaşınızı girin: "))

if 0 <= yas <= 12:
    print("Yaş Grubu: Çocuk")
elif 13 <= yas <= 19:
    print("Yaş Grubu: Genç")
elif 20 <= yas <= 59:
    print("Yaş Grubu: Yetişkin")
elif yas >= 60:
    print("Yaş Grubu: Yaşlı")
else:
    print("Geçersiz yaş.")

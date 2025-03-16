notu = int(input("Notunuzu girin: "))

if 90 <= notu <= 100:
    print("Harf Notu: A")
elif 80 <= notu <= 89:
    print("Harf Notu: B")
elif 70 <= notu <= 79:
    print("Harf Notu: C")
elif 60 <= notu <= 69:
    print("Harf Notu: D")
elif 0 <= notu <= 59:
    print("Harf Notu: F")
else:
    print("Geçersiz not.")

def faktoriyel(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

sayi = int(input("Bir sayı girin: "))
print(f"{sayi}! = {faktoriyel(sayi)}")

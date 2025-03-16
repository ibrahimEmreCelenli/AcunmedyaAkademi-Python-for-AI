numbers = []

for _ in range(5):
    num = float(input("Bir sayı girin: "))
    numbers.append(num)

total = sum(numbers)
average = total / len(numbers)
max_num = max(numbers)
min_num = min(numbers)

print(f"Toplam: {total}, Ortalama: {average}, En Büyük: {max_num}, En Küçük: {min_num}")

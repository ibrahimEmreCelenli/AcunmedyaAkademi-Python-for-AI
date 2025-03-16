elements = input("Liste elemanlarını boşlukla ayırarak girin: ").split()

unique_elements = list(set(elements))  # Kümeye çevirip tekrar edenleri kaldırır

print("Tekrarsız liste:", unique_elements)

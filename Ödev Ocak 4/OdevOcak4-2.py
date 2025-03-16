words = []

for _ in range(5):
    word = input("Bir kelime girin: ")
    words.append(word)

words.reverse()  # Listeyi ters çevirir

print("Ters sıralı liste:", words)

for i in range(10):
    print(i)
    
students = ["Ali","Veli","Ahmet","Mehmet"]

for student in students:
    print("Öğrenci:" + student)
    
text = "Merhaba"

for letter in text:
    print(letter)
    

for i in range(5,20,2):
    print(i)
    
user_input = input("çıkmak için 'q' tuşuna basınız.")

while user_input != 'q':
    print("girdiğiniz değer:"+user_input)
    user_input = input("çıkmak için 'q' tuşuna basınız.")

from math import sqrt


def asal_mi(sayi):
    karekok = int(sqrt(sayi))+1
    asal = True
    i = 2
    
    while(i <= karekok):
        if sayi%i == 0:
            asal = False
            break
        i+=1

    if asal == True:
        print(f"{sayi} bir asal sayıdır.")
    
    else:
        print(f"{sayi} bir asal sayı değildir.")
            
    return

sayi = input("Bir sayı giriniz: ")
asal_mi(int(sayi))
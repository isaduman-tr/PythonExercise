Süper_lig = {"Galasatasaray":"63 puan","Beşiktaş":"65 puan","Fenerbahçe":"60 puan"}

while True:
    takım_ekle = input("Lütfen takımı giriniz : ")
    puan_ekle = input("Lütfen puanı giriniz : ")
    Süper_lig.setdefault(takım_ekle,puan_ekle)

    for i,j in Süper_lig.items():
        print(i,j)

    secim = input("Çıkmak ister misiniz ? : E/H").upper()  
    if secim=="E":
        print("Çıkış yapıldı...") 
        break
    else:
        pass 
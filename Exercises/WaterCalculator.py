def su_hesapla(kilo):
    e_hesapla = kilo * 0.04
    k_hesapla = kilo * 0.03

    cinsiyet = input("Lütfen cinsiyetinizi giriniz - Erkek/Kadın : ").lower()
    if cinsiyet == "erkek":
        print("-"*30)
        print("Günde en az",e_hesapla , "Litre su içmelisin")
        print("-"*30)
    
    elif cinsiyet =="kadın":
        print("-"*30)
        print("Günde en az",k_hesapla , "Litre su içmelisin")
        print("-"*30)
    elif not cinsiyet:
        print("Cinsiyetinizi doğru girmediniz")
    else :
        print("Hatalı giriş")


kiloinput = int(input("Lütfen kilonuzu giriniz : "))
su_hesapla(kiloinput)    


# hopkisnův zákon
pamet_Φ = []
pamet_Fm = []
pamet_Rm = []
konec = True
import time

while konec:
    kontrola = True
    while kontrola:
        print("1. Φ = Fm / Rm")
        print("2. Rm = Fm / Φ")
        print("3. Fm = Φ * Rm")
        print("4. Konec")
        vyber = float(input("Vyberte vzoreček: "))
        if  0 < vyber < 5:
            kontrola = False
        else:
            print("Zadali jste špatnou možnost")
    kontrola = True

    if vyber == 1:
        while kontrola:
            try:
                Fm = float(input("Zadejte hodnotu Fm: "))
                if 0 >= Fm:
                    print("Zadali jste špatnou hodnotu")
                else:
                    kontrola = False
            except ValueError:
                print("Zadali jste špatnou hodnotu")
        kontrola = True

        while kontrola:
            try:
                Rm = float(input("Zadejte hodnotu Rm: "))
                if 0 >= Rm:
                    print("Zadali jste špatnou hodnotu")
                else:
                    kontrola = False
            except ValueError:
                print("Zadali jste špatnou hodnotu")
        kontrola = True

        Φ = Fm / Rm

        print("Fm = ", Fm)
        print("Rm = ", Rm)
        print("Φ = Fm / Rm")
        pamet_Φ.append(Φ)
        print("Φ = ", Φ," Φ")
        print("")
        time.sleep(2)
        for i in range(len(pamet_Φ)):
            
            if i+1 == len(pamet_Φ):
                print("Aktuální. ", pamet_Φ[i]," Φ")
            else:
                print(i + 1,". ", pamet_Φ[i]," Φ")
        time.sleep(2)
        print("")

    if vyber == 2:
        while kontrola:
            try:
                Fm = float(input("Zadejte hodnotu Fm: "))
                kontrola = False
            except ValueError:
                print("Zadali jste špatnou hodnotu")
        kontrola = True

        while kontrola:
            try:
                Φ = float(input("Zadejte hodnotu Φ: "))
                if 0 >= Φ:
                    print("Zadali jste špatnou hodnotu")
                else:
                    kontrola = False
            except ValueError:
                print("Zadali jste špatnou hodnotu")
        kontrola = True

        Rm = Fm / Φ

        print("Fm = ", Fm)
        print("Φ = ", Φ)
        print("Rm = Fm / Φ")
        pamet_Rm.append(Rm)
        print("Rm = ", Rm , " MPa")
        print("")
        time.sleep(2)
        for i in range(len(pamet_Rm)):
            if i+1 == len(pamet_Rm):
                print("Aktuální. ", pamet_Rm[i], " MPa")
            else:
                print(i + 1,". ", pamet_Rm[i], " MPa")
        time.sleep(2)
        print("")

    if vyber == 3:
        while kontrola:
            try:
                Φ = float(input("Zadejte hodnotu Φ: "))
                if 0 >= Φ:
                    print("Zadali jste špatnou hodnotu")
                else:
                    kontrola = False
            except ValueError:
                print("Zadali jste špatnou hodnotu")
        kontrola = True

        while kontrola:
            try:
                Rm = float(input("Zadejte hodnotu Rm: "))
                kontrola = False
            except ValueError:
                print("Zadali jste špatnou hodnotu")
        kontrola = True

        Fm = Φ * Rm

        print("Φ = ", Φ)
        print("Rm = ", Rm)
        print("Fm = Φ * Rm")
        pamet_Fm.append(Fm)
        print("Fm = ", Fm, " t")
        print("")
        time.sleep(2)
        for i in range(len(pamet_Fm)):
            if i+1 == len(pamet_Fm):
                print("Aktuální. ", pamet_Fm[i] , " t")
            else:
                print(i + 1,". ", pamet_Fm[i], " t")
        time.sleep(2)
        print("")

    if vyber == 4:
        print("Pa Pa")
        konec = False

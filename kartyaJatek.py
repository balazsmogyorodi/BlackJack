import random


def kartyaJatek():
    lista = []
    pakli = []
    jatekos1 = []
    jatekos2 = []

    def kartyakListaba_a():
        for m in range(4):
            for i in range(2,10):
                lista.append(i)
    def karyakListaba_b():
        i = 0
        while i <16:
            lista.append(10)
            i += 1
    def asz():
        for m in range(4):
            lista.append(11)
    def keszPakli():
        kartyakListaba_a()
        karyakListaba_b()
        asz()
    def kevertPakli():
        keszPakli()
        index = 0
        random.shuffle(lista)
        while index < len(lista):
            pakli.append(lista[index])
            index += 1

    # Kevert Pakli



    # Játékos összege



    def osztas():
        lap = 0
        index = 0
        while index < 2:
            jatekos1.append(pakli[lap])
            pakli.remove(pakli[lap])
            jatekos2.append(pakli[lap])
            pakli.remove(pakli[lap])
            index += 1

    def osztasKiiras():
        osztas()
        print("1.kör")
        print("1. játékos keze:", end=" ")
        for i in range(0,len(jatekos1)):
            print(jatekos1[i],end=" ")
        print("")
        print("2. játékos keze:", end=" ")
        for i in range(0, len(jatekos2)):
            print(jatekos2[i], end=" ")
        print("")

    # Játékos keze

    def szamlalasJatekos1():
        jatekosOsszeg1 = 0
        index = 0
        while index < len(jatekos1):
            jatekosOsszeg1 += jatekos1[index]
            index += 1
        if jatekosOsszeg1 > 21:
            jatekosOsszeg1 = False
            return jatekosOsszeg1
        else:
            return jatekosOsszeg1

    def szamlalasJatekos2():
        jatekosOsszeg2 = 0
        index = 0
        while index < len(jatekos2):
            jatekosOsszeg2 += jatekos2[index]
            index += 1
        if jatekosOsszeg2 > 21:
            jatekosOsszeg2 = False
            return jatekosOsszeg2
        else:
            return jatekosOsszeg2



    def lapot1 ():
        jatekos1Ker = 5
        while jatekos1Ker < 0 or jatekos1Ker > 1:
            jatekos1Ker = int(input("Kér még lapot az 1.játékos? igen(1), nem(0): "))
        if jatekos1Ker == 0:
            return False
        elif jatekos1Ker == 1:
            lap = 0
            jatekos1.append(pakli[lap])
            pakli.remove(pakli[lap])
            return True

    def lapot1Szamitas():
        osszeg1 = szamlalasJatekos1()
        if osszeg1 == False:
            return False
        else:
            return True



    def lapot2():
        jatekos1Ker = 5
        while jatekos1Ker < 0 or jatekos1Ker > 1:
            jatekos1Ker = int(input("Kér még lapot a 2.játékos? igen(1), nem(0): "))
        if jatekos1Ker == 0:
            return False
        elif jatekos1Ker == 1:
            lap = 0
            jatekos2.append(pakli[lap])
            pakli.remove(pakli[lap])
            return True

    def lapot2Szamitas():
        osszeg2 = szamlalasJatekos2()
        if osszeg2 == False:
            return False
        else:
            return True





    def lapotJatekos1():
        eredmeny1 = lapot1Szamitas()
        if eredmeny1 == False:
            print("1. túlment 21-en!")
            return False
        else:
            print("1. játékos keze:", end=" ")
            for i in range(0, len(jatekos1)):
                print(jatekos1[i], end=" ")
            print("")
            return True


    def lapotJatekos2():
        eredmeny2 = lapot2Szamitas()
        if eredmeny2 == False:
            print("2. túlment 21-en!")
            return False
        else:
            print("2. játékos keze:", end=" ")
            for i in range(0, len(jatekos2)):
                print(jatekos2[i], end=" ")
            print("")
            return True



    def jatekMenet():
        mehet1 = True
        mehet2 = True
        mehet3 = True
        mehet4 = True
        while (mehet3 == True or mehet4 == True) and (mehet1 == True and mehet2 == True):
            mehet3 = lapot1()
            mehet4 = lapot2()
            print("\n\n\n\n")
            mehet1 = lapotJatekos1()
            mehet2 = lapotJatekos2()
        if mehet1 == False and mehet2 == False:
            return False
        else:
            return True

    def eredmeny():
        tulment = jatekMenet()
        eredmeny1 = szamlalasJatekos1()
        eredmeny2 = szamlalasJatekos2()
        print("\n\t", end="")
        if tulment == False:
            print("DÖNTETLEN!")
        elif tulment == True:
            if eredmeny1 > eredmeny2:
                print("Az 1. játékos gyözött.")
            elif eredmeny1 < eredmeny2:
                print("A 2. játékos gyözött.")
            elif eredmeny1 == eredmeny2:
                print("DÖNTETLEN!")

    def jatekUjra():
        szeretnel = 5
        while szeretnel < 0 or szeretnel > 1:
            szeretnel = int(input("Szeretnétek menni még egy kört? igen(1) nem(0) "))
        if szeretnel == 0:
            return False
        elif szeretnel == 1:
            print("\n\n\n\n")
            return True
    def teljesJatek():
        ujra = True
        while ujra == True:
            kevertPakli()
            osztasKiiras()
            eredmeny()
            ujra = jatekUjra()

    teljesJatek()



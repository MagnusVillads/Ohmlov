#Husk At Tal Skal Skrive Med Punktum . Og IKKE Komma ,

def prmenu():
    print("1) Find Spændingen (V) ")
    print("2) Find Strømmen (A)")
    print("3) Find Modtanden (Ω)")
    print("4) Stop Program ")

def U():
    I = float(input("Indtast Strømmen "))
    R = float(input("Indtast Modstanden "))
    print("U =","%4.2f"% (I*R),"V")
    print()

def I():
    U = float(input("Indtast Spændingen "))
    R = float(input("Indtast Modstanden "))
    print("I =","%4.2f"% (U/R),"A")
    print()

def R():
    U = float(input("Indtast Spændingen "))
    I = float(input("Indtast Strømmen "))
    print("R =","%4.2f"%(U/I),"Ω")
    print()

prmenu()
Menunr=int(input("Vælg menu nr. "))
wh=1

while wh==1:
    if Menunr == 1:
        print("du har valgt menu nr. 1")
        U()
        prmenu()
        Menunr=int(input("Vælg menu nr."))

    if Menunr == 2:
        print("du har valgt menu nr. 2")
        I()
        prmenu()
        Menunr=int(input("Vælg menu nr."))

    if Menunr == 3:
        print("du har valgt menu nr. 3")
        R()
        prmenu()
        Menunr=int(input("Vælg menu nr."))

    if Menunr == 4:
        print("Nu stopper programmet!!!")
        wh=2

    else:
        prmenu()
        Menunr=int(input("Vælg menu nr."))


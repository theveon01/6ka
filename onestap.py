import random
import webbrowser

start = 1
while(start != 0):
    adres = "https://x5.app/pyaterochka#/"      #адрес, по которому перейдём в конце
    firstnubmer = 0                             #была ли цифра

    for sym in range(0,8):
        searchCol = 0
        addsum = 0
        if (random.randint(0,1) == 1):
            addsum = 32
        while(True):
            if firstnubmer == 0:
                searchCol = random.randint(0,18)
                if searchCol == 14:
                    adres += chr(random.randint(48,57))
                    firstnubmer = 1
                    break
                else:
                    searchCol = random.randint(65,90)
                    adres += chr(searchCol+addsum)
                    break
            else:
                searchCol = random.randint(65,90)
                adres += chr(searchCol+addsum)
                break

    webbrowser.open(adres, new=1)

    print(adres, end = "\n\n")
    start = input("1 - продолжить!\n0 - Прекращаем\n")

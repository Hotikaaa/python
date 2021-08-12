from random import randint

pont = 0
lepes = 0


while pont < 100 :
    rnd = randint(2, 100)
    szam = int(rnd**0.5)
    for x in range(2, szam+1):
        if szam % 2 == 0:
            pont += 1
        elif szam % 3 == 0:
            pont += 2
        elif szam % 6 == 0:
            pont += 3
        elif szam % x == 0:
            pont -= 1
    lepes += 1
    print(rnd)
    

print(f"A progam lefutott \nLépések száma: {lepes}")
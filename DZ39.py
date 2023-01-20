import random
player1=input("Введите имя первого игрока: ")
player2=input("Введите имя второго игрока: ")
konfet=int(input("Сколько всего конфет: "))
maxKonf=int(input("Сколько всего конфет можно брать за раз: "))

firPlayer=random.choice([player1,player2])

switch=player1 if firPlayer==player1 else player2

while konfet>0:
    print("Ход игрока", switch)
    t=int(input("Сколько конфет для берете: "))
    while not 0 < t <= maxKonf:
        print(f"не правильно, диапозон  от 1 до {maxKonf}")
        t=int(input("Сколько конфет берете: "))
    konfet-=t
    
    if konfet>0:
        print(f'конфет осталось {konfet}')
    else:
        print(f'конфет осталось: 0')
    switch=player2 if switch == player1 else player1
win=player2 if switch == player1 else player1
print(f'Победил {win}')

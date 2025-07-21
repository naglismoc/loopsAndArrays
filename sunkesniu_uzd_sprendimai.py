import random

sk = 30
print("[" + str(sk) + "]" )
print(f'[{sk}]')
# ===================================== S 1. ===========================================
# Sugeneruokite 300 atsitiktinių skaičių nuo 0 iki 300, V
# atspausdinkite juos atskirtus tarpais V
# ir suskaičiuokite kiek tarp jų yra didesnių už 150. V
# Skaičiai didesni nei 275 turi būti atspausdinti skliausteliuose” [ ] “. V

count = 0
result = ""
for i in range(300):
    rnd_num = random.randint(0, 300) # 0 ir 300 imtinai
    if rnd_num > 150:
        count += 1

    if rnd_num > 275:
        result += f'[{rnd_num}] '
        # print(f'[{rnd_num}]', end=" ")
    else:
        result += f'{rnd_num} '
        # print(rnd_num, end=" ")
print(result)
print()
print("===========", count)

# Vienoje eilutėje atspausdinkite visus skaičius nuo 1 iki 3000, V
# kurie dalijasi iš 77 be liekanos. V
# Skaičius atskirkite kableliais. V
# Po paskutinio skaičiaus kablelio neturi būti. V

result = ""
for num in range(1, 3001):
    if num % 77 == 0:
        result += f'{num},'
print(result[:-1])
print("==========")

result = ""
for num in range(77, 3001, 77):
    result += f'{num},'
print(result[:-1])

# Nupieškite kvadratą iš “*”, kurio kraštines sudaro 25“*”.
for a in range(12):
    for i in range(12):
        print("*", end=" ")
    print()

for y in range(1,11):
    for x in range(1,11):
        print(x * y, end=" ")
    print()


# Metam monetą. Monetos kritimo rezultatą imituojam random.randint(x,x) funkcija, kur 0 yra herbas, o 1 - skaičius. Monetos metimo rezultatus išvedame į ekraną atskiroje eilutėje: “S” jeigu iškrito skaičius ir “H” jeigu herbas. Suprogramuokite tris skirtingus scenarijus kai monetos metimą stabdome:
# Iškritus herbui;
# Tris kartus iškritus herbui;
# Tris kartus iš eilės iškritus herbui;


print("5a.")
while True:
    coin = random.randint(0,1)
    if coin == 0:
        print("H")
        break
    else:
        print("S")


print("5b.")

count = 0 # 1;2;3
while True:
    coin = random.randint(0,1)
    if coin == 0:
        print("H")
        count += 1
    else:
        print("S")
    if count >= 3:
        break


print("5c.")

count = 0 #1;0;1;0;0;0;1;2;3
while True:
    coin = random.randint(0,1)
    if coin == 0:
        print("H")
        count += 1
    else:
        print("S")
        count = 0
    if count >= 3:
        break



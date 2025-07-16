# # number = 20
# print("labas")
# #          0  1   2   3   4   5   6
# numbers = [1, 5, 10, 20, 40, 80, 30]
#
# print(numbers)
# print(numbers[0])
# print(numbers[6])
# print( len(numbers)  )
# numbers[0] = 20
# print(numbers)
# numbers.append(140)
# print(numbers)
#
# print(numbers.index(5))
# numbers.reverse()
# print(numbers)
# numbers.reverse()
# numbers.insert(2,12)
# print(numbers)
#
# numbers.sort()
# print(numbers)
# #            0                1            2         3
# vardai = ['Žygimantas', 'Gabrielius', 'Jokūbas', 'Vilius']
#
# print(vardai)
# print(vardai[1])
#
# arr2d = [
#     [1, 4, 10],
#     [3, 5, 8],
#     [1, 2, 3],
#     [5, 10, 5, 7, "Žygimantas"]
# ]
# print(arr2d)
#
# vardai = [
#     ['Žygimantas', 5],
#     ['Gabrielius',3 ],
#     ['Jokūbas', 8],
#     ['Vilius']
# ]
#
# #             0  1  2  3  4  5  6  7  8  9 INDEKSAI
# my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# ###################### PIRMAS PARAMETRAS INCLUSIVE, JI IMA, ANTRAS EXCLUSIVE, JO NEIMA, IMA IKI JO######################
# # print(my_numbers[pradzia:galas:zingsnis])
# print(my_numbers)#atspausdiname viska
# print(my_numbers[6])#vienas
# print(my_numbers[0:4])#nuo iki
# print(my_numbers[4:8])
# print(my_numbers[7:])#nuo iki galo
# print(my_numbers[:4])#nuo pradzios iki nurodytos pozicijos (exclusive, jos neima. IKI jos)
# print(my_numbers[-2])#antra pozicija nuo galo
# print(my_numbers[-5:])#nuo 5 pozicijos nuo galo iki pat galo
# print(my_numbers[:-5])#nuo pradzios iki 5 pozicijos nuo galo
# print(my_numbers[2:-5])# nuo 2 pozicijos iki 5tos nuo galo
# print(my_numbers[-6:-2])#imame nuo 6 nuo galo iki 2 nuo galo
# print(my_numbers[-8:4])#teoriskai veikia, neapsikraukis =D
# print(my_numbers[:])#paima viska nuo pradzios iki galo, lygiai taip pat, kaip ir neirasius nieko
# print(my_numbers[::2])#visa imtis, kas antras elementas
# print(my_numbers[::3])#visa imtis, kas 3cias elementas
# print(my_numbers[1::2])#visa imtis nuo 1o indekso iki galo, kas antras elementas
# print(my_numbers[3:7:2])#nuo 3 indekso inclusive iki 7 exclusive kas antras elementas
# print(my_numbers[2:-2:2])#paimu viska be pirmu dvieju IR paskutiniu dvieju kas antra
# print(my_numbers[::-1])#visi elementai, bet nuo galo.
# print(my_numbers[::-2])# visa imtis, kas antras elementas BET nuo GALO
#
# rasos_printas = my_numbers[::-2]
# print(rasos_printas)
#
import random

# imtis = range(0, 10)
#
# print(imtis)
# print(imtis[1])


for i in range(0, 10):
    print(i)
print("zemiau ciklo")
#               0           1             2         3
vardai = ['Žygimantas', 'Gabrielius', 'Jokūbas', 'Vilius']

for vardas in vardai:#4
    print(vardas)


numbers = [3, 30, 40, 5, 3]

for sk in numbers:
    print(sk)
print("-----------")
print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])
print(numbers[4])
print("-----------")

for i in range(4):
    print(i)


print("-----------")

for i in range(4, 12):
    print(i)

print("-----------")

for i in range(1000000, 1000010):
    print(i)

vardai = ['Žygimantas', 'Gabrielius', 'Jokūbas', 'Vilius']

for iteracija, vardas in enumerate(vardai):#4
    if iteracija % 2 == 0:
        print(f'{iteracija + 1}. {vardas}')
    # print(str(iteracija + 1) + '. ' + vardas)



imtis = range(0,10000)
print(imtis)

for i in imtis:
    if i % 2 == 0:
        print(i)

names = [
    "Alexander", "Benjamin", "Charlotte", "Daniel", "Elizabeth",
    "Frederick", "Gabriella", "Henry", "Isabella", "Jacob",
    "Katherine", "Liam", "Madeline", "Nathaniel", "Olivia",
    "Patrick", "Quinn", "Rebecca", "Samuel", "Theresa",
    "Ulysses", "Victoria", "William", "Xavier", "Yvonne",
    "Zachary", "Abigail", "Brandon", "Cassandra", "Derek",
    "Emily", "Francis", "Grace", "Hannah", "Ian",
    "Julia", "Kevin", "Laura", "Michael", "Natalie",
    "Oscar", "Penelope", "Quincy", "Rachel", "Stephen",
    "Tracy", "Uma", "Vincent", "Wendy", "Yosef"
]

for name in names:
    if len(name) <= 3:
        print(name)

for i, name in enumerate(names):
    if i % 5 == 0:
        print(f'rasa {name} dave 10 balu')
    else:
        print(i, name)


numbers = [3, 30, 40, 5, 3]
# numbers.sort()
print(numbers)


for i,num in enumerate(numbers):
    print(i, numbers[i])


# for i, num in enumerate(numbers):
#     if num < numbers[i + 1]:
#         numbers[i] = numbers[i + 1]
#         numbers[i + 1] = num
print(numbers)

for num in numbers:
    for i in range(len(numbers) - 1):
        if numbers[i] < numbers[i + 1]:
            temp = numbers[i]
            numbers[i] = numbers[i + 1]
            numbers[i + 1] = temp

print(numbers)

print("-----------------------------------")
arr2d = [
    [1, 4, 10],
    [3, 5, 8],
    [1, 2, 3],
    [5, 10, 5]
]
print(arr2d)
sum = 0
count = 0
for row in arr2d:
    for number in row:
        sum += number
        count += 1
print(count, sum, sum/count)

dice = random.randint(1,6)
print(dice)

print("--------------------")
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
print("--------------------")
for i in range(10):
    if i > 4:
        break
    print(i)


should_roll_dice = True
while should_roll_dice:
    dice = random.randint(1, 6)
    if dice == 4:
        should_roll_dice = False


while True:
    dice = random.randint(1, 6)
    print(dice)
    if dice == 4:
        break
#
#continue
#break
#return

count = 0
total_count = 0
max = 0  # 1
for i in range(10000):
    while True:
        count += 1
        total_count += 1
        dice = random.randint(1, 6)
        if dice == 4:
            if count > max:
                max = count
            count = 0
            break

print(max, total_count)

# Įmonė parduoda žvakes po 1 EUR. Perkant daugiau kaip 1000 vienetų taikoma 3 % nuolaida, daugiau kaip 2000 vienetų- 4 % nuolaida. Parašykite programą, kuri skaičiuos žvakių kainą ir atspausdintų atsakymą kiek žvakių ir kokia kaina perkama. Žvakių kiekį generuokite ​random.randint(x,x)​ funkcija nuo 5 iki 3000.

kaina = 24.93
print(kaina * 0.96 )
print(kaina / 100 * 96)
print(kaina / 100 * 100)
print(kaina * 1)
print(kaina / 100 * 80)
print(kaina * 0.8)

kaina = 1
kiekis = 1386
if kiekis < 1000:
    print(kiekis * kaina)
elif kiekis < 2000:
    print(kiekis * kaina * 0.97)
    print( (kiekis * kaina) - (kiekis * kaina / 100 * 3)  )
else:
    print(kiekis * kaina * 0.96)


#Zvakes
#Rimui pakomentuoti apie identacijas









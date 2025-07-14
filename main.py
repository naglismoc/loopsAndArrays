# number = 20
print("labas")
#          0  1   2   3   4   5   6
numbers = [1, 5, 10, 20, 40, 80, 30]

print(numbers)
print(numbers[0])
print(numbers[6])
print( len(numbers)  )
numbers[0] = 20
print(numbers)
numbers.append(140)
print(numbers)

print(numbers.index(5))
numbers.reverse()
print(numbers)
numbers.reverse()
numbers.insert(2,12)
print(numbers)

numbers.sort()
print(numbers)
#            0                1            2         3
vardai = ['Žygimantas', 'Gabrielius', 'Jokūbas', 'Vilius']

print(vardai)
print(vardai[1])

arr2d = [
    [1, 4, 10],
    [3, 5, 8],
    [1, 2, 3],
    [5, 10, 5, 7, "Žygimantas"]
]
print(arr2d)

vardai = [
    ['Žygimantas', 5],
    ['Gabrielius',3 ],
    ['Jokūbas', 8],
    ['Vilius']
]

#             0  1  2  3  4  5  6  7  8  9 INDEKSAI
my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

###################### PIRMAS PARAMETRAS INCLUSIVE, JI IMA, ANTRAS EXCLUSIVE, JO NEIMA, IMA IKI JO######################
# print(my_numbers[pradzia:galas:zingsnis])
print(my_numbers)#atspausdiname viska
print(my_numbers[6])#vienas
print(my_numbers[0:4])#nuo iki
print(my_numbers[4:8])
print(my_numbers[7:])#nuo iki galo
print(my_numbers[:4])#nuo pradzios iki nurodytos pozicijos (exclusive, jos neima. IKI jos)
print(my_numbers[-2])#antra pozicija nuo galo
print(my_numbers[-5:])#nuo 5 pozicijos nuo galo iki pat galo
print(my_numbers[:-5])#nuo pradzios iki 5 pozicijos nuo galo
print(my_numbers[2:-5])# nuo 2 pozicijos iki 5tos nuo galo
print(my_numbers[-6:-2])#imame nuo 6 nuo galo iki 2 nuo galo
print(my_numbers[-8:4])#teoriskai veikia, neapsikraukis =D
print(my_numbers[:])#paima viska nuo pradzios iki galo, lygiai taip pat, kaip ir neirasius nieko
print(my_numbers[::2])#visa imtis, kas antras elementas
print(my_numbers[::3])#visa imtis, kas 3cias elementas
print(my_numbers[1::2])#visa imtis nuo 1o indekso iki galo, kas antras elementas
print(my_numbers[3:7:2])#nuo 3 indekso inclusive iki 7 exclusive kas antras elementas
print(my_numbers[2:-2:2])#paimu viska be pirmu dvieju IR paskutiniu dvieju kas antra
print(my_numbers[::-1])#visi elementai, bet nuo galo.
print(my_numbers[::-2])# visa imtis, kas antras elementas BET nuo GALO

rasos_printas = my_numbers[::-2]
print(rasos_printas)


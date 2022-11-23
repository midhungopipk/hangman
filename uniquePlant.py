import random

f = open("plants.txt")
a = []
plants = {}

for p in f:
    a.append(p)

name = input("Enter your full name: ").lower()

name_array = name.split()
l = len(name_array)


def find_plant(name, i):
    for n in name:
        plants[n] = list()
        for p in a:
            if n == p[0]:
                plants[n].append(p)
            else:
                continue
        if len(plants[n]) != 0:
            break
        else:
            del plants[n]
            continue


for i in range(l):
    find_plant(name_array[i], i)


print("Your unique plants are")


for e in plants:
    print(random.choice(plants[e]), end=" ")

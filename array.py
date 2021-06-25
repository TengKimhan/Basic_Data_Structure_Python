# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190

# lst = [2200, 2350, 2600, 2130, 2190]
# print("1. ", lst[1] - lst[0])
# total = 0;
# for idx in range(0,3):
#     total =total + lst[idx]
# print("2. ", total)
# check = 2000 in lst
# print("3. ", check)
# lst.append(1980)
# print("4. ", lst)
# lst[3] = 2130 - 200
# print("5. ", lst)

# question 2
# heros = ['spider man','thor','hulk','iron man','captain america']
# print("1, ", len(heros))
# heros.append('black panther')
# print("2. ", heros)
#
# heros.remove('black panther')
# heros.insert(3, 'black panther')
# print("3. ", heros)
#
# heros[1:3] = ['doctor strage']
# print("4. ", heros)
#
# print("5. ", sorted(heros))

# question 3
max = int(input("Enter number: "))
odd = []
for item in range(1, max+1):
    if (item %2 == 0):
        continue
    else:
        odd.append(item)

print(odd)
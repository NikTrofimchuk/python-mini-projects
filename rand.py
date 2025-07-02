import random

I_COUNTER = 1000

random.seed(1)
lst = {0 : 0, 1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0, 7 : 0, 8 : 0, 9 : 0}
for i in range(I_COUNTER):
    num = random.randint(0, 9)
    lst[num] += 1

for j in range(0, 10):
    print(f'Percent of \"{j}\" : {lst[j] / I_COUNTER * 100}%')

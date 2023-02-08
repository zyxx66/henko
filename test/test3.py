max_numbers_of_human = 10
import random
total_human_number = {}
for i in range(1,max_numbers_of_human+1):
    total_human_number.update({i:0})
print(total_human_number[1])
for _ in range(1,50000):
    numbers_of_human = []
    for i in range(1, max_numbers_of_human+1):
        numbers_of_human.append(i)
    while True:
        numbers_of_human_now = numbers_of_human.__len__()
        while True:
            random_number = random.randint(1,numbers_of_human_now)
            if random_number % 2 == 1:
                del numbers_of_human[random_number-1]
                break

        if numbers_of_human_now == 2:
            total_human_number[numbers_of_human[0]] = total_human_number[numbers_of_human[0]] + 1
            break
min = 0
number = 0
for i in total_human_number:
    if total_human_number[i] >= min:
        min = total_human_number[i]
        number = i
    if i == total_human_number.__len__():
        print('%s:%s'%(str(number),str(min)))
print(total_human_number)
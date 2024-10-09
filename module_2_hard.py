import random

list = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
n = random.choice(list)
result = []

for i in range(21):
    for j in range(21):
        if i != 0 and j != 0 and i != j:
            if n % (i+j) == 0:
                result.append([i, j])
        else:
            continue

for a, b in result:
    for c, d in result:
        if a == d and b == c:
            result.remove([c, d])
        else:
            continue


print(f'Первое число: {n}')
print(f'Второе число: ', end='')
for i, j in result:
    print(i, end='')
    print(j, end='')



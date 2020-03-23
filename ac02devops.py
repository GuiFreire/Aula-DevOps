count = 0
num = 2

while (count <= 100):
    normal = False
    for i in range(2, num):
        if (num % i == 0):
            normal = True
            break

    if (not normal):
        count += 1
        print(num)

    num += 1

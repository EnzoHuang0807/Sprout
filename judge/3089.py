i , j = 1, 1
n = int(input())

while i <= 9:
    if i == n:
        i += 1
        j = 1
        continue
    while j <= 9:
        if j == n:
            j += 1
            continue
        print(f"{i}*{j}={i*j}", end =' ')
        j += 1
    print('')
    i += 1
    j = 1
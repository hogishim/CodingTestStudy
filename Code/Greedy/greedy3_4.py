n, m = map(int, input().split())

count = 0

while n !=1:
    if n == 0:
        break
    if n % m == 0:
        n = n // m
        count += 1

    elif n > m:
        count += n%m
        n = n - n%m

    else:
        count += n -1
        break
    

print(count)
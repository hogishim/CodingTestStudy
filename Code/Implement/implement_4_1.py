n = int(input());
route = input().split()

x, y= 1, 1

for val in route:
    if val == 'L' and y > 1:
        y -= 1
    elif val == 'R' and y < n:
        y += 1
    elif val == 'U' and x > 1:
        x -= 1
    elif val == 'D' and x < n:
        x += 1
    else:
        continue

print(x, y)
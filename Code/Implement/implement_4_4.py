def change_direction(d):
    d = (d + 3) % 4
    cur = direction[d]

    return cur, d



n, m = map(int, input().split())

x, y , d = map(int, input().split())


data = []
rotate = 0
count = 1
visited = [[0] * m for j in range(n)]
visited[x][y] = 1

direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
cur_dir = direction[d]

for i in range(n):
    data.append(list(map(int, input().split())))


while True:

    cur_dir, d = change_direction(d)
    cx = x + cur_dir[0]
    cy  = y + cur_dir[1]

    if data[cx][cy] == 0 and visited[cx][cy] == 0:
        x = cx
        y = cy
        visited[cx][cy] = 1
        count += 1
        rotate = 0

    elif rotate != 3:
        rotate += 1
        continue


    elif rotate == 3 and data[x-1][y] == 0:
        x -= 1
        rotate = 0
    
    elif rotate == 3 and data[x-1][y] == 1:
        break;


print(count)

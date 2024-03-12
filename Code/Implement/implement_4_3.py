coord = input()

xcoord = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
possible_x=[-2, -1, 1, 2, -2, -1, 1, 2]
possible_y=[-1, -2, -2, -1, 1, 2, 2, 1]

x = xcoord.index(coord[0])
y = int(coord[1])-1
count = 0

for i in range(8):
    new_x_coord = x + possible_x[i]
    new_y_coord = y + possible_y[i]

    if new_x_coord >= 0 and new_x_coord < 8 and new_y_coord >= 0 and new_y_coord < 8:
        count += 1

print(count)
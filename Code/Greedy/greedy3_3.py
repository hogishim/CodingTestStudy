#2중 for문 없이

n, m = map(int, input().split())

min_val = 0

for i in range(n):
  data = list(map(int, input().split()))

  cur_min = min(data)

  if min_val < cur_min:
    min_val = cur_min


print(min_val)
n = int(input())
count = 0

coin = [500, 100, 50, 10]

for i in coin:
  res = n // i
  print(i, "동전은", res)
  count = count + res
  n = n % i

print("거슬러줄 총 동전의 개수는", count)
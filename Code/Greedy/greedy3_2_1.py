#큰수의 법칙
n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
num1 = arr[n-1]
num2 = arr[n-2]

result = 0
count = 0

for i in range(m):
  if count < k:
    result = result + num1
    count += 1


  else:
    result = result + num2
    count = 0

print(result)
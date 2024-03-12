#큰수의 법칙 최적화
n, m, k = map(int, input().split())
data  = list(map(int, input().split()))

data.sort()
num1 = data[n-1]
num2 = data[n-2]

result = 0

result = result + num1 * (m // (k+1)) * k
result = result + num2 * (m // (k+1))
result = result  + num1 * (m % (k+1))

print(result)
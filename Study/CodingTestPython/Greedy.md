# Ch01.  그리디 알고리즘

### 💰Greedy algorithm: 현재 상황에서 당장 좋은 것을 고르는 방법

- 매 순간 가장 좋아보이는 것을 고르고, 현재의 선택이 나중에 미치는 영향에 대해서는 고려하지 않는다
- Dijkstra algorithm과 같은 경우를 제외하면, greedy algorithm은 단순 암기를 통해 대처하는 알고리즘이 아니고, 많은 유형을 접해보면서 대비해놓고 있어야 한다

### 그리디 알고리즘의 정당성

- 대부분의 문제는 그리디 방식으로 접근했을때 최적의 해를 찾지 못할 가능성이 높다
- 거스름돈 문제에서 500원, 100원, 50원, 10원의 경우에는 큰 단위가 작은 단위의 배수이기 때문에 작은 단위의 동전을 조합하여 다른해가 나올 수 없기 때문인데, 당장 800원을 거슬러 준다고 했을때, 동전이 500, 400, 100원 있는 경우에는 greedy로 풀면 500 100 100 100 4개가 필요한데 400원 2개로도 거슬러줄 수 있다
- 즉, 문제를 처음 보고 그리디 알고리즘으로 풀 수 있을지 생각해보고, 그리디가 최적의 해를 구할 수 없다고 생각이 들면, dynamic이나 graph 알고리즘으로 풀 수 있을지 고민해본다

### 예제 1) 거스름돈: 거스름돈으로 사용할 500, 100, 50, 10원 동전이 있다고 가정할때, 거슬러 줘야할 동전의 개수는?

- 500원을 먼저 거슬러주고, 그 다음에 100원, 그다음에 50원… 이렇게 가장 큰 화폐 단위부터 차례로 거슬러 준다
- 1260원을 거슬러 준다고 했을때 500원 최대 2개니까 1260원에서 1000원을 빼서 260원이 남고, 100원이 최대 두개니까 200원 해서 60원 남고…이런식으로 10원까지 계산해준다

My solution

```python
n = int(input())
count = 0

coin = [500, 100, 50, 10]

for i in coin:
  res = n // i
  print(i, "동전은", res)
  count = count + res
  n = n % i

print("거슬러줄 총 동전의 개수는", count)
```

![Untitled](Greedy/Untitled.png)

- 배열에 동전 종류를 저장해놓고 큰 동전부터 차례로 거스름돈 총액에서 빼나간다

book’s solution

```python
n = 1260
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
	count +=n n //coin
	n %= coin

print(count)
```

- 거스름돈 총액은 수행 시간에 영향을 주지 않고, 동전의 개수 K만 프로그램의 수행 시간에 영향을 준다
- 화폐의 개수 K만큼 시간이 필요하기 때문에 시간 복잡도는 O(K)이다

### 예제 2) 큰 수의 법칙: n개의 수중, 주어진 수를 M번 더할때, 최댓값 구한다. 단, 같은수는 최대 K번 더할 수 있다

<aside>
💻 첫줄에 N(2 ≤ N ≤ 1000), M(1 ≤ M ≤ 10000), K(1 ≤ K ≤ 10000)가 주어진다. 각 자연수는 공백으로 구분한다. K는 항상 M보다 작거나 같다
둘째줄에 N개의 자연수가 주어진다. 자연수는 공백으로 구분하고 각 자연수는 1이상 10000이하의 정수로 주어진다

</aside>

- 가장 큰수를 찾아 K번까지 더하고, K+1번째는 두번째로 큰수를 한번 더하고, 이후에 다시 가장 큰수를 K번 더하고.. 이 과정을 반복한다

My solution

```python
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
```

![Untitled](Greedy/Untitled%201.png)

- K번 더해질때까지 가장 큰수를 반복하여 더하다가 K번 더한 이후에는 두번째 큰 수를 한번 더하고 이후에 다시 K번 더하기 전까지 가장 큰 수 더하기

최적화

My solution

```python
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
```

Book’s solution

```python
# N, M, K를 공백을 기준으로 구분하여 입력 받기
n, m, k = map(int, input().split())
# N개의 수를 공백을 기준으로 구분하여 입력 받기
data = list(map(int, input().split()))

data.sort() # 입력 받은 수들 정렬하기
first = data[n - 1] # 가장 큰 수
second = data[n - 2] # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first # 가장 큰 수 더하기
result += (m - count) * second # 두 번째로 큰 수 더하기

print(result) # 최종 답안 출력
```

- 이 문제는 M이 10,000 이하이기 때문에 문제가 해결 가능하지만, M의 크기가 100억 이상으로 커지면 시간 초과 판정을 받을 것이다
- 결국 M번 더할때, (6 + 6 + 6 + 5) + (6 + 6 + 6 + 5) … 이런식으로 수열처럼 (6+6+6+5)가 반복이 되기 때문에 반복되는 횟수만 계산해주면 for문을 안돌리고, 총 개수를 구해서 곱해주기만 하면 된다
- 반복되는 (6+6+6+5)의 개수는 K+1개이다. 그리고 나누어 떨어지지 않는 6이 있을 수 있는데, 그것은 나머지 만큼 반복될 것이다
- 따라서 M / (K+1)의 몫에서 6의 개수는 K개 만큼, 5의 개수는 1개, 그리고 나머지 만큼 6이 추가로있기 때문에 계산하면 가장 큰수 * (M // (K+1)) * K + 가장 큰수 * M % (K+1) + 두번째로 큰 수 * (M // (K+1))가 최종 결과가 된다

### 예제3) 숫자 카드 게임: 최솟값에서 최댓값을 구하자

- 카드가 N * M 형태로 놓여있다고 할때, 행을 먼저 선택하고, 해당 행에서 가장 작은 값을 뽑는다
- 다른 행으로 넘어가서 가장 작은 값을 뽑고, 이전에 뽑은 수와 비교하여 더 큰 수를 선택한다
- 이 과정을 모든 행에 대해서 반복한다

<aside>
💻 첫줄에 카드가 놓인 행의 개수 N과 열의 개수 M이 공백을 기준으로 하여 각각 자연수로 주어진다
둘째줄부터 N개 줄에 걸쳐 각 카드에 적힌 숫자가 주어진다. 숫자는 1 이상, 10000 이하의 자연수다

</aside>

My solution

```python
n, m = map(int, input().split())

min_val = 0

for i in range(n):
  data = list(map(int, input().split()))

  cur_min = min(data)

  if min_val < cur_min:
    min_val = cur_min

print(min_val)
```

![Untitled](Greedy/Untitled%202.png)

- 각 행마다 가장 작은 수를 뽑아주고, 해당 숫자가 다른 행에서 뽑힌 다른 수보다 더 작은지 확인하고, 만약 다른 행에서 뽑힌 수보다 크다면 해당 수를 현재까지의 최대 숫자로 설정한다

Book’s solution

```python
# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())

result = 0
# 한 줄씩 입력 받아 확인하기
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = min(data)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result) # 최종 답안 출력
```

### 예제4) 1이 될때까지. N과 K가 주어질때, N이 1이 될때까지 연산을 몇번 해야 할까

- N을 K로 나누거나 N에서 1을 빼는것을 한번의 과정이다
- N이 K로 완전히 나누어 떨어지는 경우에만 나눌 수 있다

<aside>
💻 첫줄에 N(2 ≤ N ≤ 100000)와 K(2 ≤ K ≤ 100000)가 공백으로 구분되며 자연수로 주어진다. N은 항상 K보다 크거나 같다
첫 줄에 N이 1이 될 때까지 1번 혹은 2번의 과정 수행해야하는 횟수의 총합 구한다

</aside>

My solution

```python
n, k = map(int, input().split())

count = 0

while n !=1:
    if n % k == 0:
        n = n // k
        count += 1

    elif n > k:
        count += n%k
        n = n - n%k

    else:
        count += n -1
        break
    

print(count)
```

![Untitled](Greedy/Untitled%203.png)

- N이 1이 아닐때까지 반복해서 수행한다
- N이 K로 나누어 떨어지면 나누고, 실행 횟수를 count + 1 해준다
- 나누어 떨어지지 않는데, N > K인 경우에는 나누어 떨어질때까지 1씩 빼주는데, 한번에 나머지 만큼 뺴주면 바로 나누어 떨어진다. 실행 횟수는 1 빼는 것을 나머지 만큼 실행하는 것이기 때문에 실행 횟수는 나머지 만큼 늘어난다
- N < K이면, 더이상 나눠주지 않고 N이 1일때까지 반복하여 빼줘야 한다. 따라서 N이 1이 될때까지 반복적으로 빼줄 것이기 때문에 실행 횟수를 n-1만큼 실행한다
- 이 각각의 프로세스들이 모두 진행된 횟수의 총합을 구하면 구하고자 하는 값이 나온다

Book’s solution 1

```python
# N, K을 공백을 기준으로 구분하여 입력 받기
n, k = map(int, input().split())
result = 0

// N이 K 이상이라면 K로 계속 나누기
while n >= k:
    # N이 K로 나누어 떨어지지 않는다면 N에서 1씩 빼기
    while n % k != 0:
        n -= 1
        result += 1
    # K로 나누기
    n //= k
    result += 1

# 마지막으로 남은 수에 대하여 1씩 빼기
while n > 1:
    n -= 1
    result += 1

print(result)
```

- N이 K로 나눠질때까지 반복해서 1을 빼고, N이 K보다 작아지면 N이 1이 될때까지 1을 빼준다
- 1을 반복하여 빼는 것을 생략하여 일일이 1을 빼지 않고 한번에 빼도록 할수도 있다

Book’s solution 2 - 최적화

```python
# N, K공백을 기준으로 구분하여 입력 받기
n, k = map(int, input().split())

result = 0

while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지만 1씩 빼기
    target = (n // k) * k
    result += (n - target)
    n = target
    # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)
```

- N이 K로 나누어 떨어지는 수가 될 때까지 반복적으로 빼준다
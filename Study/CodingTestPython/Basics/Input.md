# Input 처리하기

### 💫입력

### input(): 데이터를 입력 받을때는 input()을 사용

```python
n = int(input())
a = input()

data = list(map(int, input().split()))
n, m, k = map(int, input().split()))
```

- 첫번째는 그냥 숫자 하나를 input으로 받는 것이다. 엔터로 입력이 완료된다
- 두번째는 문자열을 input으로 받는 것이다. 엔터를 누르면 입력이 완료된다
- 세번째는 array를 입력으로 받는 것으로, 1 2 3과 같이 스페이스바를 기준으로 하나씩 array의 원소로 넣어주게 된다
- 네번째는 n, m, k에 차례로 숫자 데이터를 넣는 것이다. 마찬가지로 공백을 기준으로 구분한다
- 그러나 input개수가 너무 많으면, input만으로도 런타임 초과가 발생할 수 있다

### readline(): 런타임 초과를 방지하기 위한 것

```python
import sys

data = sys.stdin.readline().rstrip()
data2 = list(map(int, sys.stdin.readline().split()))
```

- python 내제 library에 있는 readline을 이용하면 runtime을 단축할 수 있다
- readline으로 입력을 받은 이후에 rstrip을 넣어주는 것이 좋다. 이는 엔터값이 들어가는 것을 방지해준다
- 2 3 4과 같은 숫자 배열을 받아주기 위해서는 input과 동일하게 진행되다가 input 대신 readline만 써주면 된다

### 배열 입력 받기

```python
#tuple
input_data = input("Enter values separated by spaces: ")
tuple_data = tuple(input_data.split())

#list
input_data = input("Enter values separated by spaces: ")
list_data = input_data.split()

#set
input_data = input("Enter values separated by spaces: ")
set_data = set(input_data.split())
```

- 각 자료형에 대한 입력 방식이다. 모두 2 3 4과 같은 형식으로 입력 받게 된다
- 여러개를 저장하고 싶다면 먼저 데이터의 개수를 입력 받은 이후에, 원하는 개수 만큼 for문을 돌려서 반복적으로 받을 수 있다
- 1 2 3 (엔터) 2 3 4 이런 식으로 입력하면 {(1,2,3), (2,3,4) … } 이런 식으로 입력 받을 수 있다
- 아니면 list로 쭉 받아서 예를 들어 {(1,2,3), (2,3,4) … }이렇게 이용하고 싶으면 [0], [3], [6] 이런 식으로 index를 이용하여 각 원소를 구분 지을 수 있다

### 💫출력

```python
print(a)

print("a" + string(b) + "hello!")
print("a", b, "hello")

print(f"hello mr {answer} my yesterday")
```

- +로 문자열 더하기 연산을 수행하기 위해서는 string()으로 형변환 과정이 필요하다
- 혹은 , 로 문자열 더하기 연산을 수행할 수 있다
- f-string 문법을 사용할 수 있는데, 이는 중괄호 안에 변수를 넣어서 자료형 변환 없이 출력을 해줄 수 있다
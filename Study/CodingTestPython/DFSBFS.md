# Ch03. DFS/BFS

### 🗄️Stack/queue: DFS/BFS를 구현하기 위해 필요한 자료구조

- overflow: 데이터가 이미 가득찬 상태에서 삽입 연산을 수행할때 발생
- underflow: 데이터가 전혀 들어있지 않는 상태에서 삭제 연산을 수행할때 발생

### Stack: First In Last Out. 먼저 들어온 데이터가 나중에 삭제된다

```python
stack = []

stack.append(2)
stack.append(3)
stack.append(4)
print(stack)

stack.pop()
stack.append(3)

print(stack)
```

- 파이썬에서 stack은 별도의 라이브러리가 필요 없다. 기본 리스트에서 append를 하면 리스트 가장 뒤에 값이 추가되고, pop을 하면 리스트 가장 뒤의 값이 삭제된다
- 2, 3, 4를 append한 이후에 출력하면, [2,3,4]로 출력된다
- pop을 하면 가장 마지막에 들어온 4기 삭제되고, 다시 3이 들어오면 [2,3,3]이 출력된다

### Queue: First In First Out. 먼저 들어온 데이터가 가장 먼저 삭제된다

```python
from collections import queue

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
```

- 파이선에서 queue를 구현하는 경우에는 collections 모듈에서 deque자료를 활용한다
- 데이터를 넣고 빼는 속도가 리스트 자료형에 비해 효율적이며, queue 라이브러리보다 더 간단하다

### 재귀함수: 자기 자신을 다시 호출하는 함수

- 재귀 함수는 자기 자신을 계속 호출하는 함수인데, 재귀 함수의 최대 깊이가 존재하는데, 호출 횟수 제한 한계가 존재하는 것이다
- 제한이 존재하기 때문에 재귀함수에서는 반드시 종료 조건을 명시해야 한다
- 컴퓨터는 재귀함수의 수행을 스택자료형을 사용하기 때문에, stack 자료구조를 활용하는 경우에는 재귀함수를 이용하여 간단하게 구현할 수 있다# Ch03. DFS/BFS
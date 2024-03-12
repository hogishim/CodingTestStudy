# 반복문

### 💫반복문: 조건을 만족하지 않는 경우까지 반복적으로 실행

### While문: 조건문이 참인 경우에 한해서 반복적으로 코드가 수행

```python
while i > 0:
	print("hi")
```

### For문: 데이터의 포함되어있는 원소를 시작 index부터 끝 index까지 반복하여 실행

```python
for i in range(1,5):
	if i > 3:
		continue;
```

- 첫 원소로는 시작 index가, 끝 원소로는 끝 index가 들어가게 된다
- continue는 해당 index에서 아무것도 하지 않고, 다음 index로 바로 넘어가게 된다
- 중첩하여 사용하는 것이 가능하다
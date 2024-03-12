# 함수

### 💫함수: 반복적인 작업 할때 따로 분리하여 이용할 수 있다

### 함수

```python
def add(a, b):
	print(a + b)
	
	return a + b;
```

- 다음과 같이 함수에서 처리할 내용을 처리한 이후에 return으로 결과값을 반환할 수 있다

```python
a = 0

def func():
	global a
	a ++
```

- global 키워드로 변수를 지정하면 지역 변수 만들지 않고도 바로 바깥에 선언된 변수를 참조할 수 있다

### 람다 표현식

```python
print((lamda a,b : a + b)(3, 7))
```

- 함수의 내용을 간단하게 표현하여 작성할 수 있다
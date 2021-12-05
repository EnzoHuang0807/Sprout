---

slideOptions:        # 簡報相關的設定
  theme: moon   # 顏色主題
  transition: 'fade' # 換頁動畫
  # parallaxBackgroundImage: 'https://s3.amazonaws.com/hakim-static/reveal-js/reveal-parallax-1.jpg'
---

# Dictionary

---

## introduction to dictionary

----

### 已知用 list... 然後呢 ?

### dict 可以強化兩筆資料之間的對應關係
### 有函式可以做相關操作

```python =
L = [[2,1],[4,3]]

dict([[2,1],[4,3]])
#{2: 1, 4: 3}
```

----


```python =
D = dict()
D = {}

A = {"one": 1, "two": 2, "three" : 3}
print(A)
# {'one': 1, 'two': 2, 'three': 3}

B = dict({"one": 1, "two": 2, "three" : 3})
print(B)
# {'one': 1, 'two': 2, 'three': 3}

C = dict({"one": [1, 1, 1], "two": 2, "three" : 3})
print(C)
# {'one': [1, 1, 1], 'two': 2, 'three': 3}

dict([[2,1],[4,3]])
#{2: 1, 4: 3}
```

----

## Q: dict 的 key 和 value 可以是哪些型別(type) ? 

----

### A:  value 可以是任意型別，但 key 只能是 immutable data type (string, number, tuple)

----

## dict operations

----


### 1. 讀取、改變 key 對應的 value
```python=
D = {"one": 1, "two": 2, "three" : 3}

x = D["one"]
print(x)
# 1

D["two"] = 2.0
print(D)
#{'one': 1, 'two': 2.0, 'three': 3}
```

----

### 2. 刪除 key
```python=
D = {"one": 1, "two": 2, "three" : 3}

del D["three"]
print(D)
#{'one': 1, 'two': 2.0}

D.pop("one")
print(D)
#{'two': 2, 'three': 3}
```

----

### 3. 取得 dict 長度
### 4. 檢查 dict 內是否有某個 key
```python = 
D = {"one": 1, "two": 2, "three" : 3}
print(len(D))
#3

print("one" in D)
print(1 in D)
#True
#False
```

----

### 5. 複製一個dict
```python=
D1 = {"one": 1, "two": 2, "three" : 3}
D2 = D1.copy()
print(D2)
#{'one': 1, 'two': 2, 'three': 3}

print(D1 == D2)
#True
```

----

### 6. 融合!!

```python=
D1 = {"one": 1, "two": 2, "three" : 3}
D2 = {"one": 1.0, "two": 2, "four" : 4}
D1.update(D2)
D1
# {'one': 1.0, 'two': 2, 'three': 3, 'four': 4}
```

---

## dict 的迭代

----

### 1. 迭代 dict 的 keys

``` python = 
D = {"one": 1, "two": 2, "three" : 3}
for key in D:
    print(f"key {key} has value {D[key]}")
'''
key one has value 1
key two has value 2
key three has value 3
'''
```

----

### 2. 迭代 dict 的 values
```python = 
D1 = D.values()  # D.keys
for i in D1:
    print(i)
'''
1
2
3
'''
print(type(D1))
#<class 'dict_values'>

L = list(D1)
print(type(L))
#<class 'list'>
```

----

### 3. 小孩子才做選擇，我兩個都要迭代

```python =

D1 = D.items()  
for i, j in D1:
    print(f"{i} : {j}")  
'''
one : 1
two : 2
three : 3
'''
print(type(D1))
#<class 'dict_items'>
```

---

## dict 的 sort

----

## Scenario : are u from 南寧 ?

{%youtube MbfxhbgvFxE %}

----


### sorted(dict)

```python=
D1 = {"monkey": 1, "zoo": 2, "kangaroo" : 3, "crocodile" : 4}

D2 = sorted(D1)
print(D2)
#['crocodile', 'kangaroo', 'monkey', 'zoo']
print(type(D2))
#<class 'list'>

```

----

### 利用 sorted 產生另一個 dict

```python = 
D1 = {"monkey": 1, "zoo": 2, "kangaroo" : 3, "crocodile" : 4}
    
D2 = dict(sorted(D1.items()))
print(D2)
#{'crocodile': 4, 'kangaroo': 3, 'monkey': 1, 'zoo': 2}

D2 = dict(sorted(D1.items(), reverse = True))
print(D2)
#{'zoo': 2, 'monkey': 1, 'kangaroo': 3, 'crocodile': 4}

D2 = dict(sorted(D1.items(), key = lambda item: item[1]))
print(D2)
#{4: 'crocodile', 3: 'kangaroo', 1: 'monkey', 2: 'zoo'}

```

---

## Thank you :+1: 




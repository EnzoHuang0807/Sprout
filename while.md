---

slideOptions:        
  theme: solarized 
  transition: 'sky' 
  
---

# While

###### 資訊之芽py班 2022
###### 黃千睿

---

## Intro

----

在英文中，while 是什麼意思呢?

ex: <font color="blue">While Putin is invading Ukraine, </font> <font color="green">Biden is praying.</font>

分析: <font color="blue">當(while) 某個敘述成立時， </font> <font color="green">某個動作正在發生</font>

----

在python(或其他的程式語言)中，
while也有同樣的意思
這樣的語法可以讓你的程式使用loop(迴圈)做更多事情

----


## Loop (迴圈)

當你有<font color="#f00">重複</font>或<font color="red">類似</font>的指令需要執行時，
迴圈的概念可以幫你有系統的撰寫程式

while是迴圈的一種，之後還會介紹for迴圈

----

有了loop之後，我們可以...

#### print 1000次 Hello,world 

```python=
print("Hello, world.")
print("Hello, world.")
print("Hello, world.")
print("Hello, world.")
print("Hello, world.")
...
...
```

```python=
i = 1
while i <= 1000:
    print("Hello, world.")
    i += 1
```

原本要 Ctrl+C Ctrl+V
現在只要用while迴圈寫就可以了

但 是   ~~(速度ㄩ)~~

----

要是沒控制好，可能會產生無限迴圈
此時，按⏹️終止你的程式
![](https://i.imgur.com/UKSrvUU.png)
![](https://ahseeit.com//king-include/uploads/2021/01/135621505_3490110337777630_2014426057131565060_n-5779826117.jpg =500x500)

----

### 由片語學習python語法:

```python=
while condition :
    your code here
    remember to do something that can end the loop
```
#### 要記得縮排哦

----

### Discussion

```python=
while condition :
    your code here
    remember to do something that can end the loop
```

```python=
i = 1
while i <= 1000:
    print("Hello, world.")
    i += 1
```

上面程式的 condition 是什麼 ?
為什麼不會產生無限迴圈 ?

----

可以當作`if`的condition就可以當作`while`的condition
除了用`i<=1000`之外，也可以用boolean variable或是boolean constant

```python=
flag = True
while flag:
    ....
```

```python=
while True:
    ....
```

---

## Examples

----

### 1. 找因數

```python=
num = int(input())
x = 1              
while num >= x:
    if num % x == 0:
        print(x)
    x += 1
```

----

### 2. Discussion 

```python=
num = int(input())
x = 1              
while num >= x:
    if num % x == 0:
        print(x)
    x += 1
```

```python=
num = int(input())
x = 1              
while num > x:
    if num % x == 0:
        print(x)
    x += 1
```
跟前面的程式碼差在哪？
可以找到所有的因數嗎？

----

### 2.5 while loop 呼吸

[一之型 印三角形](https://neoj.sprout.tw/problem/3020/)

----

### 3. nested while loop
![](https://javatutoring.com/wp-content/uploads/2016/12/loops-in-java.jpg)

----

### 九九乘法表
```python=
i, j = 1, 1
while i <= 9:
    while j <= 9:
        print(f"{i} * {j} = {i*j}", end ='\t')
        j += 1
    print('\n')
    i += 1
    j = 1
```
#### 要點:
內層迴圈執行完畢後，
再執行外層迴圈，持續到外層迴圈停止

[python 字串格式化](https://blog.louie.lu/2017/08/08/outdate-python-string-format-and-fstring/)

----

### 4. while-else

```python=
i = 0
while i < 6:
    print(i)
    i += 2
else:
    print("finished")
```

#### 要點
* 當執行到while的condition且結果為false時，執行else
* 類似if-else的關係

---

## break & continue

----

### 猜數字 + break

```python=
key = 87

while True:   
    x = int(input())
    if x > key:
        print("Too large")
    elif x < key:
        print("Too small")
    else:
        print(f"Correct! the key is {key}")
        break;
```

#### 要點
* 用一個永遠為真的condition "True" 讓迴圈反覆執行
* 猜對了再用break強制離開迴圈

----

### while-else + break
```python=
key = 87
while True:   
    x = int(input())
    if x > key:
        print("Too large")
    elif x < key:
        print("Too small")
    else:
        print(f"Correct! the key is {key}")
        break;
else:
    print("finished")       
```

#### 要點
*  使用break強行中斷迴圈就不會執行else

----

### continue

```python=
count = 0
letMeWatch = False

while letMeWatch is False:
    if count < 3:
        count += 1
        print("No!!!")
        continue
    else:
        print("take of glasses")
        print("punch!")
        letMeWatch = True
```

#### 要點
*  使用 continue 強行回到迴圈的判斷式 

----

### 小挑戰
程式會怎麼跑呢

```python=
sc = 1000
while sc > 0:
    while sc >= 50:
        sc /= 2
        if sc > 100:
            continue
        print(f"only {sc} social credits left!")
    break
print(sc)
```

----

使用break或continue只會影響正在執行中的迴圈
如果break內層迴圈，外層迴圈依然會執行

----

### 欲練神功，必先..
[卍九九乘法表乂](https://neoj.sprout.tw/problem/3089/)

---

## Recap

* 知道while迴圈的架構
* 了解判斷條件可以是什麼
* **記得終結迴圈的方式要存在**
* 學會使用break跟continue
* 開始覺得自己不會寫程式

----

![](https://i.pinimg.com/originals/f5/d3/d2/f5d3d20efd7519d9e01fc88b0c7fc7b0.jpg)

---

## 作業(?)

---

## Thank you :+1: 




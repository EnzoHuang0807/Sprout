def calculate(x, y):
    return x * y 

n = int(input())
ans , index = -1, -1
for i in range(n):
    x, y = map(int, input().split())
    if ans == -1 or calculate(x, y) < ans:
        ans = calculate(x, y)
        index = i 

print(index, end="")

n, M  = map(int,input().split())
city = [[(0, 0) for i in range(M)] for j in  range(M)]
        
def construct(name, x, y, dx, dy, h):
    for i in range(x, x + dx):
        for j in range(y, y + dy):
            if (city[i][j] != (0, 0)):
                print("ILLEGAL CONSTRUCTION PLAN!")
                exit(0)
            city[i][j] = (name, h)

    return 0

for i in range(n):
    l = input().split()
    name = l[0]
    x, y, dx, dy, h = map(int, l[1:])
    construct(name, x, y, dx, dy, h)

def format(d):
    ans = sorted(d.items(), key=lambda x:(-x[1], x[0]))
    print(",".join([f"{i}:{j}" for i, j in ans]))

dict_x = dict()
# x axis    
for i in range(M):
    height = 0
    for j in range(M):
        name = city[i][j][0]
        cur_h = city[i][j][1]

        if cur_h > height:
            if (name not in dict_x):
                dict_x[name] = 0
            dict_x[name] += cur_h - height
            height = cur_h

format(dict_x)

dict_y = dict()
# y axis    
for j in range(M):
    height = 0
    for i in range(M):
        name = city[i][j][0]
        cur_h = city[i][j][1]

        if cur_h > height:
            if (name not in dict_y):
                dict_y[name] = 0
            dict_y[name] += cur_h - height
            height = cur_h
            
format(dict_y)
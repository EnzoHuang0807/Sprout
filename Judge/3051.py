def func(l):
    data = l[:-1]
    data_type = l[-1]

    if data_type == "num":
        print(sum(list(map(int, data))))
    else:
        print("".join(data))

l = input().split()
func(l)

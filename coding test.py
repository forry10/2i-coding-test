start=0
for i, mul in enumerate([7, 8, 9]):
    finish = 100 + (100*i)
    for i in range(start+mul, finish, mul):
        print(i)
    start = i

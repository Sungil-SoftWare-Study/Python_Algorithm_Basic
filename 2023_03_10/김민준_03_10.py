# 구구단
for i in range(1, 10):
    for j in range(1, 10):
            print('%d * %d = %2d' %(i, j, i*j))
    print('----------')

# 진화버전 
for i in range(1, 10):
    for j in range(1, 10):
            print('%d x %d = %2d' %(j, i, i*j), end = '     ')
    print()

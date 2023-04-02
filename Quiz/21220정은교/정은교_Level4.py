n = int(input())

for i in range(n):
    cnt = 0
    sum = 0
    
    test_case = input()
    
    for j in test_case:
        if j == 'O':
            cnt += 1
            sum += cnt
        else:
            cnt = 0
    print(sum)

n = int(input())

for i in range(n):
    cnt = 0
    sum = 0

    t = input()

    for j in t:
        if j == 'O':
           cnt += 1
           sum += cnt
        else:
            cnt = 0
    print(sum)

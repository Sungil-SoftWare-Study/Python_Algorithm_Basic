num = int(input())
result = n
cnt = 0

while True:
    str1 = result // 10
    str2 = result % 10
    
    sum = (str1 + str2) % 10
    result = (str2 * 10) + sum
    cnt += 1
    
    if(result == num):
        break

print(cnt)

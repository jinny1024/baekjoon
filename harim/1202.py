#greedy algorithm

#10162번 전자레인지
'''
t = int(input())

a = 5 * 60
b = 60
c = 10

cnt_a = t // a
t -= a * cnt_a

cnt_b = t // b
t -= b * cnt_b

cnt_c = t // c
t -= c * cnt_c

if t != 0:
    print("-1")

else :
    print(cnt_a, cnt_b, cnt_c)
'''

#10610번 30
'''
n = input()

#0이 없으면 10의 배수가 아님 -> 30의 배수도 아님
if n.find('0')< 0:
    print("-1")

else:
    a = list(n)
    #3의 배수는 각 자릿수의 합이 3의 배수여야함
    sum = 0
    for i in range(len(a)):
        sum += int(a[i])
    if sum % 3 != 0 :
        print("-1")

    #30의 배수 중 가장 큰 수 찾기 위해 큰 수부터 정렬, 0은 제일 작으므로 맨 뒤로 감 
    else:
        for i in range(len(a)):
            a[i] = int(a[i])
        a.sort(reverse=True)

        for i in range(len(a)):
            print(a[i], end='')
        
'''

#1789번 수들의 합
'''
s = int(input())
cnt = 0
sum = 0

for i in range(1,s):
    if sum == s:
        break
    elif sum > s :
        cnt-=1
        break
    sum += i
    cnt += 1

print(cnt)
'''

#1946번 신입사원
#sys 사용하여 시간초과 문제 해결
import sys

t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    data = [[0,0]for m in range(n)]
    for j in range(n):
        data[j][0], data[j][1] = map(int,sys.stdin.readline().split())

    #0번 인덱스로 정렬
    data.sort()
    min1 = data[0][1]
    
    #1번 인덱스로 정렬
    data.sort(key = lambda x : x[1])
    min2 = data[0][0]

    new = []
    if data[0][0] == 1 and data[0][1] == 1:
        cnt = 1
        new.append(0)
    else:
        cnt = 2
        new.append(0)
    for k in range(len(data)):
        if cnt == 1:
            break
        if data[k][0] == 1 :
            new.append(k)
            continue
        #1순위를 포함한 데이터의 다른 순위보다 둘다 작다면 count
        if data[k][0] < min1 and data[k][1] < min2:
            new.append(k)
            cnt += 1

    for l in range(len(new)):
        
    
    print(cnt)

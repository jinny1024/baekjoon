#7568번 덩치
'''
def count(list,n,i):
    cnt=0
    for j in range(n):
        if list[j][0] > list[i][0] and list[j][1] > list[i][1]:
            cnt += 1

    return cnt

n = int(input())
p=[]
for i in range(n):
    x,y = map(int,input().split())
    p.append((x,y))

for i in range(n):
    print(count(p,n,i)+1,end=' ')


'''
#1966번 프린터 큐
'''

t = int(input())

for i in range(t):
    n,m = map(int,input().split())
    doc = list(map(int,input().split()))

    flag = m #인쇄할 문서 위치
    val = doc[m] #인쇄할 문서의 중요도 값
    cnt = 0

    while len(doc) > 0:
        if flag == 0:
            if max(doc) == doc[flag]:
                cnt += 1
                break
            else:
                doc.pop(0)
                doc.append(val)
                flag = len(doc)-1
        else:
            if max(doc) == doc[0]:
                cnt += 1
                doc.pop(0)
                flag -=  1
            else:
                tmp = doc[0]
                doc.pop(0)
                doc.append(tmp)
                flag -=  1
    print(cnt)

'''

#2108번 통계학
#틀림 -> 최빈값만
'''    
def avr(list,n):
    sum = 0
    for i in range(n):
        sum += list[i]

    return sum/n

def mid(list,n):
    return list[n//2]

#해결못함
def freq(list,n):
    f = [0] * 504000
    max = 0
    s = []
    
    for i in range(n):
        f[list[i]] += 1

    for i in range(504000):
        if f[i] > 0 :
            print(i)
    print(type(f))
    print(type(f[0]))
    max(f)
    
    prev = 0
    cnt = 0
    for i in range(-4000,50000):
        if cnt == 0 and max == f[i]:
            prev = max
            cnt += 1
            continue
        if cnt != 0 and max == f[i] and prev != list[i]:
            return list[i]

##산술평균
print(int(round(avr(list,n),0)))

##중앙값
print(mid(list,n))

##최빈값
print(freq(list,n))

##범위
print(list[n-1] - list[0])

'''

#1476번 날짜 계산 - 실버5
#틀림 -> 브루트포스로 해결가능

e,s,m = map(int,input().split())

flag = 0
if s == m:
    print(s)
    flag = 1

if flag == 0:
    n = 15 + e
    flag1 = 0
    flag2 = 0
    while True:
        if (n - s) % 28 == 0:
            flag1 = 1
        if (n - m) % 19 == 0:
            flag2 = 1

        if flag1 == 1 and flag2 == 1:
            break

        flag1 = 0
        flag2 = 0
        n += 15
        
    print(n)










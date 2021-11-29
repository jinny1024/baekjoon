#1026번 보물

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
sum = 0

##a에서 가장 작은 값과 b에서 가장 큰 값을 곱함
for i in range(n):
    sum += a[i] * max(b)
    b.remove(max(b))

print(sum)


#1541번 잃어버린 괄호

exp = input()
num = []

a = []
b= []
a.append(exp[0])
i = 1

#숫자는 a에 한자리씩 가져와서 num에, 연산은 b에 저장
while i < len(exp):
    if exp[i] == '+' or exp[i] == '-':
        num.append(a)
        a=[]
        b.append(exp[i])
        i += 1
    else :
        a.append(exp[i])
        i += 1
num.append(a)

r_num = []
for i in range(len(num)):
    r_num.append(int(''.join(num[i])))

sum = r_num[0]

i = 0
while i < len(b):
    # +연산일 때
    if b[i] == '+':
        sum += r_num[i+1]

    # -연산일 때
    elif b[i] == '-':
        if i+1 >= len(b):
            sum -= r_num[i+1]

        elif b[i+1] == '-':
            sum -= r_num[i+1]

        # - 연산 다음 + 연산의 경우 괄호
        elif b[i+1] =='+':
            sum1 = 0
            i += 1
            while i < len(b) and b[i] == '+' :
                sum1 += r_num[i]
                i += 1
            sum1 += r_num[i]
            sum -= sum1
            continue

    i += 1

print(sum)


#5585번 거스름돈

n = int(input())

rest = 1000 - n

##500엔 개수
five_h = rest // 500
rest -= 500 * five_h

##100엔 개수
one_h = rest // 100
rest -= 100 * one_h

##50엔 개수
fifty = rest // 50
rest -= 50 * fifty

##10엔 개수
ten = rest // 10
rest -= 10 * ten

##5엔 개수
five = rest // 5
rest -= 5 * five

##1엔 개수
one = rest

print(five_h+one_h+fifty+ten+five+one)


#2217번 로프

n = int(input())
rope=[]
for i in range(n):
    rope.append(int(input()))

rope.sort(reverse = True)

##가장 큰 수를 초기값으로 설정
ans = rope[0]

##현재까지 가장 큰 값과 그다음으로 큰 값을 들 수 있는 로프만큼 더한 값과 비교
for i in range(1,len(rope)):
    if ans < rope[i]*(i+1):
        ans = rope[i] * (i+1)

print(ans)

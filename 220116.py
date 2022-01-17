#1339번 단어 수학 - 골드4 => 틀림

'''
def max_len(list, n):
    max = 0
    for i in range(n):
        if len(word[i]) > len(word[max]):
            max = i
    return max

def unique(list):
    return len(list) - len(set(list))

        

n = int(input())
word = []
for i in range(n):
    word.append(input())

word= sorted(word, key = lambda x:(len(x),unique(x)))
word.reverse()

alphabet = [-1]*26
num=9

number=[[] for i in range(n)]

#문자열의 길이를 비교하여 가장 긴 문자열의 첫번째 문자에 숫자 할당, 첫번째 문자를 제거
while len(word[n-1]) > 0:
    max_idx = max_len(word,n)
    
    if alphabet[ord(word[max_idx][0])-65] < 0 :
        alphabet[ord(word[max_idx][0])-65] = num
        num -= 1
        number[max_idx].append(str(alphabet[ord(word[max_idx][0])-65]))

    else:
        number[max_idx].append(str(alphabet[ord(word[max_idx][0])-65]))
    word[max_idx] = word[max_idx][1:]           
                          

#문자열을 int형으로 바꾸면서 합을 구함
sum = 0
for i in range(n):
    a = "".join(number[i])
    sum += int(a)
    
print(sum)
'''

#1715번 카드 정렬하기 - 골드4
#틀림
n = int(input())
list=[0]*n
for i in range(n):
    list[i] = int(input())

list.sort()

def sum1(list):
    sum = list[0]
    ans = 0
    for i in range(1,n):
        sum = sum + list[i]
        ans += sum
    return ans

def sum2(list):
    if len(list) <= 1:
        return list[0]
    else:
        sum = 0
        ans=[]
        j=0
        for i in range(0,n,2):
            sum = list[i] + list[i+1]
            ans[j]=sum
            j+= 1
        sum2(ans)

print(sum2(list))
    
    

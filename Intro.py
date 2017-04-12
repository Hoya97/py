#만약 4가 [1,2,3,4] 중에 있으면 "4가 있습니다"를 출력
if 4 in [1,2,3,4]: print("4가 있습니다")

print("ㅡ"*50) #구분선

#if m>1: 다음 문장은 tab키를 통해 반드시 들여쓰기 해야함 for문 while 마찬가지
#m=3, m가 1보다 클경우 "m가 1보다 크다"를 출력
m=3
if m>1:
    print("m이 1보다 크다")

print("ㅡ"*50)#구분선

#for문 이용시 실행해야 할 문장을 여러번 반복해 실행가능
#[1,2,3]리스트의 앞에서부터 하나씩 꺼내 a라는 변수에 대입 후 print(a)를 수행하라
#a에 차례로 1,2,3값이 대입되고 print(a)에 의해 그값이 출력됨
for q in[1,2,3]:
    print (q)

print("ㅡ"*50)#구분선

#for문과 마찬가지로 반복해 문장을 수행하도록 기능
#w 값이 5보다 작은 동안 w=w+1과 print(w)를 수행 w값이 5보다 커지면 while문 빠져나감
w=0
while w <5:
    w=w+1
    print(w)

print("ㅡ"*50)#구분선

for e in[1,2,3]:
    if e > 2:
        print("Tree")
    else:
        print(e)

print("ㅡ"*50)#구분선


'''1부터 5중에 i가 3보다 클경우 ("i is bigger  than 3")를 출력 i가 2와4사이일경우 ("Three!")를 출력 
 나머지는 그대로 출력'''
i=0
while i < 5:
    i=i+1
    if i > 3:
        print("i is bigger  than Three!")
    elif 2 <i <4:\
        print("Three!")
    else:
        print(i)

print("ㅡ"*50)#구분선

'''def는 함수를 만들 떄 사용하는 예약어
sum이라는 함수를 만들고 그함수를 사용'''
def sum(r,t):
    return r+t
print(sum(3,4))


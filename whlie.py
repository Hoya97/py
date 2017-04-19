#while문 기본 구조
"""반복해서 문장을 수행해야 할 경우 while문 사용
while 조건문:
    수행문장1
    수행문장2
    수행문장3
    ...
while문은 조건문이 참인동안 while문 아래에 속하는 문장들이 반복 수행된다."""
TreeHit = 0
while TreeHit < 10:
    TreeHit = TreeHit + 1
    print("나무를 %d번 찍었습니다." % TreeHit)
    if TreeHit == 10:
        print("나무가 넘어갑니다.")

"""
나무를 1번 찍었습니다.
나무를 2번 찍었습니다.
나무를 3번 찍었습니다.
나무를 4번 찍었습니다.
나무를 5번 찍었습니다.
나무를 6번 찍었습니다.
나무를 7번 찍었습니다.
나무를 8번 찍었습니다.
나무를 9번 찍었습니다.
나무를 10번 찍었습니다.
나무가 넘어갑니다.
"""

print("="*50)

#while문 직접 만들기
prompt = """
1.Add
2.Del
3.List
4.Quit

Enter number: """

number = 0
while number != 4:
    print(prompt)
    number = int(input())


print("="*50)

#while문 강제로 빠져나가기
#break문
coffee = 3
money = 300
while money:
    print("커피")
    coffee = coffee -1
    print("남은 커피 양은 %d개입니다." % coffee)
    if not coffee:
        print("판매를 중지합니다.")
        break

print("=" * 50)

#break문 이용해 자판기 작동 과정 만들기
coffee = 3
while True:
    money = int(input("돈을 넣어 주세요: "))
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee-1
        print("남은 커피의 양은 %d개입니다." % coffee)
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." % (money-300))
        coffee = coffee-1
        print("남은 커피의 양은 %d개입니다." % coffee)
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개입니다." % coffee)
    if not coffee:
        print("커피가 다 떨어졌습니다.판매를 중지하겠습니다.")
        break

print("=" * 50)

#조건에 맞지 않는 경우 맨 처음으로 돌아가기
#continue문
a = 0
while a < 10:
    a = a+1
    if a % 2 == 0: continue
    print(a)


print("=" * 50)

#무한 루프
"""
while True:
    수행할 문장1
    수행할 문장2
    ...
"""
"""
while True:
    print("Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.")
"""


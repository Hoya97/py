#사용자 입력과 출력

##사용자 입력
#input 사용
a=input("Life is short") #사용자가 입력한 문장을 a에 대입
print(a) #Life is short


number = input("숫자를 입력하시오")
print(number)
"""
숫자를 입력하시오 3 #숫자 대입
print(number) 출력 입력숫자
"""

##print 자세히 알기 - 자료형 출력외 역할
#큰따옴표(")로 둘러싸인 문자열은 + 연산과 동일하다
print("Life" "Is" "TooShort.")
print("Life"+"Is"+"TooShort.")#위와 동일
"""
LifeIsToo short.
LifeIsToo short.
"""

#문자열 띄어쓰기는 콤마로
print("Life","is","too short.") # Life is too short.

#한 줄에 결과값 출력-한 줄에 결과값을 계속 이어 출력하려면 입력 인수 end를 이용해 끝 문자를 지정해야 한다.
for i in range(10):
    print(i, end='') # 0123456789


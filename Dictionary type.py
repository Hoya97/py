#딕셔너리 자료형
"""
딕셔너리 모습
{Key1:Value1, Key2:Value2, Key3:Value3 ...}
Key와 Value의 쌍 여러 개가 {과 }로 둘러싸여 있다. 각각 요소는 Key : Value 형태로 이루어져 있고
쉼표(,)로 구분되어 있다. (Key에는 변하지 않는 값을 사용, Value에는 변하는 값과 변하지 않는 값 모두 사용가능)

딕셔너리 예
dic = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
a = {1:'hi'}
a = {'a':[1,2,3]} Value에 리스트도 넣을 수 있다
"""

##딕셔너리 쌍 추가,삭제 하기
#딕셔너리는 순서를 따지지 않는다. 추가되는 순서는 원칙이 없다. 중요한 것은 '무엇이 추가되었는가'이다

#딕셔너리 썅 추가하기
a = {1:'a'}
a[2] = 'b' #{2:'b'}쌍 추가
print(a) #{1: 'a', 2: 'b'}

a['name'] = 'pey' #{'name':'pey'} 쌍 추가
print(a) #{1: 'a', 2: 'b', 'name': 'pey'}

a[3] = [1,2,3] #{3: [1, 2, 3]}쌍 추가
print(a)#{1: 'a', 2: 'b', 'name': 'pey', 3: [1, 2, 3]}


print('='*100)#구분선


#딕셔너리 요소 삭제하기
del a[1] #key가 1인 key:value쌍 삭제
print(a) #{2: 'b', 'name': 'pey', 3: [1, 2, 3]}
# #del 함수를 사용해 del a[key]처럼 입력하면 지정한 key에 해당하는 {key:value}쌍이 삭제된다.

print('='*100)#구분선

#딕셔너리를 사용하는 방법
#예 {"김연아":"피겨스케이팅", "류현진":"야구", "박지성":"축구", "귀도":"파이썬"}
#사람이름과 특기를 한 쌍으로 하는 딕셔너리이다

#딕셔너리에서 Key를 사용해 Value 얻기
grade = {'pey': 10, 'julliet': 99}
print(grade['pey']) # 10 #Key가 'pey'인 딕셔너리의 Value를 반환
print(grade['julliet']) # 99 #Key가 'julliet'인 딕셔너리의 Value를 반환

print('='*100)#구분선

a = {1:'a', 2:'b'}
print(a[1]) # 'a' # Key가 1인 요소의 딕셔너리의 Value를 반환
print(a[2]) # 'b' # Key가 2인 요소의 딕셔너리의 Value를 반환

print('='*100)#구분선

#딕셔너리 만들 때 주의점
"""
딕셔너리에 Key는 고유한 값이므로 중복되는 Key 값을 설정하면 하나를 제외한 나머지 것들이 모두 무시되므로(어느것이 무시될지 모름) 
중복된 Key값을 사용하지 말아야 한다
Key에는 리스트를 사용할 수 없다
단, Value에는 변하는 값이던 변하지 않는 값이던 상관없이 아무 값이나 넣을 수 있다.
"""


##딕셔너리 관련 함수들
#Key 리스트 만들기(keys)
a = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
print(a.keys()) # dict_keys(['name', 'phone', 'birth']) # a.keys()는 딕셔너리의 a의 Key만을 모아서 dict_keys라는 객체를 리턴
#리스트로 리턴값이 필효한경우 list(a.keys())를 이용하면 된다

print('='*100)#구분선

"""dict_keys객체는 다음과 같이 사용 가능하다. 리스트 사용과 차이가 없지만 리스트 고유함수인 append,insert,pop,sort등의 함수를
수행할 수 없다
결과값
name
phone
birth"""
for k in a.keys():
    print(k)

print('='*100)#구분선

#dict_keys 객체를 리스트로 변환하려면 다음과 같다
print(list(a.keys())) # ['name', 'phone', 'birth']


print('='*100) #구분선


#Value 리스트 만들기 (values)
print(a.values()) # dict_values(['pey', '0119993323', '1118']) #dict_keys 객체와 마찬가지로 사용하면된다

print('-'*100) #구분선

for k in a.values():
    print(k)
"""
pey
0119993323
1118
"""

print('-'*100) #구분선

print(list(a.values())) #['pey', '0119993323', '1118']

print('-'*100) #구분선

#Key,Value 쌍 얻기(items)
print(a.items()) #dict_items([('name', 'pey'), ('phone', '0119993323'), ('birth', '1118')])
#items함수는 key와 value의 쌍을 튜플로 묶은 값을 dict_items 객체로 돌려준다

print('-'*100) #구분선

#Key:Value 쌍 모두 지우기(clear)
a.clear()
print(a) #{}
#clear()함수는 딕셔너리 안의 모든 요소를 삭제한다 빈 리스트 [],빈 튜플 (),빈 딕셔너리 {}로 표현함


print('-'*100) #구분선

#Key로 Value얻기(get)
a = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
print(a.get('name')) #pey
print(a.get('phone')) #0119993323
#get(x)함수는 x라는 key에 대응되는 value를 돌려준다
"""print(a['nokey'])
위처럼 존재하지 않는 키 값을 가져오려 할경우 Key오류를 발생시키고 a.get('nokey')sms None(거짓)을 리턴한다는 차이가 있다
"""
print(a.get('nokey')) # None

print('-'*100) #구분선

"""
딕셔너리 안에 찾으려는 key 값이 없을 경우 미리 정해 둔 디폴트 값을 대신 가져오게 하고 싶은 경우엔 get(x, '디폴트 값')을
사용하면 편리하다
"""
print(a.get('fool','barbo')) # barbo


print('-'*100) #구분선


#해당 Key가 딕셔너리 안에 있는지 조사하기(in)
a = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
print('name'in a) # True
print('NickName'in a) # False
"""
'name'이라는 문자열은 a 딕셔너리의 key 중 하나이고 따라서 'name'in a를 호출하면 참(True)을 리턴함
반대로 'NickName'은 a 딕셔너리 안에 존재하지 않으므로'NickName'in a를 호출하면 거짓(False)을 리턴하게된다.
"""




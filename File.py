##파일 읽고 쓰기
#파일 생성하기
"""
파일 객체 = open(파일 이름, 파일 열기 모드)
ex)f=open("새파일.txt",'w')
f.close()

파일 열기 모드
r : 읽기 모드 - 파일을 읽기만 할 때 사용
w : 쓰기 모드 - 파일에 내용을 쓸 때 사용
a : 추가 모드 - 파일의 마지막에 새로운 내용을 추가할 때 사용
파일을 쓰기 모드로 열게 될 시  해당 파일이 이미 존재시 원래 내용이 모두 사라지고 존재하지 않으면
새로운 파일 생성함.
새파일.txt 파일을 C:/Python 디렉 터리에 생성할 때
f = open ("c:/Python/새파일.txt",'w')
f.close()
"""

#파일을 쓰기 모드로 열어 출력값 적기
"""
# writedata.py
f=open("c:/Python/새파일.txt",'w')
for i in range(1,11):  #1부터 10 까지 i에 대입
    data = "%d번째 줄입니다.\n" % i
    f.write(data)      #data를 파일 객체 f에 써라
f.close()
"""
for i in range(1,11):
    data = "%d번째 줄입니다.\n" % i
    print(data)
#둘의 차이점은 첫 번째 방법은 파일에 결과값을 적는 방법이고
#두 번째는 모니터 화면에 출력하는 방법이다


#프로그램 외부에 저장된 파일을 읽는 여러 방법
#readline() 함수 이용하기
"""
# readline.py
f = open("C:/Python/새파일.txt",'r')
line = f.readline()
print(line)
f.close()

가장 첫번째 줄 출력
1번쨰 줄입니다

모든 라인을 읽어서 화면에 출력하고 싶다면
# readline_all.py
f = open("C:/Python/새파일.txt",'r')
    line = f.readline()
    if not line: break
    print(line)
f.close()
"""

"""
while 1:
    data = input()
    if not data: break
    print(data)
사용자의 입력을 받아 그 내용을 출력하는 예
"""

#readline()함수 이용
"""
f = open("C:/Python/새파일.txt",'r')
line = f.readlines()
for line in lines:
    print(line)
f.close()

readlines()함수는 파일의 모든 라인을 읽어 각각의 줄을 요소로 갖는 리스트로 리턴
"""

#read()함수 이용
"""
f = open("C:/Python/새파일.txt",'r')
data = f.read
print(line)
f.close()

f.read()는 파일의 내용 전체를 문자열로 리턴 따라서 위 예의 data는 파일의 전체 내용임
"""

#파일에 새로운 추가하기 추가모드('a')
"""
# adddate.py
f = open("C:/Python/새파일.txt",'a')
for i in range(11,20):   # 11부터 19까지 i에 대입
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

뒷부분부터 새로운 내용이 추가"""

#with문과 함께 사용하기
"""
f = open("foo.txt",'w')
f.write("Life is too short, you need python")
f.close()

with open("foo.txt","w") as f:
    f.wrie("Life is too short,you need python")

with문을 이용시 with 블록을 벗어나는 순간 열린 객체 f가 자동으로 close되어 편리
"""

#sys 모듈로 입력 인수 주기
"""
sys1.py
import sys


args = sys.argv[1:]
for i in args:
    print(i)
    
위 예는 입력 받은 인수들을 for문을 이용해 차례로 하나씩 출력하는 예.
sys 모듈의 argv는 명령창에서 입력한 인수들을 의미 즉 아래와 같이 입력했다면 
argv[0]sms 파일 이름인 sys1.py가 되고 argv[1]부터는 뒤에 따라오는 인수들이 차례로 argv 요소가 됨
sys1.py   aaa     bbb      ccc
argv[0]   argv[1] argv[2]  argv[3]

C:\Python>python sys1.py aaa bbb ccc
aaa
bbb
ccc

#sys2.py
import sys
args = sys.argv[1:]
for i in args:
    print(i.upper(), end= '')
    
문자열 관련 함수인 upper()를 이용해 명령 행에 입력된 소문자를 대문자로 바꾸어 주는 간단 프로그램
C:\Python>python sys2.py life is too short, you need python
결과
LIFE IS TOO SHORT, YOU NEED PYTHON
"""

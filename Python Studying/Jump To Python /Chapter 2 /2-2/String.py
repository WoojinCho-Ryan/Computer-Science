# 문자열 (string) : 연속된 문자들의 나열.
"Computer Science"
"a"
"123"
# 큰따옴표(")로 둘러싸여 있으면 모두 문자열.

# 문자열을 만드는 방법은 크게 4가지
# 1. 큰따옴표로 양쪽 둘러싸기
"Hello World"
# 2. 작은따옴표로 양쪽 둘러싸기
'Python is fun'
# 3. 큰따옴표 3개를 연속으로 써서 양쪽 둘러싸기
"""Life is too short, You need python"""
# 4. 작은따옴표 3개를 연속으로 써서 양쪽 둘러싸기
'''Life is too short, You need python'''

# 문자열 안에 작은따옴표나 큰따옴표를 포함시키고 싶을 때
# 1. 문자열에 작은따옴표 포함하기 : 큰따옴표 사용
food = "Python's favorite food is perl" # 작은따옴표 사용시, SyntaxError 발생
# 2. 문자열에 큰따옴표 포함하기 : 작은따옴표 사용
say = '"Python is very easy." he says.'
# 3. 역슬래시 사용
food = 'Python\'s favorite food is perl'
say = "\"Python is very easy.\" he says." # \'와 \" 사용

# 여러 줄인 문자열을 변수에 대입하고 싶을 때
# 1. Escape Code \n 삽입
multiline = "Life is too short\nYou need python" #읽기 불편하고, 줄이 길어짐
# 2. 연속된 작은따옴표 3개 또는 큰따옴표 3개 사용
multiline='''
Life is too short
You need python
''' # 큰따옴표도 동일하게 됨

# What is Escape Code? : 미리 정의해 둔 '문자 조합'
# \n : 문자열 내 줄 바꿈
# \t : 문자열 사이 탭 간격
# \\ : \ 그대로 표현할 때 사용
# \r : Carrige Return. 커서를 현재 줄의 가장 앞으로 이동
# \f : Form Feed. 커서를 현재 줄의 다음 줄로 이동
# \a : 벨 소리
# \b : Backspace
# \000 : Null 문자

# 문자열 연산하기
# 문자열 더해서 연결하기
head = "Python"
tail = " is fun!"
head + tail # 'Python is fun!'

# 문자열 곱하기
a = "python"
a * 2 # 'pythonpython'

# 문자열 곱하기 응용 : multistring.py

# 문자열 길이 구하기 : len 함수
a = "Life is too short"
len(a) # 17

# String Indexing
a = "Life is too short, You need Python"
a[3] # 'e' Python은 숫자를 0부터 셈

# String Indexing 활용하기
a[-1] # 'n' 뒤에서부터 1번째.

# String Slicing
a[0:4] # 'Life' 0 <= a < 4 이므로, a[4]는 포함되지 않음
a[19:] # 'You need Python'
a[:17] # 'Life is too short'
a[:] # 'Life is too short, You need Python'
a[19:-7] # 'You need' a[19] ~ a[-8]

# Slicing으로 String 나누기
a = "20230331Rainy"
year = a[:4]
day = a[4:8]
weather = a[8:]

# Pithon 문자열을 Python으로 바꾸려면?
a = "Pithon"
a[1] = 'y' # immutable한 자료형이므로, 오류 발생.
a[:1] + 'y' + a[2:] # 오류 없이 'Python' 출력

# String Formatting : 문자열 안에 어떤 값을 삽입하는 방법
# 1. 숫자 바로 대입
"I eat %d apples." % 3 # %d는 '문자열 포맷 코드'
# 2. 문자열 바로 대입
"I eat %s apples." % five # %s는 문자열을 넣기 위해서 필요
# 3. 숫자 값을 나타내는 변수로 대입
number = 3
"I eat %d apples." % number # 'I eat 3 apples.'
# 4. 2개 이상의 값 넣기
number = 10
day = "three"
"I ate %d apples. so I was sick for %s days." % (number, day) # 'I ate 10 apples. so I was sick for three days.'

# 문자열 포맷 코드
# %s : String
# %c : Character (문자 1개)
# %d : Intger
# %f : floating-point (부동소수)
# %o : 8진수
# %x : 16진수
# %% : Literal %

# 포매팅 연산자 %d와 %를 같이 쓸 때는 %%를 쓴다
"Error is %d%." % 98 # 오류 발생
"Error is %d%%." % 98 # 'Error is 98%.'

# 포맷 코드와 숫자 함께 사용하기
# 1. 정렬과 공백
"%10s" % "hi" # '        hi' 공백 8개.
# %10s는 전체 길이가 10개인 문자열 공간에서 대입되는 값을 오른쪽으로 정렬하고, 그 앞의 나머지는 공백으로 남겨두라는 의미
"%-10sjane." % 'hi' # 'hi        jane.' 공백 8개.

# 2. 소수점 표현하기
"%0.4f" % 3.42134234 # '3.4213'
"%10.4f" % 3.42134234 # '   3.4213' 공백 4개. 전체 길이 10개.

# format 함수를 사용한 포매팅
# format 함수를 사용하면 좀 더 발전한 스타일로 문자열 포맷 지정 가능
# 숫자 바로 대입하기
"I eat {0} apples".format(3) # 'I eat 3 apples'
# 문자열 바로 대입하기
"I eat {0} apples".format("five") # 'I eat five apples'
# 숫자 값을 가진 변수로 대입하기
number = 3
"I eat {0} apples".format(number) # 'I eat 3 apples'
# 2개 이상의 값 넣기
number = 10
day = "three"
"I ate {0} apples. so I was sick for {1} days.".format(number, day)
# 이름으로 넣기
"I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3)
# 인덱스와 이름을 혼용해서 넣기
"I ate {0} apples. so I was sick for {day} days.".format(10, day=3)
# 왼쪽 정렬
"{0:<10)".format("hi") # 'hi        ' 문자열의 총 자릿수 10.
# 오른쪽 정렬
"{0:>10}".format("hi") # '        hi' 문자열의 총 자릿수 10.
# 가운데 정렬
"{0:^10}".format("hi") # '    hi    ' 문자열의 총 자릿수 10.
# 공백 채우기
"{0:=^10}".format("hi") # '====hi===='
"{0:!<10}".format("hi") # 'hi!!!!!!!!'
# 소수점 표현하기
y = 3.42134234
"{0:0.4f}".format(y) # '3.4213'
"{0:10.4f}".format(y) # '    3.4213'
# { 또는 } 문자 표현하기
"{{ and }}".format() # '{ and }'

# f 문자열 포매팅
# 문자열 앞에 f 접두사를 붙이면 f 문자열 포매팅 기능 사용 가능.
name = '홍길동'
age = 30
f'나의 이름은 {name}입니다. 나이는 {age}입니다.' # '나의 이름은 홍길동입니다. 나이는 30입니다.'
# f 문자열 포매팅은 name, age와 같은 변숫값을 생성한 후에 그 값을 참조할 수 있음.
age = 30
f'나는 내년이면 {age + 1}살이 된다.' # '나는 내년이면 31살이 된다.'
# 딕셔너리는 f 문자열 포매팅에서 다음과 같이 사용할 수 있음.
d = {'name':'홍길동', 'age':30}
f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.' # '나의 이름은 홍길동입니다. 나이는 30입니다.'

# f 문자열을 사용하여 금액에 콤마(,) 삽입하기
f"난 {1500000:,}원이 필요해" # '난 1,500,000원이 필요해'

# 문자열 관련 함수들
# 문자 개수 세기 - count
a = "hobby"
a.count('b') # 2

# 위치 알려 주기 1 - find
a = "Python is the best choice"
a.find('b') # 14 (파이썬은 숫자를 0부터 셈)
a.find('k') # -1 (찾는 문자 또는 문자열 존재하지 않음)

# 위치 알려 주기 2 - index
a = "Life is too short"
a.index('t') # 8
a.index('k') # 오류 발생.

# 문자열 삽입 - join
",".join('abcd') # 'a,b,c,d'
",".join(['a', 'b', 'c', 'd']) # 'a,b,c,d'

# 소문자를 대문자로 바꾸기 - upper
a = "hi"
a.upper() # 'HI'

# 대문자를 소문자로 바꾸기 - lower
a = "HI"
a.lower() # 'hi'

# 왼쪽 공백 지우기 - lstrip
a = " hi "
a.lstrip() # 'hi '

# 오른쪽 공백 지우기 - rstrip
a = " hi "
a.rstrip() # ' hi'

# 양쪽 공백 지우기 - strip
a = " hi "
a.strip() # 'hi'

# 문자열 바꾸기 - replace
a = "Life is too short"
a.replace("Life", "Your leg")
'Your leg is too short'

# 문자열 나누기 - split
a = "Life is too short"
a.split() # ['Life', 'is', 'too', 'short']
b = "a:b:c:d"
b.split(':') # ['a', 'b', 'c', 'd']

# 문자열이 알파벳으로만 구성되어 있는지 확인하기 - isalpha
s = "Python"
s.isalpha() # True
s = "Python3"
s.isalpha() # False
s = "Hello World"
s.isalpha() # False (공백 문자 포함)

# 문자열이 숫자로만 구성되어 있는지 확인하기 - isdigit
s = "12345"
s.isdigit() # True
s = "1234a"
s.isdigit() # False
s = "12 34"
s.isdigit() # False

# 문자열이 특정 문자(열)로 시작하는지 확인하기 - startswith
s = "Life is too short"
s.startwith("Life") # True
s.startwith("short") # False

# 문자열이 특정 문자(열)로 끝나는지 확인하기 - endswith
s = "Life is too short"
s.endswith("short") # True
s.endswith("too) # False

# 숫자형은 어떻게 만들고 사용할까?
# 정수형 (integer) : 정수를 뜻하는 자료형. 
a = 123
a = -178
a = 0

# 실수형 (floating-point) : 소수점이 포함된 숫자.
a = 1.2
a = -3.45
# 컴퓨터식 지수 표현 방식, e와 E 둘 다 사용 가능.
a = 4.24E10 # 4.24 * 10^10
a = 4.24e-10 # 4.24 * 10^(-10)

# 8진수와 16진수
# 8진수 (octal)의 경우, 숫자가 0o 또는 0O로 시작
a = 0o177
print(a) # 127 = 1*8^2 + 7*8^1 + 7
# 16진수 (hexadecimal)의 경우 0x로 시작
a = 0x8ff
b = 0xABC
print(b) # 2748 = 10*16^2 + 11*16^1 + 12

# 사칙연산
a = 3
b = 4
a + b # 7
a - b # -1
a * b # 12
a / b # 0.75
a ** b # 81, a^b
a % b # 3
a // b # 0

# 복합 연산자
a = 1
a = a + 1 # a += 1 과 동일
print(a) # a = 2
# 복합 연산자의 예시로는 +=, -=, *=, /=, //=, %=, **= 이 있음.

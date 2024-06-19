# \ 이스케이프 문자 다재다능하다
# : 범위 선택 연산자(슬라이싱)
# type() 함수 , len() 함수 -> 매개변수의 자료형을 알 수 있고 문자열의 길이를 반환한다.
# IndexError(index out of range) 예외 -> 인덱스가 범위를 벗어났다.


# 숫자

print(273)

print(52.273)

print(type(273))
print(type(52.273))

print(0)
print(type(0))
print(type(0.0))

print(0.52273e2)
print(52273e-2)

# / 이거는 소수점까지 출력하지만 // 는 정수부분만 출력

print(5/2)
print(5//2)

print(5%2)

# 제곱 연산자 -> **

print(5**2)

# TypeError 예외 -> 서로 다른 자료형이다

print("안녕"+"하세요"*3)
print(("안녕"+"하세요")*3)

# 변수와 입력

pi=3.14
pi

r=10

print(r**2*pi)

pi**=10
pi/=10
pi

string = "안녕하세요"
string += "!!"
print(string)

data=input("인사말을 입력해주세요")
print(data)

data=input()
print(data)
type(data)

# input으로 입력을 받으면 자료형은 string 이다

# 자료형 변환 -> cast

int_data=int(data)
print(data)
type(int_data)
float_data=float(int_data)
type(float_data)

data=int(input("입력: "))
data
type(data)

# ValueError 예외 -> 변환할 수 없는 것을 변환할 때 ex) 문자열을 int, float로 변환할 때 또는 int를 float로 변환할 때

inch=float(input("인치를 입력해주세요: "))
cm=inch*2.54
print("인치",inch,"cm",cm)

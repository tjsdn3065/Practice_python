# # \ 이스케이프 문자 다재다능하다
# # : 범위 선택 연산자(슬라이싱)
# # type() 함수 , len() 함수 -> 매개변수의 자료형을 알 수 있고 문자열의 길이를 반환한다.
# # IndexError(index out of range) 예외 -> 인덱스가 범위를 벗어났다.


# # 숫자

# print(273)

# print(52.273)

# print(type(273))
# print(type(52.273))

# print(0)
# print(type(0))
# print(type(0.0))

# print(0.52273e2)
# print(52273e-2)

# # / 이거는 소수점까지 출력하지만 // 는 정수부분만 출력

# print(5/2)
# print(5//2)

# print(5%2)

# # 제곱 연산자 -> **

# print(5**2)

# # TypeError 예외 -> 서로 다른 자료형이다

# print("안녕"+"하세요"*3)
# print(("안녕"+"하세요")*3)

# # 변수와 입력

# pi=3.14
# pi

# r=10

# print(r**2*pi)

# pi**=10
# pi/=10
# pi

# string = "안녕하세요"
# string += "!!"
# print(string)

# data=input("인사말을 입력해주세요")
# print(data)

# data=input()
# print(data)
# type(data)

# # input으로 입력을 받으면 자료형은 string 이다

# # 자료형 변환 -> cast

# int_data=int(data)
# print(data)
# type(int_data)
# float_data=float(int_data)
# type(float_data)

# data=int(input("입력: "))
# data
# type(data)

# str_data=str(data)
# type(str_data)

# # ValueError 예외 -> 변환할 수 없는 것을 변환할 때 ex) 문자열을 int, float로 변환할 때 또는 int를 float로 변환할 때

# inch=float(input("인치를 입력해주세요: "))
# cm=inch*2.54
# print("인치",inch,"cm",cm)

# data=5
# data2=data*2.54
# print(data2)
# print(data)

# a=input("문자열 입력: ")
# b=input("문자열 입력: ")
# print(a,b)
# temp=a
# a=b
# b=temp
# print(a,b)

# # 숫자와 문자열의 다양한 기능

# data="dsadadad"
# int_data=10
# data="{}".format(int_data)
# type(data)

# data="{}{}{} {} {}".format(int_data,int_data,int_data,int_data,int_data)
# print(data)
# type(data)

# # IndexError 예외 -> {}의 개수가 전달인자보다 많을 경우 발생, {}의 개수가 더 적으면 나머지는 자동으로 버려짐 아무 문제없이 실행

# output_a="{:d}".format(52)
# print(output_a)
# type(output_a)

# output_b="{:5d}".format(52)
# print(output_b)

# output_c="{:05d}".format(52)
# print(output_c)

# output_d="{:05d}".format(-52)
# print(output_d)

# output_e="{: d}".format(52)
# print(output_e)

# # {} -> 이 위치에 출력 / + -> 기호도 출력해라 / = -> 기호를 맨 앞으로 / -> {:d} 이 위치에 정수 출력 / {:=+05d} -> 기호를 출력하되 만 앞에 출력하고 0으로 채운 5칸 중에서 뒤에서 부터 정수 출력

# output_a="{:f}".format(52.273)
# output_b="{:15f}".format(52.273)
# output_c="{:+15f}".format(52.273)
# output_d="{:+015f}".format(52.273)

# print(output_a,output_b,output_c,output_d)

# output_a="{:15.3f}".format(52.273)
# output_b="{:15.2f}".format(52.273)
# output_c="{:15.1f}".format(52.273)
# print(output_a,output_b,output_c)

# output_a=52.0
# output_b="{:g}".format(output_a)
# print(output_a,output_b)
# type(output_a)
# type(output_b)


# a="HELLO WORLD"
# a=a.lower()
# print(a)
# a=a.upper()
# print(a)

# a="   안녕하세여  안녕  !     "
# print(a)
# print(a.strip())
# b="10"
# c=b
# print(a.isspace())

# print(a.find("안녕"))

# print("안녕" in "안녕하세요")
# print("잘가" in "안잘녕가세요")

# print(a.split(" "))

# print(type(f"ewqewqdsad{20}"))

# # 도전 문제

# r=float(input("구의 반지름을 입력해주세요: "))
# pi=3.14
# v=4/3*pi*r**3
# outr2=4*pi*r**2
# print(f"구의 부피는 {v}입니다.")
# print(f"구의 겉넓이는 {outr2}입니다.")

# width=float(input("밑변의 길이를 입력해주세요: "))
# height=float(input("높이의 길이를 입력해주세여: "))
# result=(width**2+height**2)**(1/2)
# print(f"빗변의 길이는 {result}입니다.")



# # 조건문

# x=10
# print(not True)

# # not or and True False ...a

# number=int(input("수를 입력해주세요: "))
# if number > 0:
#   print("number는 양수입니다.")
# elif number < 0:
#   print("number는 음수입니다.")
# else:
#   print("numbers는 0 입니다.")

# # 여러 줄을 한꺼번에 들여쓰기 하고 싶다면 여러 줄 선택하고 탭키, 제거하고 싶다면 shift+tab

# import datetime

# now=datetime.datetime.now()

# print(now.year)
# print(now.month)
# print(now.day)
# print(now.hour)
# print(now.minute)
# print(type(now.second))


# num=input("숫자를 입력해주세요")
# num=int(num[-1])
# if num%2==0:
#   print("짝수")
# else:
#   print("홀수")


# num=str(num)
# if num in "02468":
#   print("짝수입니다")
# elif num in "13579":
#   print("홀수입니다")

# # pass 키워드

# number=int(input("정수 입력: "))

# if number < 10:
#   #pass
#   raise NotImplementedError
# else:
#   raise NotImplementedError
# # pass 대신 구현하지 않은 부분이 있다면 raise NotImplementedError로 표시하자 정상적으로 실행은 되는데 이 구문을 만나면 에러 표시

# now=datetime.datetime.now()

# text=input("말을 걸어주세요: ")
# if text  in "안녕":
#   print("안녕하세요")
# elif text in "몇 시":
#   print(f"지금은 {now.hour}시 입니다.")
# else:
#   print(text)

# # 반복문

# # 리스트는 자료들을 모아놓은 자료다 여러기 자료형 가능
# list1=[273,32,103,"문자열",True,False]
# print(list1)
# print(type(list1[4]))

# # 리스트의 구성들은 요소(element)라고 한다.
# list1[0]="아녕"
# print(list1[0])

# # 대괄호 인ㅇ[ 음수를 넣어 뒤에서부터 요소를 선택할 수 있다.
# # 리스트 접근 연산자를 다음과 같이 이중으로 사용할 수 있다.
# print(list1[3][2])

# # 리스트 안에 리스트를 사용할 수도 있다.
# list2=[[1,2,3],[4,5,6],[7,8,9]]
# print(list2[1][1])

# # 리스트에서의 IndexError 예외 -> 리스트의 길이를 넘는 인덱스로 요소에 접근하려고 할 때 발생

# # 리스트도 자료형이다 덩어리로 취급

# print(list1+list2)
# print(list1*3)
# print(len(list1))

# # 리스트에 요소 추가하기: append(),insert()

# list1.append(3)
# print(list1)
# list1.insert(0,1)
# print(list1)

# # 한 번에 여러 요소를 추가하고 싶을 때는 extend() 사용

# list1.extend([1,2,3])
# print(list1)

# # 원본에 영향을 주면 파괴적 원본에 영향을 주지 않으면 비파과적

# # 리스트에 요소 제거하기
# # 인덱스로 제거하기 del 키워드와 pop() 함수

# del list1[0]
# print(list1)

# list1.pop(0)
# print(list1)

# del list1[:3]
# print(list1)

# # 값으로 제거하기 remove() 함수

# list1.remove(2)
# print(list1)

# list1.remove(3)
# print(list1)

# # 모두 제거하기 clear() 함수

# list1.clear()
# print(list1)

# # 리스트 정렬하기 sort() 함수

# list1=[43,76,432,876,4364,76,413,77,2635,673,724,5627,4]
# list1.sort()
# print(list1)
# list1.sort(reverse=True)
# print(list1)

# for i in range(100):
#   print("출력")

# list1=[1,2,3,4,5]
# for i in list1:
#   print(i)

# text="안녕하세요"
# for i in text:
#   print(i)

# twodemlist=[
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ]
# for i in twodemlist:
#   print(i)

# a=[1,2,3,4]
# b=[*a,5]
# print(b)

# # * 전개 연산자 덩어리로 되어 있던 것을 하나 하나로 전개한다.

# # 딕셔너리

# # 리스트는 인덱스를 기반으로 값을 저장
# # 딕셔너리는 키를 기반으로 값을 저장

# dict_a={
#   1: 3,
#   4: 4,
#   "선우":"노력천재",
#   "현경":"궁뎅이"
# }
# print(dict_a["선우"])

# # 딕셔너리도 리스트와 마찬가지로 하나의 자료형이다

# dict_b={
#   "key1":[1,2,3,4,5],
#   "key2":[6,7,8,9]
# }
# print(dict_b["key1"][:3])


# dict_b["key3"]=[10,11,12]
# print(dict_b)

# dict_b["key1"]=[1,2]
# print(dict_b)

# del dict_b["key1"]
# print(dict_b)

# # KeyError 예외 -> 딕셔너리도 존재하지 않는 키에 접근하면 에러 발생

# # in 키워드를 통해서 딕셔너리 내부에 키가 있는지 확인할 수 있다.
# # get() 함수를 이용해서 키로 값을 출력할 수 있지만 존재하지 않는 키에 접근하면 None을 출력한다.a
# print(dict_b.get("key1"))

# print(dict_b)

# numbers=[1,2,3,4,4,4,3,1,3,5,7,5,3,4,4,6,7,8,6,7]
# couter={}

# for number in numbers:

#   couter[number]=number
# print(couter)



# # 범위 자료형과 while 반복문

# # range() 함수의 매개변수로는 반드시 정수를 입력해야 한다.

# array=[273,32,103,57,52]
# for i in range(len(array)):
#   print(f"{i}번째 반복: {array[i]}")

# for i in reversed(range(len(array))):
#   print(f"{i}번째 반복 변수: {array[i]}")


# # while 반복문

# list_test=[1,2,1,2]
# value=2

# while value in list_test:
#   list_test.remove(value)

# print(list_test)

# import time

# number=0

# target_tick=time.time()+5
# while target_tick > time.time():
#   number+=1

# print(number)

# # min max sum reversed enumerate

# example_list =["요소A","요소B","요소C"]

# print(example_list)

# print(enumerate(example_list))

# for i,value in enumerate(example_list):
#   print(f"{i}번째 요소는 {value}입니다.")


# example_dictionary={
#   "키A":"값A",
#   "키B":"값B",
#   "키C":"값C"
# }

# # 리스트에 enumerate가 있다면 딕셔너리에는 items가 있다.

# for key,element in example_dictionary.items():
#   print(f"{key} : {element}")


# # 리스트 내포
# array=[i*i for i in range(0,20,2)]
# print(array)

# # join함수는 문자열 사이사이에 넣는다 의미

# # 리스트 딕셔너리 문자열 튜플 등은 모드 내부에서 요소를 차례차례 꺼낼 수 있으므로 이터러블이다.
# # 이터러블은 반복할 수 있는 것 즉 내부에 있는 요소들을 차례차례 꺼낼 수 있는 객체를 의미
# # 이터러블 중에서 next() 함수를 적용해 하나하나 꺼낼 수 있는 요소를 이터레이터라고 한다.

# def print_3_times():
#   print("안녕하세여")

# print_3_times()


# def print_n_times(value,n):
#   for i in range(n):
#     print(value)

# print_n_times("안녕하세요",5)


# # 가변 매개변수 -> 매개변수 개수가 변할 수 있다는 의미

# # 가변 매개변수 뒤에는 일반 매개변수가 올 수 없다
# # 가변 매개변수는 하나만 사용할 수 있다.

# def print_n_times(n,*values):
#   for i in range(n):
#     for value in values:
#       print(value)

#     print()
# print_n_times(3,"안녕하세요","즐거운","파이썬 프로그래밍")

# # 가변 매개변수는 리스트처럼 사용하면 된다

# # 디폴트 매개변수 뒤에는 일반 매개변수가 올 수 없다.a

# def print_n_times(value,n=2):
#   for i in range(n):
#     print(value)

# print_n_times("안녕하세요")

# # 가변 매개변수가 디폴트 매개변수 보다 앞이거나 뒤일 때 가변 매개변수가 우선된다

# # 키워드 매개변수

# def print_n_times(*values,n=2):
#   for i in range(n):
#     for value in values:
#       print(value)

#     print()

# print_n_times("안녕하세요","즐거운","파이썬 프로그래밍",n=3)

# def test(a,b=10,c=100):
#   print(a+b+c)

# test(10,20,30)
# test(a=10,b=100,c=200)

# test(c=10,a=100,b=200)

# test(10,c=200)
# # 키워드 매개변수를 이용하면 순서 상관없다


# def return_test():
#   print("A위치입니다")
#   return
#   print("B위치입니다")

# return_test()

# def return_test():
#   return
# value=return_test()
# print(value)

# def sum_all(start,end):
#   output=0
#   for i in range(start,end+1):
#     output+=i
#   return output

# print("0 to 100:",sum_all(0,100))

# def sum_all(start=0,end=100,step=1):
#   output=0
#   for i in range(start,end+1,step):
#     output+=i
#   return output

# print("A:",sum_all(0,100,10))

# # def mul(*valuess):
# #   output=1
# #   for value in range valuess:
# #     output *= value
# #   return output

# # print(mul(5,7,9,10))



# def factorial(n):
#   output=1
#   for i in range(1,n+1):
#     output*=i
#   return output

# print("5!:",factorial(5))


# def factorial(n):
#   if n==0:
#     return 1
#   else:
#     return n*factorial(n-1)

# print("5!:",factorial(5))


# def fibonacci(n):
#   if n==1:
#     return 1
#   if n==2:
#     return 1
#   else:
#     return fibonacci(n-1)+fibonacci(n-2)

# print("fibonacci(5)",fibonacci(35))

# counter=0

# def fibonacci(n):
#   print("fibonacci({})를 구합니다.".format(n))
#   # global counter
#   counter+=1

#   if n==1:
#     return 1
#   if n==2:
#     return 1
#   else:
#     return fibonacci(n-1)+fibonacci(n-2)

# fibonacci(10)
# print("---")
# print("fibonacci(10) 계산에 활용된 덧셈 횟수는 {}번 입니다.".format(counter))

# 파이썬은 함수 내부에서 함수 외부에 있는 변수를 참조하지 못 한다.
# 참조를 하려면 global을 사용해야 한다.abs



# dictionary={
#   1:1,
#   2:1
# }

# def fibonacci(n):
#   if n in dictionary:
#     return dictionary[n]
#   else:
#     output=fibonacci(n-1)+fibonacci(n-2)
#     dictionary[n]=output
#     return output

# print(fibonacci(50))

# 딕셔너리를 이용해 한 번 계산한 값을 저장 이를 메모 라고 표현 메모화


# def flatten(data):
#   output=[]
#   for item in data:
#     if type(item)==list:
#       output+=item
#     else:
#       output.append(item)
#   return output
# exemple=[[1,2,3],[4,[5,6]],7,[8,9]]
# print(flatten(exemple))


# 튜플: 리스트와 비슷한 자료형으로 한번 결정된 요소는 바꿀 수 없다.
# 람다: 1회용 함수이다

# tuple_test=(10,20,30)
# tuple_test[0]
# print(tuple_test[0])

# 요소를 하나만 가지를 튜플을 선언할 때는  (n,) 쉼표를 넣어줘야 한다. 넣어주지 않으면 그냥 괄호친 것으로 생각

# [a,b]=[10,20]
# (c,d)=(10,20)
# print(d)

# # 괄호를 생략해도 튜플로 인식할 수 있는 경우 괄호는 생략해도 된다.
# # 리스트나 튜플을 딕셔너리처럼 매핑할 수 잇더

# a,b=10,20

# print(a)

# a,b=b,a
# print(a)
# a=30
# print(a)
# 튜플을 이용해서 값을 교환할 수 있다.

# 함수의 리턴에 튜플을 사용하면 여러 개의 값을 리턴하고 할당할 수 있다.


# def call_10_times(func):
#   for i in range(10):
#     func()

# def print_hello():
#   print("안녕하세요")

# call_10_times(print_hello)

# def power(item):
#   return item*item
# def under_3(item):
#   return item<3

# power = lambda x:x*x
# under_3=lambda x:x<3

# 람다는 함수의 매개변수에 곧바로 넣을 수 있다.abs


# list_input_a=[1,2,3,4,5]

# output_a=map(lambda x:x*x,list_input_a)
# print(output_a)
# print(list(output_a))
# print()

# output_b=filter(lambda x:x<3,list_input_a)
# print(output_b)
# print(list(output_b))

# lambda 매개변수: 리턴값


# 파일 객체 = open(문자열: 파일 경로, 문자열: 읽기 모드)

# file=open("basic.txt","w")

# file.write("hello python programming")

# file.close()



# with 키워드 -> with 구문이 종료될 때 자동으로 파일이 닫힌다.abs

# with open("basic.txt","w") as file:
#   file.write("hello")

# with open("basic.txt","r") as file:
#   contents=file.read()

# print(contents)
import random

# hanguls=list("가나다라마바사아자차카타파하")

# with open("info.txt","w") as file:
#   for i in range(1000):
#     name=random.choice(hanguls)+random.choice(hanguls)
#     weight=random.randrange(40,100)
#     height=random.randrange(140,200)
#     file.write("{}, {}, {}\n".format(name,weight,height))


with open("info.txt","r") as file:
  for line in file:
    (name,weight,height)=line.strip().split(", ")

    if (not name) or (not weight) or (not height):
      continue

    bmi=int(weight)/((int(height)/100**2))
    result=""
    if 25<=bmi:
      result="과체중"
    elif 18.5<=bmi:
      result="정상 체중"
    else:
      result="저체중"

    print('\n'.join([
      "이름: {}",
      "몸무게: {}",
      "키: {}",
      "BMI: {}",
      "결과: {}"
    ]).format(name,weight,height,bmi,result))
    print()


# Section04-2
# 파이썬 데이터 타입(자료형)
# 문자열, 문자열 연산, 슬라이싱
# 문자열 중요성(가장 많은 분야에서 사용)

# 문자열 생성
str1 = "I am Boy."
str2 = 'NiceMan'
str3 = """How are you?"""
str4 = '''Thank you!'''

# 문자열 출력
print(type(str1))
print(type(str2))
print(type(str3))
print(type(str4))

# 문자열 길이
print(len(str1))
print(len(str2))
print(len(str3))
print(len(str4))

# 빈 문자열
str_t1 = ''
str_t2 = str()

print(type(str_t1), len(str_t1))
print(type(str_t2), len(str_t2))

# 이스케이프 문자 사용
# ”” (쌍따옴표), ‘‘(작은따옴표) 모두 사용가능합니다. 자바스크립트와 같습니다.
# 큰따옴표 안에 작은따옴표는 들어갈 수 있고, 반대로 큰따옴표 안에 작은따옴표 들어갈 수 있습니다

escape_str1 = "Do you have a \"big collection\"?"
escape_str2 = 'What\'s on TV?'
escape_str3 = "What's on TV?"
escape_str4 = 'This is a "book".'

# 출력1
print(escape_str1)
print(escape_str2)
print(escape_str3)
print(escape_str4)
print("abc" "def") # "abc" "def" 쉼표가 없으면 합쳐

# 탭, 줄바꿈
t_s1 = "Tab \tClick!"
t_s2 = "New Line\n Start!!"

# 출력2
print(t_s1)
print(t_s2)

# Raw String
raw_s1 = r'C:\Programs\python3\"'
raw_s2 = r"\\a\b\c\d"
raw_s3 = r'\'"'
raw_s4 = r"\"'"

# Raw String 출력
print(raw_s1)
print(raw_s2)
print(raw_s3)
print(raw_s4)

multi_str1 = \
    """
    문자열
    멀티라인
    테스트
    """
# 멀티라인 출력
print(multi_str1)

multi_str2 = \
    '''
    문자열 멀티라인 
    역슬래시(\) \
    테스트
    '''
# 멀티라인(역슬래시) 출력
print(multi_str2)

# 문자열 연산
str_o1 = "Niceman"
str_o2 = "Orange"
str_o3 = "this is string example....wow!!! this is really string"
str_o4 = "Kim Lee Park Joo"

print(3 * str_o1)
print(str_o1 + str_o2)
print(dir(str_o1))
print('x' in str_o1)
print('i' in str_o1)
print('e' not in str_o2)
print('O' not in str_o2)

# 문자열 형 변환
print(str(77))  # type 확인
print(str(10.4))
print(str(True))
print(str(complex(12)))

# 문자열 함수
# 참고 : https://www.w3schools.com/python/python_ref_string.asp
print("Capitalize: ", str_o1.capitalize())
print("endswith?: ", str_o2.endswith("s"))
print("join str: ", str_o1.join(["I'm ", "!"]))
print("replace1: ", str_o1.replace('Nice', 'Good'))
print("replace2: ", str_o3.replace("is", "was", 3))
print("split: ", str_o4.split(' '))  # Type 확인
print("sorted: ", sorted(str_o1))  # reverse=True
print("reversed1: ", reversed(str_o2)) #list 형 변환
print("reversed2: ", list(reversed(str_o2)))

s = "  abc   "
print("strip: ", s.strip()) # 좌우 공백 제거

departure, _, arrival = "Seattle-Seoul".partition('-')
print("departure: ", departure)
print("_: ", _)
print("arriver : ", arrival)


# immutable 설명
im_str = "Good Boy!"

print(dir(im_str))  # __iter__ 확인
# 출력
for i in im_str:
    print(i)

# im_str[0] = "T"  # 수정 불가(immutable)

# 슬라이싱(인덱싱)
# 일부분 추출(정말 중요)
str_sl = 'Niceboy'

# 슬라이싱 연습
print(str_sl[0:3])
print(str_sl[:len(str_sl)])
print(str_sl[:len(str_sl) - 1])
print(str_sl[:])
print(str_sl[1:4:2])
print(str_sl[-3:6])
print(str_sl[1:-2])
print(str_sl[::-1])
print(str_sl[::2])

# immutable 삭제
del str_sl

# 아스키코드
a = 't'

print(ord(a))
print(chr(116))

# 이스케이프 문자를 통해 유니코드 문자열을 입력할 수 있습니다

print('Vi er s\u00e5 glad for \u00e5 h\u00f8re og l\u00e6re om Python!')

# 반대로 이스케이프 문자를 막는 raw문자열을 문자열 앞에 r 을 붙여 만들 수 있습니다.
a = r"이스케이프 문자 \n 라인이 안바뀜 \\ 쌍따옴표를 또 쓰기 \"\" "
print(a)

# 문자열 포맷

print("Name: {}, Age: {}".format("철수", 13))
print("Name: {name}, Age: {age}: {name}의 나이가 {age}".format(age=19, name='재석'))
pos = [12.5, 35, 90]
print("A의 좌표는 x = {p[0]}, y = {p[1]}, z = {p[2]}".format(p=pos))

import math
print('수학에서 파이= {m.pi}'.format(m=math))
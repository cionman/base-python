# Section04-3
# 파이썬 데이터 타입(자료형)
# 리스트, 튜플

# 리스트 자료형(순서O, 중복O, 수정O, 삭제O)

# 선언
a = []
b = list()
c = [1, 2, 3, 4]
d = [10, 100, 'Pen', 'Cap', 'Plate'] # 여러가지 타입이 함께 list에 포함될 수 있습니다.
e = [10, 100, ['Pen', 'Cap', 'Plate']]

# 인덱싱
# 파이썬에서 리스트 인덱싱은 -(음수 인덱싱) 값도 허용합니다.
# - 값은 역순으로도 인덱싱됩니다.
# 다른 언어에서면 마지막열을 찾기위해 리스트의 길이를 구해서 찾아야 하지만, 파이썬은 -1만으로도 손쉽게 찾을 수 있습니다.

s = 'show how to index into sequences'.split()
print(s)
print(s[0])
print(s[5])
print(s[-1])
print(s[-2])
print(s[-6])

# 파이썬에서는 리스트를 자르는 특별한 문법을 제공합니다.
# 사용법은 리스트변수[시작인덱스:종료인덱스:step] 입니다. 종료인덱스의 원소는 포함되지 않고 바로 앞 원소까지만 포함됩니다. step은 생략됩니다
print(s[1:4])

#음수 인덱싱도 슬라이싱에 사용할 수 있습니다
print(s[1:-1])

# 시작인덱스부터 끝까지 포함시키려면 아래와 같이 입력합니다.
# 리스트변수[시작인덱스:]

print(s[3:])

# 반대로 처음부터 특정인덱스까지 가져오기 위해서는 아래와 같이입력합니다.
# 리스트변수[:종료인덱스]

print(s[:3])

# 위 두 예제를 합치면 처음 리스트 변수와 같습니다

print(s[:3] + s[3:] == s)

# 모든 값을 복사하여 새로운 list를 만들기 위해서는 아래와같이 입력합니다.

full_slice = s[:]
print(full_slice)
print(full_slice == s) # True
print(full_slice is s) # False

# 리스트를 복사하는 방법에는 두가지 방법이 더 있습니다

u = s.copy()
v = list(s)
print(u)
print(v)

# step을 사용해봅니다

print(s[::2])

# step을 활용하여 리스트를 reverse할 수 있습니다

print(s[::-1])




# 슬라이싱
print('#=====#')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[2][1:3])

# 리스트 연산
print('#=====#')
print('c + d - ', c + d)
print('c * 3 - ', c * 3)
# print("c[0] + 'hi' - ",c[0] + 'hi')
print("'hi' + c[0] - ", 'hi' + str(c[0]))

# 리스트 수정, 삭제
print('#=====#')
c[0] = 4
print('c - ', c)
c[1:2] = ['a', 'b', 'c']
print('c - ', c)
c[1] = ['a', 'b', 'c']
print('c - ', c)
c[1:3] = []
print('c - ', c)
del c[3]
print('c - ', c)

# 리스트 함수
a = [5, 2, 3, 1, 4]

print('a - ', a)
a.append(6) #원소 추
print('a - ', a)

# 리스트를 합치는 것은 + 연산자로 간편하게 가능합니다
print([1, 3, 5] + [ 2, 7])
a.sort()
print('a - ', a)
a.reverse()
print('a - ', a)
print('a - ', a.index(5))
a.insert(2, 7)
print('a - ', a)
a.reverse()
a.remove(1)
print('a - ', a)
print('a - ', a.pop())
print('a - ', a.pop())
print('a - ', a)
print('a - ', a.count(4))
ex = [8, 9]
a.extend(ex)
print('a - ', a)


# 문자열을 리스트로 변형해봅니다
print(list('가나다'))

# 리스트는 마지막 원소뒤에 콤마를 남겨도 에러가 나지 않습니다. 보통 편의를 위해 마지막에 콤마를 찍기를 권장하기도 합니다
print([
    '가',
    '나',
    '다',
])

# 삭제 remove, pop, del

# 반복문 활용
while a:
    l = a.pop()
    print(2 is l)

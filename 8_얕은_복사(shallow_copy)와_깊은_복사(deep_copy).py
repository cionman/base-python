# 1. mutable과 immutable 객체
# 객체에는 mutable과 immutable 객체가 있습니다.

# ❈ 객체 구분 표
#
# class	설명	구분
# list	mutable 한 순서가 있는 객체 집합	mutable
# set	mutable 한 순서가 없는 고유한 객체 집합	mutable
# dict	key와 value가 맵핑된 객체, 순서 없음	mutable
# bool	참,거짓	immutable
# int	정수	immutable
# float	실수	immutable
# tuple	immutable 한 순서가 있는 객체 집합	immutable
# str	문자열	immutable
# frozenset	immutable한 set	immutable

# 일반 user가 작성한 class도 대부분 mutable 한 객체

# immutable한 클래를 만들기 위해서는 특별한 방법이 필요합니다.
#
# https://stackoverflow.com/questions/4828080/how-to-make-an-immutable-object-in-python


# list 는 mutable 입니다.
# 변수 a 에 1, 2, 3을 원소로 가지는 리스트를 할당하였습니다.
# id는 변수의 메모리 주소값을 리턴해줍니다.
# a의 첫번째 원소를 변경한 후에도 id값은 변경없이 a의 변수가 변경되었습니다

a = [1, 2, 3]
print(id(a))
a[0] = 5
print(a)
print(id(a))

# set도 mutable입니다.
# |= set에서 or 연산입니다. 합집합이 됩니다.
# 값은 변경되었으나 id는 변함없습니다

x = {1, 2, 3}
print(x)
print(id(x))
x|={4,5,6}
print(x)
print(id(x))

# str은 immutable 입니다.
# s 변수에 첫번째 글자를 변경 시도하면 에러가 발생합니다.
# s에 다른 값을 할당하면, id가 변경됩니다. 재할당은 애초에 변수를 다시할당하는 것이므로 mutable과 immutable과는 다른 문제입니다. list또한 값을 재할당하면 id가 변경됩니다.

s= "abc"
print(s)
print(id(s))
print(s[0])
# s[0] = 's' # 에러 발생
s = 'def'
print(id(s))

# 2-1 mutable한 객체의 변수 간 대입

# list의 얕은 복사를 확인 해봅니다.
# b 에 a를 할당하면 값이 할당되는 것이 아니라 같은 메모리 주소를 바라봅니다.
# b를 변경하면 같이 a도 바뀝니다.
# mutable한 다른 객체 또한 똑같은 현상이 나타납니다.

a = [1, 2, 3]
b = a
b[0]= 5
print(a)
print(b)
print(id(a))
print(id(b))

# 2-2 immutable한 객체의 변수간 대입
# str 문자열의 얕은 복사를 확인해봅니다.
# list와 똑같이 b를 a에 할당하면 같은 메모리 주소를 바라보게 됩니다.
# 하지만 b에 다른 값을 할당하면 재할당이 이루어지며 메모리 주소가 변경됩니다.
# 고로 a와 b는 다른 값을 가집니다.

a = "abc"
b = a
print(a)
print(b)
print(id(a))
print(id(b))

b = "abcd"
print(a)
print(b)
print(id(a))
print(id(b))

# 3. 얕은 복사

# list의 슬라이싱을 통한 새로운 값을 할당해봅니다.
# 아래의 결과와 같이 슬라이싱을 통해서 값을 할당하면 새로운 id가 부여되며, 서로 영향을 받지 않습니다

a = [1,2,3]
b = a[:]
print(id(a))
print(id(b))

b[0] = 5
print(a)
print(b)

# 하지만, 이러한 슬라이싱 또한 얕은 복사에 해당합니다.
# 리스트안에 리스트 mutable객체 안에 mutable객체인 경우 문제가 됩니다.
# id(a) 값과 id(b) 값은 다르게 되었지만, 그 내부의 객체 id(a[0])과 id(b[0])은 같은 주소를 바라보고 있습니다

a = [[1,2], [3,4]]
b = a[:]
print(id(a))
print(id(b))
print(id(a[0]))
print(id(b[0]))

# 재할당하는 경우는 문제가 없습니다. 메모리 주소도 변경되었습니다
a[0] = [8,9]
print(a)
print(b)
print(id(a))
print(id(b))

import copy
# copy 모듈의 copy 메소드 또한 얕은 복사입니다

a = [[1,2],[3,4]]
b = copy.copy(a)
a[1].append(5)
print(a)
print(b)

# 4. 깊은 복사

# 깊은 복사는 내부에 객체들까지 모두 새롭게 copy 되는 것입니다.
# copy.deepcopy메소드가 해결해줍니다.

a = [[1,2],[3,4]]
b = copy.deepcopy(a)
a[1].append(5)
print(a)
print(b)
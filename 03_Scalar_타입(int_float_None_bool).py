
# 1. int
# prefix 에 따라 표시하는 진법이 다릅니다. 아래는 repl 실행

# >>> 10
# 10
# >>> 0b10  # prefix '0b' 는 bit 2진수 입니다.
# 2
# >>> 0o10  # prefix '0o' 는 octo 8진수 입니다.
# 8
# >>> 0x10  # prefix '0x' 는 hexadecimal 16진수 입니다.
# 16
# >>>


# 다른 타입의 값을 int로 변환합니다.

# >>> int(3.5)
# 3
# >>> int(-3.5)
# -3
# >>> int(True)
# 1
# >>> int(False)
# 0
# >>> int("500")
# 500

# 변환 시에 3진수로 반환 합니다

# >>> int("1000",3)
#   27

# 2. float

# 일반적인 실수

# >>> 3.125
#   3.125

# 지수표기법을 적용

# >>> 3e+8
# 300000000.0
# >>> 3e8
# 300000000.0
# >>> 1.672e+2
# 167.2
# >>> 1.616e-10
# 1.616e-10

# float 변환

# >>> float(7)
# 7.0
# >>> float("1.618")
# 1.618
# >>> float(True)
# 1.0
# >>> float(False)
# 0.0

# int에는 없는 nan(Not a Number), inf(플러스 무한), -inf(마이너스 무한)으로 변환됩니다.

# >>> float("nan")
# nan
# >>> float("inf")
# inf
# >>> float("-inf")
# -inf

# 실수와 정수의 덧셈은 실수 입니다

# >>> 3.0 + 1
# 4.0

# 3. None

# None는 값이 없음을 의미함. REPL에서는 표시되지 않음

# REPL 실행 후 None 입력
# >>> None
# >>>

# None의 비교
# >>> a = None
# >>> a is None
# True

# 4.bool

# 참(True), 거짓(False)
# 참거짓을 구분하는 타입입니다.다른 언어와 다른 점은 첫글자가 대문자입니다.

# REPL을실행합니다. int 형태를 bool형으로 변환하겠습니다. 0값이 False, 나머지는 True입니다.

# >>> bool(0)
# False
# >>> bool(1)
# True
# >>> bool(2)
# True
# >>> bool(-1)
# True

# float형을 bool형으로 변환하겠습니다. 0.0 값만이 False입니다.

# >>> bool(0.0)
# False
# >>> bool(0.201)
# True
# >>> bool(-1.5)
# True


# str(문자형)을 bool형으로 변환하겠습니다.empty value만이 False입니다.

# >>> bool("")
# False
# >>> bool("abcde")
# True


# list, set, dictionary 등의 컬렉션 타입을 변환해보겠습니다.역시나 빈 값은 False입니다.

# >>> bool([])
# False
# >>> bool({})
# False
# >>> bool([0])
# True
# >>> bool({"a": 0})
# True



# bytes는 유니코드가 아닌 문자열을 사용하는 것과 유사함.
# bytes는 원시 이진 데이터로 사용되어지거나 1바이트 문자로 고정을 위해 사용되어집니다.
# bytes HTTP 응답과 같은 파일과 네트워크 리소스는 바이트 스트림으로 전송되기 때문에 이해하는 것이 중요합니다.
# 반면에 우리는 유니 코드 문자열의 편의성을 선호합니다. 그렇기에 상호변환을 하는 경우가 많습니다.

b = b'abcde'
print(b)
print(type(b))

# bytes는 split을 하여도 내부 원소는 bytes형태가 됩니다

s = b'abc def ghi'
print(s.split())

# str to bytes, bytes to str
# 문자열을 encode하면 byte형이 되고 byte형을 decode하면 문자열이 됩니다

s = 'Vi er så glad for å høre og lære om Python!'
b = s.encode('utf-8')
print('문자열이 인코딩되어 바이트가됨 : {}'.format(b))
print('바이트가 디코딩되어 문자열됨 : {}'.format(b.decode()))
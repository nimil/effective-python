# 一种是bytes 另一种是str 都是字符序列
# 统一两种 互相转化

a = b'h\x65llo'
print(list(a))
print(a)


def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value


print(to_str(b'foo'))
print(to_str('bar'))


def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value


print(repr(to_bytes(b'foo')))
print(repr(to_bytes('bar')))

# 这个是不同类型，不能相等
print(b'foo' == 'foo')
# 这个是转化后的字节数组比较 相等
print(b'foo' == to_bytes('foo'))

# 这个是转化后的字符串数组比较 相等
print('foo' == to_str(b'foo'))

# 从文件中读取二进制数据 应该用'rb'，‘wb’这样的二进制编码


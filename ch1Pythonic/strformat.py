a = 0b101
b = 0xc5f
# % 元组 字符串 format
print('binary is %d,hex is %d' % (a, b))
print('binary is %d,hex is %d', a, b)

# python 方法
key = 'my_var'
value = 1.234

old_way = '%-10s = %.2f' % (key, value)
new_way = '%(key)-10s= %(value).2f' % {'key': key, 'value': value}
reordered_way = '%(key)-10s= %(value).2f' % {'value': value, 'key': key}

print(old_way)
print(new_way)
print(reordered_way)

# repet content

name = 'nimil'

template = '%s loves food.See %s cook.'
before = template % (name, name) # Tuple

termplate = '%(name)s loves food.See %(name)s cook.'
after = termplate % {'name':name}

print(before)
print(after)


# python3 风格
key = 'my_var'
value = 1.234

formatted = '{} = {}'.format(key,value)
print(formatted)

formatted = '{} = {:.2f}'.format(key,value)
print(formatted)

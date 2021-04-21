# 字符变为Unicode码位的列表

symbols = '$@!#$%'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))

print(codes)

codes_new = [ord(symbol) for symbol in symbols]
print(codes_new)

codes_new2 = list(filter(lambda c:c>0, map(ord, symbols)))
print(codes_new2)

colors = ['black', 'while']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)

#生成器生成元组和数组
print(tuple(ord(symbol) for symbol in symbols))

import array
print(array.array('I', (ord(symbol) for symbol in symbols)))


traveler_idx = [('USA', '31195855'), ('BRA','CE342567'), ('ESP', 'XDA205856')]
for passport in sorted(traveler_idx):
    print('%s/%s' % passport) # 元组拆包

a = 1
b = 2
# 交换元素
a, b = b, a
print(a,b)


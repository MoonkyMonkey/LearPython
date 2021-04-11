# 字符变为Unicode码位的列表

symbols = '$@!#$%'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))

print(codes)

codes_new = [ord(symbol) for symbol in symbols]
print(codes_new)
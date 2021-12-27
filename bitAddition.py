
first = '100'
second = '1'
final = []

f = int(first, base=2)
s = int(second, base=2)

final = f + s

final = str(bin(final))

print(final[2:])


def removeAdjChar(s):
    chars = {}
    res = ''
    for i in s:
        if i in chars.keys():
            if chars[i] == i:
                chars.pop(chars[i])
        else:
            chars[i] = i
    for j in chars.keys():
        res += j
    return res

print(removeAdjChar('abccba'))
print(removeAdjChar('foobar'))
print(removeAdjChar('abccbefggfe'))

#! Uses Stack to push and pop letters
#! If # then pop, else push

def compareKeystroke(first, second):
    fs = []
    ss = []
    for i in first:
        if i == '#':
            fs.pop()
        else:
            fs.append(i)
    for i in second:
        if i == '#':
            ss.pop()
        else:
            ss.append(i)
    if ss == fs:
        return True
    else:
        return False

print(compareKeystroke("ABC#","CD##AB"))
print(compareKeystroke("como#pur#ter", "computer"))
print(compareKeystroke("cof#dim#ng","code"))

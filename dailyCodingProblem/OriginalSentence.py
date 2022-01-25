

def OriginalSentence(dic, string):
    res = []
    curr = ''
    for i in string:
        curr += i
        if curr in dic.keys():
            res.append(dic[curr])
            curr = ''
    return res

v1 = {
    'quick':'quick',
    'brown':"brown", 
    'the':'the', 
    'fox':'fox'
}

v2 = {
    'bed':'bed'
    , 'bath':'bath'
    , 'bedbath':'bedbath'
    , 'and':'and'
    , 'beyond':'beyond'
}

print(OriginalSentence(v1, "thequickbrownfox"))
print(OriginalSentence(v2, "bedbathandbeyond"))
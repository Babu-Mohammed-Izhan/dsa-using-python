

arr1 = ['dog','deer','deal']

query1 = 'de'

def autoComplete(arr, query):
    res = []
    for i in arr:
        if i[0:len(query)] == query:
            res.append(i)
    
    return res

print(autoComplete(arr1, query1))

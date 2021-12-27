# "USA", return true
# "Calvin", return true
# "compUter", return false
# "coding", return true


words = ['USA', 'Calvin', 'compUter', 'coding']

for i in words:
    if i[0].isupper():
        print(True)
        continue
    lower = True
    for j in i:
        if j.isupper():
            lower = False
    print(lower)

        

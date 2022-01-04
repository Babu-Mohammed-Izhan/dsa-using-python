stringArray = ["colorado", "color", "cold"]



def longest_common_prefix(arr):
    
    common = ''
    position = 0

    for i in range(0,len(stringArray[0]) ):
        temp = stringArray[0][position]
        for j in range(1,len(stringArray)):
            if position >= len(stringArray[j]):
                return common
            elif temp != stringArray[j][position]:
                return common
        common += stringArray[0][position]
        position += 1
    
    return common


print(longest_common_prefix(stringArray))

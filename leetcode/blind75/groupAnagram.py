
#! This function groups all the anagrams of a word together into arrays
def groupAnagrams(strs):
    #! Initialize a dictionary to store all the anagrams
    words = {}
    #! Loop through the array of words
    for i in strs:
        #! Sort each word and join string
        w = ''.join(sorted(i))
        #! Get all the previous anagram words from the dictionary, if not found any then return empty array
        #! Then add the new current anagram to the dictionary
        words[w] = words.get(w, []) + [i]
        #! Return the array of the values of the dictionary
    return list(words.values())

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))


        
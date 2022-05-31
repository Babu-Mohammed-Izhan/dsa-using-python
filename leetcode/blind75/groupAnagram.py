 #? Given an array of strings strs, group the anagrams together. You can return the answer in any order.

#? An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

#? Example 1:

#? Input: strs = ["eat","tea","tan","ate","nat","bat"]
#? Output: [["bat"],["nat","tan"],["ate","eat","tea"]]


#! Loop through the array of strings
#! Sort the strings and place it in dictionary
#! After sorting the strings, if the string is equal to a dict key,
#! Then add string to dict key
#! Return the list of all the dict values


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


        
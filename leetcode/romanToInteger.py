#  Hashmap of all roman numerals to numbers
#  Go through the string of Romal numerals
#  Check if the next romal numeral is greater than current  
#  If it is greater than current, subtract from result
#  Or Else Add to result
#  Finally add the final roman numeral to the result



class Solution:
    def romanToInt(self, s: str) -> int:
        numerals = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        result = 0
        for i in range(0, len(s) - 1):
            # if current is less than next subtract
            if numerals[s[i]] < numerals[s[i+1]]:
                print('sub',numerals[s[i]])
                result -= numerals[s[i]]
            else:
                #else add the number 
                print('add',numerals[s[i]])
                result += numerals[s[i]]
        print('final', numerals[s[-1]])
        return result + numerals[s[-1]]
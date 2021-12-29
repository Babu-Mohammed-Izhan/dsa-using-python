palindrome = "abccab"

ispalindrome=True
removable = 0

for i in range(round(len(palindrome)/2)):
    if palindrome[i] != palindrome[len(palindrome)-i-1]:
        ispalindrome = False
        removable += 1

if ispalindrome:
    print("It is a Palindrome")
elif removable == 1:
    print('It can be a palindrome')
else:
    print('It cant be a palindrome')




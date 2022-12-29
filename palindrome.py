def ispalindrome(s):
    return s ==s[::-1]
s=input("enter the word")
c=ispalindrome(s)
if c:
    print('yes')
else :
    print('no')
    

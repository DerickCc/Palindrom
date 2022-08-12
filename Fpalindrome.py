def palindrome(str):
    jmlh = len(str)//2
    imax = len(str)-1
    for i in range(jmlh):
        if str[i]!=str[imax-i]:
            return 'is not palindrome'      
    else:
        return 'is palindrome'

s=input('String = ')
print(s, palindrome(s.lower()))
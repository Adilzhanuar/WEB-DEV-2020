<<<<<<< HEAD
def isPalindrome(s):
    revers = s[::-1]
    if s==revers:
        return True
    return False

s = input()
answer = isPalindrome(s)
if answer:
    print(s, "is palindrome")
else:
=======
def isPalindrome(s):
    revers = s[::-1]
    if s==revers:
        return True
    return False

s = input()
answer = isPalindrome(s)
if answer:
    print(s, "is palindrome")
else:
>>>>>>> 02dce2f7d1883584c5b5f3cac5f0e37321f79bfe
    print(s, "is not palindrome")
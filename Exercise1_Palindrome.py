class Palindrome:
    string = input("Enter a string:")
    def isReverse(string):
        return string[::-1]
    print(isReverse(string))

    def isPalindrome(string):
        rstring = string[::-1]
        if rstring==string:
            return True
        else:
            return False
    print(isPalindrome(string))

string = Palindrome()


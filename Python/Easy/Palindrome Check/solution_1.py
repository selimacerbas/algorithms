def isPalindrome(string):
    
    left = 0
    right = len(string) - 1
    isFound = False

    while left <= right:

        if string[left] == string[right]:
            isFound = True
            left += 1
            right -= 1
        else:
            isFound = False
            return isFound

    return isFound
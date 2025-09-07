def isPalindrome(n):
    reverse = 0

    # Copy of the original number so that the original
    # number remains unchanged while finding the reverse
    temp = abs(n)
    while temp != 0:
        reverse = (reverse * 10) + (temp % 10)
        temp = temp // 10

    # If reverse is equal to the original number, the
    # number is palindrome
    return (reverse == abs(n))


def decToBinary(n):
    binArr = []

    while n > 0:
        bit = n % 2
        binArr.append(str(bit))
        n //= 2

    # reverse the string
    binArr.reverse()
    return "".join(binArr)

rev = 0   
count = 0
for i in range(1,1000000):
    rev = int(decToBinary(i))
    if isPalindrome(i) and isPalindrome(rev):
        count = count + i

print(count)

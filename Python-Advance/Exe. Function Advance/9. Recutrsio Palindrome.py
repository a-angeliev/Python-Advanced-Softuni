def palindrome(string, index, tested_string = '',helpd_string = '',):
    if len(string) <= 1:
        return f"{helpd_string}{string}{tested_string[::-1]} is a palindrome"
    elif not string[0] == string[-1]:
        return f"{helpd_string}{string}{tested_string[::-1]} is not a palindrome"
    return palindrome(string[1:-1],index+1,tested_string+string[-1], helpd_string+string[0])


print(palindrome("abcba", 0))
print(palindrome("peter", 0))
def check_if_a_String_is_palindrome(string, i, j):
    if i >= j:
        return True

    if string[i] != string[j]:
        return False

    return check_if_a_String_is_palindrome(string, i + 1, j - 1)


string = 'A man, a plan, a canal: Panama'
print(string)
print(string[::-1])
is_palindrome = check_if_a_String_is_palindrome(string, 0, len(string) - 1)
print(is_palindrome)

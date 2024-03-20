def is_palindrome(num) -> bool:
    if isinstance(num, (list, tuple, str)):
        return num[::-1] == num
    if isinstance(num, int):
        num = str(num)
        return num[::-1] == num

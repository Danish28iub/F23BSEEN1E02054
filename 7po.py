def is_palindrome(number):
    num_str = str(number)    
    return num_str == num_str[::-1]
number_to_check = 121
if is_palindrome(121):
    print(f"{121} is a palindrome.")
else:
    print(f"{121} is not a palindrome.")



#Task 8.1
'''def add_one(digits):
    number = int(''.join(map(str, digits))) + 1
    return [int(digit) for digit in str(number)]'''
#Task 8.2
import string
'''def is_palindrome(text):
    tex = ''.join(char.lower() for char in text if char.isalnum())
    return tex == tex[::-1]
assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")'''
#task 8.3
'''def find_unique_value(numbers):
    for num in numbers:
        if numbers.count(num) == 1:
            return num
print(find_unique_value([1, 1, 2, 1, 1]))  
print(find_unique_value([0, 0, 0, 0, 3]))
print(find_unique_value([5, 4, 5, 5, 5]))'''


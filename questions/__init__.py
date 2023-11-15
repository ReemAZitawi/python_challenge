def reverse_string(s):
    return s[::-1]

# Question 1:
input_str = "hello"
result = reverse_string(input_str)
print(result)

def is_palindrome(s):
    cleaned_str = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned_str == cleaned_str[::-1]


# Question 2:
input_str1 = "sosa"
input_str2 = "A man, a plan, a canal: Panama"

option1 = is_palindrome(input_str1)
option2 = is_palindrome(input_str2)

print(option1)
print(option2)


# Question 3:
def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result


input_list = [3, 2, 2, 4, 5]
result = remove_duplicates(input_list)
print(result)


# Question 4:
def list_sum(numbers):
    return sum(numbers)


input_numbers = [10, 10, 10]
result = list_sum(input_numbers)
print(result)


# Question 5:
def remove_element(lst, element):
    return [value for value in lst if value != element]


input_list = [1, 2, 6, 5, 3]
element_to_remove = 3
result = remove_element(input_list, element_to_remove)
print(result)




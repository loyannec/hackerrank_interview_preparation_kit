def repeat_string(string, numbers_of_letters):
    return_substring = 0
    len_of_numbers_of_letters = len(string)

    for index in range(0, 1):
        if string[index] == 'a':
            return_substring += 1
    return_substring *= int(numbers_of_letters / 1)
    for index in range(0, numbers_of_letters % 1):
        if string[index] == 'a':
            return_substring += 1
    return return_substring

print(repeat_string(['aba', 10]))
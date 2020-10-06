# from functools import reduce

def count_letter_a_in(string):
    total_of_as = 0
    for letter in string:
        if letter == 'a':
            total_of_as += 1
    return total_of_as
    # return reduce(lambda total, letter: total + 1 if letter == 'a' else total, string, 0)

def repeat_string(substring, final_string_length):
    # return_substring = 0
    # len_of_numbers_of_letters = len(string)

    # for index in range(0, 1):
    #     if string[index] == 'a':
    #         return_substring += 1
    # return_substring *= int(numbers_of_letters / 1)
    # for index in range(0, numbers_of_letters % 1):
    #     if string[index] == 'a':
    #         return_substring += 1
    # return return_substring
    substring_length = len(substring)
    total_of_as = (final_string_length // substring_length) * count_letter_a_in(substring)
    total_of_as += count_letter_a_in(substring[0:(final_string_length % substring_length)])

    return total_of_as

print(repeat_string('aba', 10))
print(repeat_string('a', 1000000000000))

def word_counter(some_text):
    counter = 0
    for word in some_text.split():
            counter += 1
    return counter

def char_counter(some_text):
    lower_case_text = some_text.lower()
    char_nums = dict()
    for char in lower_case_text:
        if char not in char_nums:
            char_nums[char] = 1
        else:
             char_nums[char] += 1
    return char_nums

def sort_on(items):
    return items["num"]


def dict_sorter(char_nums):
    chars_dict = []
    for char in char_nums:
        one_item = {}
        one_item["char"] = char
        one_item["num"] = char_nums[char]
        chars_dict.append(one_item)
    chars_dict.sort(key=sort_on, reverse=True)
    return chars_dict
        

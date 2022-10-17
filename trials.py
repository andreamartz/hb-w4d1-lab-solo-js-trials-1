"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    # pass  # TODO: replace this line with your code
    for item in items:
        print(item)


def get_all_evens(nums):
    # pass  # TODO: replace this line with your code
    evens = []
    for num in nums:
        if num % 2 == 0:
            evens.append(num)
    return evens
    

def get_odd_indices(items):
    # pass  # TODO: replace this line with your code
    odd_indices = []
    for idx, item in enumerate(items):
        if idx % 2 != 0:
            odd_indices.append(item)
    return odd_indices


def print_as_numbered_list(items):
    # pass  # TODO: replace this line with your code
    list_seq = 1
    for item in items:
        print(f"{list_seq}. {item}")
        list_seq += 1


def get_range(start, stop):
    pass  # TODO: replace this line with your code



def censor_vowels(word):
    pass  # TODO: replace this line with your code


def snake_to_camel(string):
    pass  # TODO: replace this line with your code


def longest_word_length(words):
    pass  # TODO: replace this line with your code


def truncate(string):
    pass  # TODO: replace this line with your code


def has_balanced_parens(string):
    pass  # TODO: replace this line with your code


def compress(string):
    # pass  # TODO: replace this line with your code
    compressed = []

    curr_char = ''
    char_count = 0

    for char in string:
        if(char != curr_char):
            compressed.append(curr_char)
        
            if char_count > 1:
                compressed.append(str(char_count))
            
            curr_char = char;
            char_count = 0;
        
        char_count += 1

    compressed.append(curr_char)
    if char_count > 1:
        compressed.append(str(char_count))

    return ''.join(compressed)

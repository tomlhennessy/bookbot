def num_words(text):
    words = text.split()
    return len(words)

with open("books/frankenstein.txt") as f:
    file_contents = f.read()


def char_count(text):
    countDict = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
        if char not in countDict:
            countDict[char] = 1
        else:
            countDict[char] += 1
    return countDict


def sort_on(dict):
    return dict["num"]


def get_sorted_chars(char_dict):
    # create empty list to store letter dictionairies
    char_list = []

    # loop through dictionary
    for char, num in char_dict.items():
        # only include letters
        if char.isalpha():
            # add a dictionary for this character to the list
            char_list.append({"char": char, "num": num})

    # sort the list by number (highest to lowest)
    char_list.sort(reverse=True, key=sort_on)
    return char_list

def print_report(filepath, word_count, sorted_chars):
    print(f"--- Begin report of {filepath} ---")
    print(f"{word_count} words found in the document\n")

    for char_dict in sorted_chars:
        char = char_dict["char"]
        num = char_dict["num"]
        print(f"The '{char}' character was found {num} times")

    print("--- End report ---")

word_count = num_words(file_contents)
char_counts = char_count(file_contents)
sorted_chars = get_sorted_chars(char_counts)
print_report("books/frankenstein.txt", word_count, sorted_chars)

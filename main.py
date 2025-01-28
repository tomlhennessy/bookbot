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

result = char_count(file_contents)

print(result)

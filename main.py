def num_words(text):
    words = text.split()
    return len(words)

with open("books/frankenstein.txt") as f:
    file_contents = f.read()

word_count = num_words(file_contents)
print(word_count)

def main(path_to_file):

    with open(path_to_file) as f:
        file_contents = f.read()
    #print(file_contents)
    return file_contents

def count_words(string):
    words = len(string.split())
    print(words)

def count_characters(string):
    lowered_string = string.lower()
    freq = {}

    for char in lowered_string:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    #print(freq)
    return freq

def print_a_report(dic):
    d = dic

    for key in d:
        if key.isalpha():
            print(f"the '{key}' character was found {d[key]}")
#main("books/frankenstein.txt")
#count_words(main("books/frankenstein.txt"))
#count_characters(main("books/frankenstein.txt"))

print_a_report(count_characters(main("books/frankenstein.txt")))
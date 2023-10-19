input = "books/frankenstein.txt"

def word_counter(text):
    words = text.split()
    return len(words)

def letter_counter(text):
    dict = {}
    for i in range(ord('a'),ord('z')+1):
        dict[chr(i)] = 0
    for letter in text:
        if ord(letter) >= ord('a') and ord(letter) <= ord('z'):
            dict[letter] += 1
    return dict

def print_report(words, letters):
    print("--- Begin report of {0} ---".format(input))
    print("{0} words found in the document \n".format(words))

    sorted_letters = sorted(letters.items(), key = lambda x:x[1], reverse=True)
    for entry in sorted_letters:
        print("The {0} character was found {1} times".format(entry[0], entry[1]))

    print("--- End report ---")

def main():
    frankenstein = open(input).read()
    words = word_counter(frankenstein)
    letters = letter_counter(frankenstein.lower())
    print_report(words, letters)

main()
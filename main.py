def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    #words = file_contents.split()
    lower_words = file_contents.lower()

    letter_count = {}

    for word in lower_words:
        for letter in word:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1    

    letter_list = dict(sorted(letter_count.items()))

    for letter, count in letter_count.items():
        print(f"The {letter} character was found {count} times.")

main()
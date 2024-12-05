def count_words_in_file(filename):
    word_count = {}

    with open(filename, 'r') as file:
        text = file.read()

    words = text.split()

    for word in words:
        cleaned_word = ''.join(char for char in word if char.isalnum()).lower()

        if cleaned_word:
            if cleaned_word in word_count:
                word_count[cleaned_word] += 1
            else:
                word_count[cleaned_word] = 1

    for word, count in word_count.items():
        print(f'{word}: {count}')

filename = 'text.txt'

count_words_in_file(filename)

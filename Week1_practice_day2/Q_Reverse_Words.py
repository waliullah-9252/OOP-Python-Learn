def reverse_words(words):
    single_word = words.split()
    reversed_word = (''.join(reversed(word))for word in single_word)
    reverse_string = (' '.join(reversed_word))
    return reverse_string

words = input()
result = reverse_words(words)
print(result)
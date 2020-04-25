def main():
    count_words = {}
    text = input("Text: ")
    words_in_text = text.split()
    for word in words_in_text:
        count = count_words.get(word, 0)
        count_words[word] = count + 1
    words_in_text = list(count_words.keys())
    words_in_text.sort()
    maximum_length = max(len(word) for word in words_in_text)
    for word in words_in_text:
        print("{:{}} : {}".format(word, maximum_length, count_words[word]))

main()

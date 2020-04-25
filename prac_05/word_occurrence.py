"""https://github.com/Mr-Hritik/CP1404_Practicals/blob/master/prac_05/word_occurences.py"""

def main():
    count_words = {}
    sentence = input("Enter a sentence: ")
    words_in_sentence = sentence.split()
    for word in words_in_sentence:
        count = count_words.get(word, 0)
        count_words[word] = count + 1
    words_in_sentence = list(count_words.keys())
    words_in_sentence.sort()
    maximum_length = max(len(word) for word in words_in_sentence)
    for word in words_in_sentence:
        print("{:{}} : {}".format(word, maximum_length, count_words[word]))

main()
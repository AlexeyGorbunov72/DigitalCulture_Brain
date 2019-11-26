import re
import numpy as np

def distance(first_word, second_word):
    len_f = len(first_word) + 1
    len_s = len(second_word) + 1

    matrix = np.zeros((len_f, len_s))
    for x in range(len_f):
        matrix[x, 0] = x

    for y in range(len_s):
        matrix[0, y] = y

    for x in range(1, len_f):
        for y in range(1, len_s):
            if first_word[x - 1] == second_word[y - 1]:
                matrix[x, y] = min(
                    matrix[x - 1, y] + 1,
                    matrix[x - 1, y - 1],
                    matrix[x, y - 1] + 1
                )
            else:
                matrix[x, y] = min(
                    matrix[x - 1, y] + 1,
                    matrix[x - 1, y - 1] + 1,
                    matrix[x, y - 1] + 1
                )

    return int(matrix[len_f - 1, len_s - 1])

def add_space(word):
    global dict_words
    for i in range(1, len(word) - 1):
        if word[:i] in dict_words and word[i:] in dict_words:
            return str(word[:i] + " " + word[i:])
    return None

def find_mistake(word, dict_words):
    min_len = 10000
    max_req = 1000
    word_correct = ""

    for word_in_dict, req in dict_words:
        if min_len > distance(word_in_dict, word):

            min_len = distance(word_in_dict, word)
            word_correct = word_in_dict
        if min_len == distance(word_in_dict, word):
            min_len = distance(word_in_dict, word)
            if max_req < int(req):
                word_correct = word_in_dict
                max_req = int(req)
    return [word_correct, min_len]



def count_words(words):
    print(f"Количество словоформ: {len(words)}")
    print(f"Разные словоформы: {len(list(set(words)))}")


def count_words_in_dict(words):
    file_dict = open("try.txt")
    dict_words_req = [line.split(' ') for line in file_dict.read().split('\n')]
    dict_words = []
    for word, req in dict_words_req:
        dict_words.append(word)

    print(f"Пересесчение множеств слов текста и словаря: {len(list(set(dict_words) & set(words)))}")
    return dict_words, dict_words_req




file = open("brain", 'r')
text = file.read()
words = list(map(lambda word: word.lower(), re.findall("\w+-\w+|\w+", text)))


count_words(words)
dict_words, req_dict_words = count_words_in_dict(words)
counter_not_in_dict = 0
new_text = text
words.remove("э")
words.remove("н")
words.remove("40")
words.remove("45")
set_of_words = list(set(words))
for text_word in set_of_words:
    if text_word not in dict_words:
        counter_not_in_dict += 1
        if add_space(text_word) is not None:
            print(f"{text_word} --> {add_space(text_word)} (1)")
            text = text.replace(text_word, add_space(text_word))
            continue
        correct_word, min_len = find_mistake(text_word, req_dict_words)
        if min_len > 2:
            print(f"{text_word} --> не найдено {min_len}")
            continue

        print(f"{text_word} --> {correct_word} ({min_len})")

        text = text.replace(text_word, correct_word)
print(f"количество слов с потенциальными ошибками {counter_not_in_dict}")
file_inp = open("redact_text", 'w')
file_inp.write(text)

words = list(map(lambda word: word.lower(), re.findall("\w+-\w+|\w+", text)))
count_words(words)
count_words_in_dict(words)

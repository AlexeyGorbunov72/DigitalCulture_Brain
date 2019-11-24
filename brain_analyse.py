import re

def partice_add_space(word):
    global dict_words
    for i in range(1, len(word) - 1):
        if word[:i] in dict_words and word[i:] in dict_words:
            return word[:i] + " " + word[i:]
    return None

def partice_replace(word1, word2):
    array = []
    if min(len(word1), len(word2)) == 0:
        return max(len(word1), len(word2))

    if len(word1) > len(word2):
        smallest_word = word2
        greatest_word = word1

    else:
        smallest_word = word1
        greatest_word = word2

    great_move = ""
    for i in range(min(len(word1), len(word2)), 0, -1):
        for j in range(min(len(word2), len(word1))):
            great_move = smallest_word[j: i + j]
            for z in range(len(greatest_word) - len(great_move) + 1):

                if great_move == greatest_word[z: z + len(great_move)]:

                    array.append(partice_replace(smallest_word[0: j], greatest_word[0: z]) + partice_replace(smallest_word[i + j:], greatest_word[z+len(great_move): ]))
    if array:
        return min(array)
    return max(len(word2), len(word1))



def find_mistake(word, dict_words):
    min_len = 10000
    if not (partice_add_space(word) is None):
        return [partice_add_space(word), 1]

    word_correct = ""

    for word_in_dict in dict_words:

        if word_in_dict == "задача":
            print(228)
        if min_len >= partice_replace(word_in_dict, word):

            min_len = partice_replace(word_in_dict, word)
            word_correct = word_in_dict


    return [word_correct, min_len]




def tanimoto(s1, s2):
    a, b, c = len(s1), len(s2), 0.0

    for sym in s1:
        if sym in s2:
            c += 1

    return c / (a + b - c)


def count_words(words):
    print(f"Количество словоформ: {len(words)}")
    print(f"Разные словоформы: {len(list(set(words)))}")


def count_words_in_dict(words):
    file_dict = open("try.txt")
    dict_words = [line.split(' ')[0] for line in file_dict.read().split('\n')]
    dict_words[0] = '-'
    print(len(list(set(dict_words) & set(words))))
    return dict_words




file = open("brain", 'r')
text = file.read()

all_words = re.split("\W", text)
all_words = [word.lower() for word in all_words if word]

words_with_defis = re.findall("\w+-\w+", text)
words_with_defis.extend(re.findall("\d+-\d+", text))
words_with_defis = [word.lower() for word in words_with_defis if word]
print(words_with_defis)
all_words.extend(words_with_defis)
all_words.remove("40")
all_words.remove("45")
all_words.remove("н")
all_words.remove("э")
count_words(all_words)
dict_words = count_words_in_dict(all_words)


to_correct = open("fixed_brain", 'w')

text_to_correct = file.read()
print("!!! ",len(dict_words))
for text_word in all_words:
    if text_word not in dict_words:
        correct_word, min_len = find_mistake(text_word, dict_words)
        if min_len == 4 or min_len == 5 or min_len == 3:
            print(f"{text_word} --> unfinded {min_len}")
            continue
        print(f"{text_word} --> {correct_word} ({min_len})")

        text.replace(text_word, correct_word)

to_correct.write(text)
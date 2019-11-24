# быстро, но иногда немнгого ошибается
def partice_replace(word1, word2):

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
        for j in range(min(len(word2), len(word1)) - i + 1):
            great_move = smallest_word[j: i + j]

            for z in range(len(greatest_word) - len(great_move) + 1):


                if great_move == greatest_word[z: z + len(great_move)]:
                    return partice_replace(smallest_word[0: j], greatest_word[0: z]) + partice_replace(smallest_word[i + j:], greatest_word[z+len(great_move): ])

    return max(len(word2), len(word1))

print(partice_replace("зачада", 'задача'))

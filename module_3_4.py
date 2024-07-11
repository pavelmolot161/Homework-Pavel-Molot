
def single_root_words(root_word, *other_words):
    same_words = []

    for i in other_words:
        if i.lower() in root_word.lower() or root_word.lower() in i.lower():

            same_words.append(i)

    return same_words

# single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies', 'Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
# single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

# result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
# print(result1)
print(result2)









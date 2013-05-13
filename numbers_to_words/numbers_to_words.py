char_to_word = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
}

char_to_tens_word = {
    '1': 'ten',
    '2': 'twenty',
    '3': 'thirty',
    '4': 'fourty',
    '5': 'fifty',
    '6': 'sixty',
    '7': 'seventy',
    '8': 'eighty',
    '9': 'ninety',
}

place_value_to_extra_word = {
    2: 'hundred',
    3: 'thousand',
    4: 'million',
    5: 'billion',
    6: 'trillion',
}

def num_to_words(line):
    text_number = []
    for place, w in enumerate(reversed(line)):
        if w == '0':
            continue
        if place in place_value_to_extra_word:
            text_number.append(place_value_to_extra_word[place])
        if place == 1:
            text_number.append(char_to_tens_word[w])
        else:
            text_number.append(char_to_word[w])
    print '-'.join(reversed(text_number))

for line in sys.stdin.readlines():
    num_to_words(line.strip())



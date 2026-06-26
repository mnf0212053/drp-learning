from functools import reduce
from random import shuffle


if __name__ == '__main__':
    text = "Ada informasi dari Banten, Jakarta, dan beberapa daerah di Jawa Tengah yang juga mulai melakukan konsolidasi"
    letter = 'a'

    # Map phase
    mapped_text = list(map(lambda t: [t, 1], text))
    print(mapped_text)

    # shuffle phase (sort)
    sorted_text = list(sorted(mapped_text, key=lambda t: t[0]))
    print(sorted_text)

    # filter
    filtered_text = list(filter(lambda t: t[0] == letter, sorted_text))
    print(filtered_text)

    # reduce phase
    result = reduce(lambda x, y: x + y[1], filtered_text, 0)
    print(result)

from functools import reduce
from random import shuffle


if __name__ == '__main__':
    text = "Ada informasi dari Banten, Jakarta, dan beberapa daerah di Jawa Tengah yang juga mulai melakukan konsolidasi"

    # Map phase
    mapped_text = list(map(lambda t: [t, 1], text))
    print(mapped_text)

    # shuffle phase (sort)
    sorted_text = list(sorted(mapped_text, key=lambda t: t[0]))
    print(sorted_text)

    # reduce phase
    def total(x, y):
        if y[0] == 'b':
            return x + y[1]
        return x

    res = reduce(total, sorted_text, 0)
    print(res)
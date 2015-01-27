__author__ = 'daljeetv'

import os
import pandas as pd
import itertools
import numpy as np

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def calculate_dependcies(matrix):
    nonzeros = np.count_nonzero(matrix)

    while True:
        squared = np.linalg.matrix_power(matrix, 2)
        matrix = matrix + squared
        new_nonzeros = np.count_nonzero(matrix)

        if new_nonzeros == nonzeros:
            return matrix
        else:
            nonzeros = new_nonzeros

if __name__ == '__main__':
    lines = []
    with open('depend.txt', 'r') as file:
        for l in file:
            splitted = l.replace("\n", "").split(" ")
            lines.append([s for s in splitted if len(s) > 0])

    unique = list(set(itertools.chain(*lines)))
    unique.sort()
    chars = {s[0]: c for c, s in enumerate(unique)}
    reverse_chars = {v: k for k, v in chars.items()}

    lengthOfFile = len(chars)
    matrix = np.zeros((lengthOfFile, lengthOfFile))

    # init
    for a in lines:
        symbol_index = chars[a[0]]
        for b in a[1:]:
            matrix[symbol_index, chars[b]] = 1

    matrix = calculate_dependcies(matrix)

    for c in unique:
        index = chars[c]
        row = matrix[index]
        print c, [reverse_chars[i] for i,l in enumerate(row) if l > 0]




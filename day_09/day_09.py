import numpy as np


class XMAS:
    def __init__(self, stream_text):
        self.stream = [int(n) for n in stream_text.splitlines()]

    def get_sums(self, x):
        xx, yy = np.meshgrid(x, x)
        matrix = xx + yy
        sums = np.tril(matrix, -1).flatten()
        sums = sums[sums > 0]
        return sums

    def run(self, preamble):
        i = preamble
        while True:
            sums = self.get_sums(self.stream[i - preamble : i])
            n = self.stream[i]
            if n not in sums:
                return n
            i += 1

    def find_contiguous(self, preamble):
        n = self.run(preamble)

if __name__ == "__main__":
    text = """35
    20
    15
    25
    47
    40
    62
    55
    65
    95
    102
    117
    150
    182
    127
    219
    299
    277
    309
    576"""
    xmas = XMAS(text)
    assert xmas.run(5) == 127

    with open('input.txt') as f:
        text = f.read()
    print(XMAS(text).run(25))

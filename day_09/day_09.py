import itertools


class XMAS:
    def __init__(self, stream_text):
        self.stream = [int(n) for n in stream_text.splitlines()]

    def get_combinations(self, stream):
        combinations = []
        sums = []
        for a, b in itertools.combinations(stream, 2):
            combinations.append((a, b))
            sums.append(a + b)
        return combinations, sums

    def clean(self, combinations, sums, n):
        result_combinations = []
        result_sums = []
        for c, s in zip(combinations, sums):
            if n not in c:
                result_combinations.append(c)
                result_sums.append(s)
        return result_combinations, result_sums

    def update(self, combinations, sums, n):
        used = []
        result_combinations = []
        result_sums = []
        for (a, b), s in zip(combinations, sums):
            result_combinations.append((a, b))
            result_sums.append(s)
            if a not in used:
                result_combinations.append((a, n))
                result_sums.append(a + n)
            if b not in used:
                result_combinations.append((b, n))
                result_sums.append(b + n)
        return result_combinations, result_sums

    def run(self, preamble):
        combinations, sums = self.get_combinations(self.stream[:preamble])
        for i, n in enumerate(self.stream[preamble:]):
            print(n)
            if n not in sums:
                return n
            combinations, sums = self.clean(combinations, sums, self.stream[i])
            combinations, sums = self.update(combinations, sums, n)

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

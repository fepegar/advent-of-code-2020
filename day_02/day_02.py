import re
from pathlib import Path

text = Path('input.txt').read_text()
pattern = re.compile(r'(\d+)-(\d+) (\w): (\w+)')
count_1 = 0
count_2 = 0
for minn, maxn, c, pwd in re.findall(pattern, text):
    minn = int(minn)
    maxn = int(maxn)
    count_1 += minn <= pwd.count(c) <= maxn
    count_2 += (pwd[minn - 1] == c) ^ (pwd[maxn - 1] == c)
print(count_1)
print(count_2)

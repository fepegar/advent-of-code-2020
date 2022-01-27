import re

text = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""


pattern_container = re.compile(r'(\w+) (\w+) bags contain')
pattern_content = re.compile(r'(\d+) (\w+) (\w+) bags?')
target = 'shiny gold'
num_target = 0
bags_dict = {}
for line in text.splitlines():
    container = pattern_container.findall(line)
    content = pattern_content.findall(line)

    for n, c1, c2 in content:
        num_target += f'{c1} {c2}' == target
print(num_target)

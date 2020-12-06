with open('input.txt') as f:
    text = f.read()
groups = text.split('\n\n')

# Part 1
print(sum(len(set(group.replace('\n', ''))) for group in groups))

# Part 2
count = 0
for group in groups:
    sets = [set(line) for line in group.splitlines()]
    count += len(sets[0].intersection(*sets[1:]))
print(count)

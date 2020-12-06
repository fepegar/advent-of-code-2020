def get_row(boarding_pass):
    return sum((c == 'B') * 2**i for i, c in enumerate(boarding_pass[-4::-1]))

def get_column(boarding_pass):
    return sum((c == 'R') * 2**i for i, c in enumerate(boarding_pass[:-4:-1]))

def get_seat(boarding_pass):
    return 8 * get_row(boarding_pass) + get_column(boarding_pass)

print(get_seat('FBFBBFFRLR'))
print(get_seat('BFFFBBFRRR'))
print(get_seat('FFFBBBFRRR'))
print(get_seat('BBFFBBFRLL'))
print()

with open('input.txt') as f:
    seats = sorted(get_seat(line.strip()) for line in f.readlines())
print(max(seats))
for a, b in zip(seats, seats[1:]):
    if b - a == 2:
        print(a + 1)
        break

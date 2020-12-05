import re
from pathlib import Path

FIELDS = (
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
    'cid',
)

def check_passport(passport):
    for field in FIELDS:
        if field != 'cid' and field not in passport: return False
    if not 1920 <= int(passport['byr']) <= 2002: return False
    if not 2010 <= int(passport['iyr']) <= 2020: return False
    if not 2020 <= int(passport['eyr']) <= 2030: return False
    height, units = passport['hgt'][:-2], passport['hgt'][-2:]
    if units not in ('cm', 'in'): return False
    height = int(height)
    if units == 'cm' and not 150 <= height <= 193: return False
    elif units == 'in' and not 59 <= height <= 76: return False
    hair = passport['hcl']
    numbers = '0123456789'
    if hair[0] != '#': return False
    else:
        for c in hair[1:]:
            if c not in (numbers + 'abcdef'): return False
    if passport['ecl'] not in 'amb blu brn gry grn hzl oth'.split(): return False
    pid = passport['pid']
    if len(pid) != 9: return False
    for c in pid:
        if c not in numbers: return False
    return True

lines = Path('input.txt').read_text().splitlines()
# lines = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
# byr:1937 iyr:2017 cid:147 hgt:183cm

# iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
# hcl:#cfa07d byr:1929

# hcl:#ae17e1 iyr:2013
# eyr:2024
# ecl:brn pid:760753108 byr:1931
# hgt:179cm

# hcl:#cfa07d eyr:2025 pid:166559648
# iyr:2011 ecl:brn hgt:59in""".splitlines()

pattern = re.compile(r'(\w+):([#\w]+)')
num_valid = 0
passport = {}
for line in lines:
    if not line:
        num_valid += check_passport(passport)
        passport = {}
        continue
    passport.update(re.findall(pattern, line))
num_valid += check_passport(passport)
print(num_valid)

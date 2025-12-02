with open('inputs/input2.txt') as ifile:
    inp = ifile.read().rstrip('\n').split(',')


def p1():
    return count_invalid(get_invalid_numbers)


def p2():
    return count_invalid(get_invalid_numbers2)


def count_invalid(invalid_getter: callable):
    tot = 0
    for rng in inp:
        rng = tuple([int(i) for i in rng.split("-")])
        tot += invalid_getter(rng)
    return tot


def get_invalid_numbers(r: tuple[int]):
    invalid_count = 0
    for i in range(r[0], r[1]+1):
        stringified = str(i)
        if stringified[:len(stringified)//2] == stringified[len(stringified)//2:]:
            invalid_count += int(stringified)

    return invalid_count


def get_divisors(n: int):
    divisors = [1]
    for i in range(2, n):
        if n % i == 0:
            divisors.append(i)
    return divisors


def is_invalid(s: str):
    if len(s) == 1:
        return False
    i = 0
    divs = get_divisors(len(s))
    while (i < len(divs)):
        repeating = s[0:divs[i]]
        multiplier = len(s)//divs[i]
        if repeating * multiplier == s:
            return True
        i += 1
    return False


def get_invalid_numbers2(r: tuple[int]):
    invalid_count = 0
    for i in range(r[0], r[1]+1):
        stringified = str(i)
        if is_invalid(stringified):
            invalid_count += int(stringified)

    return invalid_count


assert p1() == 17077011375
assert p2() == 36037497037

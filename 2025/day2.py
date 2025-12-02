with open('inputs/input2.txt') as ifile:
    inp = ifile.read().rstrip('\n').split(',')


def p1():
    tot = 0
    for rng in inp:
        rng = tuple([int(i) for i in rng.split("-")])
        tot += get_invalid_numbers(rng)
    return tot


def get_invalid_numbers(r: tuple[int]):
    invalid_count = 0
    for i in range(r[0], r[1]+1):  # figure out later how not to iterate everything
        stringified = str(i)
        if stringified[:len(stringified)//2] == stringified[len(stringified)//2:]:
            # print(f"adding {stringified}")
            invalid_count += int(stringified)

        # generate all other possible values
        candidate = stringified + stringified
        if r[0] <= int(candidate) <= r[1]:
            # print(f"adding c {candidate}")
            invalid_count += int(candidate)

    return invalid_count


def get_divisors(n: int):
    divisors = [1]
    for i in range(2, n):
        if n%i==0:
            divisors.append(i)
    return divisors

def is_invalid(s: str):
    multiplier = len(s)
    if multiplier == 1:
        return False
    i = 0
    # if len(s) % 2 == 0:
    divs = get_divisors(len(s))
    # print(f"s: {s} divs : {divs}")
    while (i < len(divs)):
        repeating = s[0:divs[i]]
        # print(f"div {divs[i]} repeating {repeating}, multi {multiplier}")
        if repeating * multiplier == s:
            return True
        i += 1
        if i>= len(divs):
            break
        multiplier = len(s)//divs[i]
    # elif len(s) % 3 == 0:
    #     while (i < len(s)):
    #         repeating = s[0:i]
    #         if repeating * multiplier == s:
    #             return True
    #         i += 3
    #         multiplier = multiplier//3
    return False


def p2():
    tot = 0
    for rng in inp:
        rng = tuple([int(i) for i in rng.split("-")])
        tot += get_invalid_numbers2(rng)
    return tot


def get_invalid_numbers2(r: tuple[int]):
    invalid_count = 0
    for i in range(r[0], r[1]+1):  # figure out later how not to iterate everything
        stringified = str(i)
        if is_invalid(stringified):
            # print(f"adding {stringified}")
            invalid_count += int(stringified)

    return invalid_count

# print(f"num {11}, result {is_invalid("11")}")
# print(f"num {111}, result {is_invalid("111")}")
# print(f"num {1188511885}, result {is_invalid("1188511885")}")
# print(f"num {1010}, result {is_invalid("1010")}")
print(f"num {12}, result {is_invalid("12")}")
print(f"num {2}, result {is_invalid("2")}")
# print(p1())



print(p2())

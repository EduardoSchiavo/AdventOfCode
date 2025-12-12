from functools import cache
with open("inputs/input11.txt") as ifile:
    inp = ifile.read().splitlines()
    DEVICE_MAP = {
        line.split(":", 1)[0]: line.split(":", 1)[1].strip().split()
        for line in inp
    }


def p1():
    return count_paths("you", "out")


def p2():
    dac_out = count_paths("dac", "out")
    fft_dac = count_paths("fft", "dac")
    svr_fft = count_paths("svr", "fft")
    return dac_out*fft_dac*svr_fft


@cache
def count_paths(start: str, stop: str) -> int:
    tot = 0

    if start == stop:
        return tot + 1

    if start not in DEVICE_MAP:
        return 0

    for connected in DEVICE_MAP[start]:
        tot += count_paths(connected, stop)

    return tot


assert p1() == 523
assert p2() == 517315308154944

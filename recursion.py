def flatten_dict(bundle):
    """dict with nested dicts flatten so all values strings"""
    result = {}
    if is_flat_d(bundle):
        return bundle
    for item in bundle:
        if not isinstance(bundle[item], str):
            new = flatten_dict(bundle[item])
            for n in new:
                result[n] = new[n]
        else:
            result[item] = bundle[item]
    return result


def is_flat_d(thing):
    for key, item in thing.iteritems():
        if not isinstance(item, str):
            return False
    return True


def is_flat_l(thing):
    for item in thing:
        if isinstance(item, list):
            return False
    return True


def flatten_list(lst):
    if is_flat_l(lst):
        return lst
    new = []
    for thing in lst:
        if isinstance(thing, list):
            new += flatten_list(thing)
        else:
            new.append(thing)
    return new


def count_list(lst):
    if not lst:
        return 0
    return 1 + count_list(lst[:-1])


def print_list(lst):
    if not lst:
        return
    print lst[0]
    print_list(lst[1:])


def get_index(lst, thing):
    count = 0
    if lst[0] == thing:
        return count
    return count + 1 + get_index(lst[1:], thing)


def rev_string(word):
    if not word:
        return ""
    return word[-1] + rev_string(word[:-1])


def sum_list(lst):
    if not lst:
        return 0
    return lst[0] + sum_list(lst[1:])


def find_needle(needle, haystack):
    if not haystack:
        return None
    if haystack[0] == needle:
        return 0
    result = find_needle(needle, haystack[1:])
    if result is not None:
        return 1 + result
    return None


def bin(num):
    if num < 2:
        return str(num)
    next = num % 2
    return bin(num / 2) + str(next)


def three(num):
    if num < 3:
        return str(num)
    next = num % 3
    return three(num / 3) + str(next)


def rebase(num, base):
    if num < base:
        return str(num)
    next = num % base
    return rebase(num / base, base) + str(next)


# the iterative solution to rebasing to decimal
def to_ten(num, prev):
    chars = list(num)
    n = len(chars)
    result = 0
    for i in range(1, n + 1):
        result += int(chars[i - 1]) * (int(prev) ** (n - i))
    return result


def tenbase(num, prev):
    if len(num) == 0:
        return 0
    return int(num[-1]) + (tenbase(num[:-1], prev) * prev)

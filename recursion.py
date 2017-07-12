def flatten_dict(bundle):
    """dict with nested dicts flatten so all values strings"""
    result = {}
    if is_flat(bundle):
        return bundle
    for item in bundle:
        if not isinstance(bundle[item], str):
            new = flatten_dict(bundle[item])
            for n in new:
                result[n] = new[n]
        else:
            result[item] = bundle[item]
    return result

def is_flat(thing):
    for key, item in thing.iteritems():
        if not isinstance(item, str):
            return False
    return True

test = {6: {5: {3: '2'}}, 'a': 'b', 'c': 'd', 'e': {1: '2'}}

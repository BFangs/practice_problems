def find_pop(lst, item):
    if not lst:
        return 0
    check = lst.pop()
    if check==item:
        return -1
    else:
        return -1 - find_pop(lst, item)

def find_slice(lst, item):
    if not lst:
        return 0
    if lst[0]==item:
        return 0
    else:
        return 1 + find_slice(lst[1:], item)

# tail recursion is when you don't do work on the way up
def find_index(lst, item, count=0):
    try:
        if lst[count]==item:
            return count
        return find_index(lst, item, count+1)
    except:
        return None

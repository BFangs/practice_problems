def find_index(lst, item):
    if not lst:
        return 0
    check = lst.pop()
    if check==item:
        return -1
    else:
        return -1 - find_index(lst, item)

 def find_index(lst, item, count=0):
    if lst:
        check = lst.pop()
        if check==item:
            return
        else:
            find_index(lst, item, count+1)
    return count

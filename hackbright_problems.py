# recursion
def find_index(lst, item):
    """index of list without other param, doesn't work not sure why"""
    if not lst:
        return 0
    check = lst.pop()
    print check
    if check==item:
        print "woo"
        return -1
    else:
        print "keep on it"
        return -1 - find_index(lst, item)

def find_index(lst, item, count=0):
    """index of list"""
    if lst:
        if lst[count]==item:
            return count
        return find_index(lst, item, count+1)

def reverse(thing):
    """reverse of string"""
    if len(thing) < 2:
        return thing

    return thing[-1] + reverse(thing[:-1])

def counter(lst):
    """length of list"""
    if not lst:
        return 0
    lst.pop()
    return 1+ counter(lst)


# loops and such, no recursion
def reverse_in_place(lst):
    """reverse list in place"""
    for i in xrange(len(lst)/2):
        lst[i], lst[-i-1] = lst[-i-1], lst[i]
    return lst

def decode(thing):
    """decode message, number is skip"""
    nums = set(str(x) for x in range(0,10))
    message = ""
    for i, x in enumerate(thing):
        if x in nums:
            message += thing[i+int(x)+1]
    return message

def leaps(lst):
    """return number of leaps lemur makes"""
    pass

def split(str, splitter):
    """implement .split"""
    new = []
    start = 0
    for i in xrange(len(str)):
        if str[i] == splitter:
            new.append(str[start:i])
            start = i + 1
    if start != 0 and start < (len(str) - 1):
        new.append(str[start:])
    return new

def reverse_string(word):
    new = ""
    for char in word:
        new = char + new
    return new

def rev_words(phrase):
    new = ""
    stub = ""
    num = len(phrase)
    for i in xrange(num-1, -1, -1):
        print i, phrase[i], stub, new
        if phrase[i] == " ":
            new += phrase[i]
        else:
            stub = phrase[i] + stub
            if phrase[i-1] == " " or i==0:
                new += stub
                stub = ""
    return new


["cat", "hat", "bat"], "hat"
["blue","red","yellow","black","white","orange","green"]
"porcupine"
"I love hackbright"

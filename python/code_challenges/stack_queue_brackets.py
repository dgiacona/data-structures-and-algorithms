from data_structures.queue import Queue
from data_structures.stack import Stack

open_bracks = Stack()
openers = ["(", "[", "{"]
closers = [")", "]", "}"]
matches = {
    ')': '(',
    ']': '[',
    '}': '{'
}

def multi_bracket_validation(bracks):
    if len(bracks) // 2 != 0:
        return False
    elif bracks[0] in closers:
        return False
    else:
        for x in len(bracks):
            if bracks[x] in openers:
                open_bracks.push(x)
            else:
                print("hello world")
                match_combo = (bracks[0] + open_bracks.peek())
                print(match_combo)
                if (bracks[0] + open_bracks.peek()) in matches:
                    open_bracks.pop()
                else:
                    return False

#             print(open_bracks)
#
multi_bracket_validation("[[{}]]")

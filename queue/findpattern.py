def checkPattern(ptr):
    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    stack = []

    for p in ptr:
        if p in pairs:
            if not stack or stack[-1] != pairs[p]:
                return False
            stack.pop()
        else:
            stack.append(p)

    return len(stack) == 0


print(checkPattern("(){}[]"))   # True
print(checkPattern("([{}])"))   # True
print(checkPattern("([)]"))     # False
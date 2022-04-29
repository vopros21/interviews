def isValid(string):

    stack = []
    for s in string:
        if s in ['(', '[', '{']:
            stack.append(s)
        else:
            if len(stack) == 0:
                return False
            elif s == ')' and stack.pop() != '(':
                return False
            elif s == ']' and stack.pop() != '[':
                return False
            elif s == '}' and stack.pop() != '{':
                return False
    if len(stack) != 0:
        return False
    return True


if __name__ == "__main__":
    line = ""
    print(isValid(line))

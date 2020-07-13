def is_balanced(string):
    stack = []
    open_brackets = "{(["
    for bracket in string:
        if bracket in open_brackets:
            stack.append(bracket)
        else:
            if not stack:
                return False
            if not is_matching(stack.pop(), bracket):
                return False
    if not stack:
        return True
    return False


def is_matching(opening, closing):
    if (opening == '(' and closing == ')') or\
            (opening == '[' and closing == ']') or\
            (opening == '{' and closing == '}'):
        return True
    return False

if __name__ == "__main__":
    print(is_balanced('{}[]()'))
    print(is_balanced('{]('))
    print(is_balanced('{[({[}])]}'))

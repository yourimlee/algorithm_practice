import sys

while True:
    sentences = sys.stdin.readline().rstrip()
    stack = []
    true_flag = 1
    for s in sentences:
        if s == "(" or s == "[":
            stack.append(s)
        elif s == ")":
            if len(stack) != 0 and stack[-1] == "(":
                stack.pop()
            else:
                true_flag = 0
                break
        elif s == "]":
            if len(stack) != 0 and stack[-1] == "[":
                stack.pop()
            else:
                true_flag = 0
                break

    if sentences == '.': break

    print('yes' if true_flag and not(stack) else 'no')
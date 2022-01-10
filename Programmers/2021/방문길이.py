def solution(dirs):
    answer = set()
    loc = (0,0)
    for i in dirs:
        x, y = loc
        if i == 'U':
            y += 1
        elif i == 'D':
            y -= 1
        elif i == 'L':
            x -= 1
        elif i == 'R':
            x += 1
        if -5 <= x and x <= 5 and -5 <= y and y <= 5:
            next = (x, y)
            answer.add((next, loc))
            answer.add((loc, next))
            loc = next
    return len(answer) // 2
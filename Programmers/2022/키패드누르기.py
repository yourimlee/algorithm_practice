def solution(numbers, hand):
    answer = ''
    dict = {'*':[0,0], 0:[1,0], '#':[2,0], 7:[0,1], 8:[1,1], 9:[2,1],
            4:[0,2], 5:[1,2], 6:[2,2], 1:[0,3], 2:[1,3], 3:[2,3]}
    left, right = dict['*'], dict['#']
    for num in numbers:
        now = dict[num]
        if num == 1 or num == 4 or num == 7:
            answer += 'L'
            left = now
        elif num == 3 or num == 6 or num == 9:
            answer += 'R'
            right = now
        else:
            dist_left, dist_right = 0, 0
            for a, b, c in zip(left, right, now):
                dist_left += abs(a-c)
                dist_right += abs(b-c)
            if dist_left < dist_right:
                answer += 'L'
                left = now
            elif dist_left > dist_right:
                answer += 'R'
                right = now
            else:
                if hand == 'left':
                    answer += 'L'
                    left = now
                else:
                    answer += 'R'
                    right = now
    return answer
def solution(n, words):
    answer = [0,0]
    i = 1
    for ind in range(1, len(words)):
        word = words[ind]
        if (word in words[0:ind]) or word[0] != words[ind-1][-1]:
            answer = [i%n+1, i//n+1]
            return answer
        i += 1

    return answer
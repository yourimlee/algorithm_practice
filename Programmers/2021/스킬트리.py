def solution(skill, skill_trees):
    answer = 0
    skill_list = list(skill)
    for skills in skill_trees:
        ans = True
        tree_list = []
        for s in skills:
            if s in skill_list:
                tree_list.append(s)
        for t in range(len(tree_list)):
            if tree_list[t] != skill_list[t]:
                ans = False
                break
        if ans == True:
            answer += 1

    return answer
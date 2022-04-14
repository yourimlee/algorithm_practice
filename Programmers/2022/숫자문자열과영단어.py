def solution(s):
    strings = [('zero', '0'), ('one', '1'), ('two', '2'), ('three', '3'), ('four', '4'), ('five', '5'), ('six', '6'), ('seven', '7'), ('eight', '8'), ('nine', '9')]
    while s.isdigit() == False:
        for i in range(len(strings)):
            if strings[i][0] in s:
                s = s.replace(strings[i][0], strings[i][1])
        return int(s)
  
    return int(s)

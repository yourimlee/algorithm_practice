import re

def solution(files):
    file_list = [re.split('([0-9]+)', f) for f in files]
    file_list.sort(key = lambda x: (x[0].lower(), int(x[1])))

    return ["".join(s) for s in file_list]

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
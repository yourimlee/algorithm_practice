import re

def solution(phone_book):
    phone_book.sort()
    for i in phone_book:
        res=re.compile("^"+i) # ^는 ^뒤에 나오는 것을 찾는 것, 즉 접두어가 i인것을 찾는 것이다.
        for l in phone_book:
            if i!=l and res.match(l): # phone_book에서 차례대로 가져오는 것이므로 같은 원소가 아니면서 re를 접두어로 가지고 있는 것을 찾는 것이다.
                return False 
    return True
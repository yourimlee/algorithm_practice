import re

text1="(()) 오랜만에 아기가1 이 @웃음 생긴 거고 그러고 인제 첫 번째 그~ 크리스마스여서요"
#text2=

def cleansing(data):

    text=re.sub('[^ㄱ-힣\s.,?!]',"",data)
    spe=re.compile('[@&\{\((]',"",data)
    return text, spe

print(cleansing(text1))
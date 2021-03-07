# 이 문제는 전부터 풀고싶었는데 마땅한 해답이 정말 떠오르지 않아서 풀이를 참고함.

# # [6, 10, 2]을 예시로 들면, numbers.sort(key=lambda x" x*3, reverse = True)를 하면,
# # [666, 101010, 222]가 되고 이를 정렬하면, [666, 222, 101010]이 되어서 결과적으로 [6, 2, 10]의 순서가 된다.
# # 위와 같이 정렬되는 이유는 "문자열 비교연산의 경우엔 첫번째 인덱스인 666[0]인 6과 101010[0]인 1과 222[0]인 2를 ascii숫자로 바꿔서 비교한다. 
# # 물론 같으면, 다음 인덱스도 비교합니다. 비교한 결과 [6, 2, 10]의 순으로 정렬됩니다.
# # 즉, 앞자리가 큰 6 -> 2 -> 1순으로 정렬되어서 위와 같은 결과를 얻게 된 것이다.

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))
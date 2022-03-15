import collections
def solution(money, costs):
    coin = [1, 5, 10, 50, 100, 500]
    answer = 0
    costs_per_prod = {}
    for i in range(len(costs)):
        costs_per_prod[coin[i]] = round((costs[i] / coin[i]), 2)
    costs_per_prod_ = sorted(costs_per_prod.items(), key=lambda x: (x[1], -x[0]))

    num = {}
    for i in range(6):
        num[costs_per_prod_[i][0]] = money // costs_per_prod_[i][0]
        money %= costs_per_prod_[i][0]
    num_ = sorted(num.items(), key=lambda x: x[0])
    
    for i in range(6):
        answer += num_[i][1] * costs[i]

    return answer
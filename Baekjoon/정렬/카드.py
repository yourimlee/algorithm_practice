n = int(input())
cards = {}

for _ in range(n):
    k = int(input())
    if k in cards:
        cards[k] += 1
    if k not in cards:
        cards[k] = 1
        
freq_max = max(cards.values())
max_cards = []

for card, count in cards.items():
    if count == freq_max:
        max_cards.append(card)

print(sorted(max_cards)[0])
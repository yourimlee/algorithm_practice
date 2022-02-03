n = int(input())
books = {}

for _ in range(n):
    b = input()
    if b in books:
        books[b] += 1
    if b not in books:
        books[b] = 1
        
freq_max = max(books.values())
best_seller = []

for book, count in books.items():
    if count == freq_max:
        best_seller.append(book)

print(sorted(best_seller)[0])
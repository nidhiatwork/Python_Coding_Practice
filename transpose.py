matrix = [
[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12]
]

# via loops
transpose = []
for i in range(len(matrix[0])):
    items = []
    for row in matrix:
        items.append(row[i])
    transpose.append(items)
print(transpose)

#via list comprehension
t = [[row[i] for row in matrix]for i in range(len(matrix[0]))]
print(t)
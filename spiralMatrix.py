# our goal is to take any given M x N matrix, and return a list of it's values traversed in a spiral fashion

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12],
    [13,14,15]
]

# solution is going to be -> [1, 2, 3, 6, 9, 12, 15, 14, 13, 10, 7, 4, 5, 8, 11]

solution = []

while matrix:
    solution.extend(matrix.pop(0))
    matrix = [*(zip(*matrix))][::-1]
print(solution)

# matrix.pop(0)
# [4,5,6], - post pop() function
# [7,8,9],
# [10,11,12],
# [13,14,15]

# *matrix
# [4,5,6] [7,8,9] [10,11,12] [13,14,15] - post splat operation

# *(zip(*matrix))
# (4,7,10,13) (5,8,11,14) (6,9,12,15) - post zip operation with another splat, turns them into individual tuples

# [*(zip(*matrix))]
# [(4,7,10,13), (5,8,11,14), (6,9,12,15)] - using list syntax [] around the product turns them into indexed list items

# [*(zip(*matrix))][::-1]
# [(6,9,12,15), (5,8,11,14), (4,7,10,13)] - [::-1] reverses their order as list items, not each item's order

# this process causes the next loop to essentially pop the "top row" of the matrix again, until we're left with no more values to work with, and returning the list

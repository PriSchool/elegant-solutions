# our goal is to take any given M x M matrix represting a 2D image, and rotate it 90 degrees, clockwise (perform it in-place, no creation of any new matrices).

matrix = [
  [5,1,9,11],
  [2,4,8,10],
  [13,3,6,7],
  [15,14,12,16]
]

# solution goal is going to be -> [
#                                   [15,13,2,5],
#                                   [14,3,4,1],
#                                   [12,6,8,9],
#                                   [16,7,10,11]
#                                 ]

matrix[:] = [*(zip(*matrix))]

# *matrix
# [5,1,9,11] [2,4,8,10] [13,3,6,7] [15,14,12,16] - post splat operation
---------⬇️⬇️⬇️---------
# *(zip(*matrix))
# (5,2,13,15) (1,4,3,14) (9,8,6,12) (11,10,7,16) - post zip operation with another splat, turns them into individual tuples
---------⬇️⬇️⬇️---------
# [*(zip(*matrix))]
# [(5,2,13,15) (1,4,3,14) (9,8,6,12) (11,10,7,16)] - using list syntax [] around the product turns them into indexed list items
---------⬇️⬇️⬇️---------
# matrix[:]
# we use this syntax instead of a plain 'matrix' usage, because the question requires us to perform the changes in-place - thus we use this slice operator

matrix[:] = [[*item][::-1] for index, item in enumerate(matrix)]

# [*item]
# [5,2,13,15] - this operation takes an item inside of the matrix (item in this case being a full row, still saved as a tuple), flattens it to it's individual values using splat, and then creates a list out of them 
---------⬇️⬇️⬇️---------
# [*item][::-1]
# [15,13,2,5] - this slicing operation flips the mentioned item (being a full matrix row, now saved as a list)
---------⬇️⬇️⬇️---------
# [[*item][::-1] for index, item in enumerate(matrix)]
# [15,13,2,5], [14,3,4,1], [12,6,8,9], [16,7,10,11] - we perform the previous operation of flattening, then saving in a list and finally reversing - but for each of the mentioned rows inside of the matrix  

return matrix

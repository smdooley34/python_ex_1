####################################################################################################
# ex1.py
#
# This file contains the solution to Homework One Exercise One.
#
# Prompt:
#
#   L = [0, [], [1, 2, 3, 4], [[5], [6, 7]], [8, 9, 10]]
#
#   Using both indexing and slicing on L, assemble and print a new list N that contains:
#     [0, 2, 3, [5, 6], 8, 10]
#
#   As an example, here's how I've constructed a similar list X which contains [[2, 3], [10]] from L:
#
#   L = [0, [], [1, 2, 3, 4], [[5], [6, 7]], [8, 9, 10]]
#   X = [ L[2][1:-1], L[-1][2] ]
#   print(x) => [[2, 3], [10]]
#
#   You need to do something similar but end up with [0, 2, 3, [5, 6], 8, 10] instead. One way to
#   work through this is to break the process down in small steps, store result of each step in a
#   new variable and use those variables in the next step.
####################################################################################################

print("----- Start Of Part 1 -----")
print("\n")

L = [0, [], [1, 2, 3, 4], [[5], [6, 7]], [8, 9, 10]]
print("Old Array: ", L)

# Simply Directly Accessing Required Indices Is Probably The Most Readable But Easily Unwieldy Approach
N = [L[0], L[2][1], L[2][2], [L[3][0][0], L[3][1][0]], L[4][0], L[4][2]]
print("New Array: ", N)

print("\n")
print("----- End Of Part 1 -----")

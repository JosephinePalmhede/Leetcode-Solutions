"""
Solution by Josephine Palmhede for August 8th, 2021 leetcode question
Guided by https://leetcode.libaoj.in/rank-transform-of-a-matrix.html

Given an m x n matrix, return a new matrix answer where answer[row][col] is the rank of matrix[row][col].
The rank is an integer that represents how large an element is compared to other elements. It is calculated using the following rules:
    - The rank is an integer starting from 1.
    - If two elements p and q are in the same row or column, then:
        -- If p < q then rank(p) < rank(q)
        -- If p == q then rank(p) == rank(q)
        -- If p > q then rank(p) > rank(q)
    - The rank should be as small as possible.
"""

def matrixRankTransform(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[List[int]]
    """
    print("given matrix: ", matrix)
    rows = len(matrix)
    columns = len(matrix[0])

    #dictionary to map elements to their location in the matrix
    d = dict()
    for i in range(rows):
        for j in range(columns):
            element = matrix[i][j]
            if element not in d:
                d[element] = [(i, j)]
            else:
                d[element].append((i,j))
    print("d: ", d)

    #link the rows and columns
    #I will use this to find connected elements
    connections = {} #connections[element] = the connections to element
    for row in range(rows):
        for col in range(columns):
            element = matrix[row][col]
            if element not in connections:
                connections[element] = {}
            if row not in connections[element]:
                connections[element][row] = []
            #∼col = −col − 1 and ∼(∼col) = col
            #used to store columns and rows in the same map, without complication from both having an index 0.
            if ~col not in connections[element]:
                connections[element][~col] = []
            #link row and column
            connections[element][row].append(~col)
            connections[element][~col].append(row)
    print("connections: ", connections)

    """
    In the example of test 1, the following matrix:
    [1 2]
    [2 3]
    is represented in connections as:
    {1: {0: [-1], -1: [0]}, 2: {0: [-2], -2: [0], 1: [-1], -1: [1]}, 3: {1: [-2], -2: [1]}}
    where the positive numbers are the rows and negative numbers are the columns.

    This is interpreted as element 1 is in row 0 and column 0 (~0 = -0 - 1 = -1). Thus through element 1, row 0 has a link to columnn 0 and column 0 has a link to row 0.
    Element 2 is in row 0 and column 1 (~1 = -1 - 1 = -2), and row 1 and column 0 (~0 = -0 - 1 = -1). 
    So through element 2, row 0 has a link to column 1, column 1 has a link to row 0, row 1 has a link to column 0, and column 0 has a link to row 1.
    Element 3 is in row 1 and column 1 (~1 = -1 - 1 = -2), etc.
    """

    #create an element-index map that separates elements to put connected elements together in the same array
    elementindex = dict()
    seen = []
    for i in range(rows):
        for j in range(columns):
            if (i, j) not in seen:
                seen.append((i,j))
                element = matrix[i][j]
                cons = connections[element]
    
    
    
    
    #collect all elements into a list
    allElements = []
    for i in range(rows):
        for j in range(columns):
            allElements.append(matrix[i][j])
              
    #sort list
    allElements.sort()
    print("allElements: ", allElements)
        
    #remove duplicates with list comprehension
    elements = []
    [elements.append(x) for x in allElements if x not in elements]
    print("elements: ", elements)
    
    """
    initial answer to all zero
    initial rowMax and colMax to all zero
    for connected_part in sorted_connected_parts:
        rank = -1
        for point (i, j) in connected_part:
            rank = (rank, max(rowMax[i], colMax[i]) + 1)
        for point (i, j) in connected_part:
            answer[i][j] = rank
            update rowMax and colMax
    """
    #rank transform
    for key in d.keys():
        rank = elements.index(key) + 1
        print("rank: ", rank)
        #d[key] returns [(r1, c1), (r2, c2), ..]
        for i in range(len(d[key])):
            (r, c) = d[key][i]
            print("(r, c): ", r, c)
            matrix[r][c] = rank
    print(matrix)
    return matrix
        
matrix1 = [[1,2],[2,3]]
output1 = [[1,2],[2,3]]
matrix2 = [[7,7],[7,7]]
output2 = [[1,1],[1,1]]
matrix3 = [[20,-21,14],[-19,4,19],[22,-47,24],[-19,4,19]]
output3 = [[4,2,3],[1,3,4],[5,1,6],[1,3,4]]
matrix4 = [[7,3,6],[1,4,5],[9,8,2]]
output4 = [[5,1,4],[1,2,3],[6,3,1]]

print("\nTest 1:")
if output1 == matrixRankTransform(matrix1):
    print("pass")
else:
    print("fail")
print("\nTest 2:")
if output2 == matrixRankTransform(matrix2):
    print("pass")
else:
    print("fail")
print("\nTest 3:")
if output3 == matrixRankTransform(matrix3):
    print("pass")
else:
    print("fail")
print("\nTest 4:")
if output4 == matrixRankTransform(matrix4):
    print("pass")
else:
    print("fail")

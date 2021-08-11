"""
Solution by Josephine Palmhede for August 8th, 2021 leetcode question

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
    d = dict()
    # list(d) -> Return a list of all the keys used in the dictionary d
    # len(d) -> Return the number of items in the dictionary d
    # d.items() -> Return a new view of the dictionary’s items ((key, value), ..)
    # d.keys() -> Return a new view of the dictionary’s keys
    # d.values() -> Return a new view of the dictionary’s values
    # d[key] -> Return the item of d with key key. Raises a KeyError if key is not in the map.
    # d[key] = value -> Set d[key] to value
    # key in d -> Return True if d has key, else False
    # iter(d) -> Return an iterator over the keys of the dictionary

    rows = len(matrix)
    columns = len(matrix[0])

    print("given matrix: ", matrix)
    #sort into ascending order the elements in the same row and column
    #the rank of element i will be the position of element i in the array, given there are no duplicates.
        
    #collect like elements in a dictionary
    #need to account for situation where there is a duplicate number but it is not in the same column or row...
    for i in range(rows):
        for j in range(columns):
            element = matrix[i][j]
            if element not in d:
                d[element] = [(i, j)]
            else:
                d[element].append((i,j))
    print("d: ", d)
        
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
        
    for key in d.keys():
        rank = elements.index(key) + 1
        print("rank: ", rank)
        #d[key] returns [(r1, c1), (r2, c2), ..]
        for i in range(len(d[key])):
            (r, c) = d[key][i]
            print("(r, c): ", r, c)
            matrix[r][c] = rank
    print(matrix)
        
matrix1 = [[1,2],[2,3]]
output1 = [[1,2],[2,3]]
matrix2 = [[7,7],[7,7]]
output2 = [[1,1],[1,1]]
matrix3 = [[20,-21,14],[-19,4,19],[22,-47,24],[-19,4,19]]
output3 = [[4,2,3],[1,3,4],[5,1,6],[1,3,4]]
matrix4 = [[7,3,6],[1,4,5],[9,8,2]]
output4 = [[5,1,4],[1,2,3],[6,3,1]]
matrixRankTransform(matrix4)
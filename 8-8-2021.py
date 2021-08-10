class Solution(object):
    def matrixRankTransform(self, matrix):
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
        #the rank of element i will be the position of element i in the array, given there are no                   duplicates.
        
        #collect like elements in a dictionary
        #need to account for situation where there is a duplicate number but it is not in the same column or          row...
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
                print(r, c)
            
            
        
"""
Solution by Josephine Palmhede for August 6th, 2021 leetcode question.

Given an n-ary tree, return the level order traversal of its nodes' values.
"""
import Queue

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        answer = []
        qu = Queue.Queue()
        qu.put(root)
        
        if root is None:
            return []
        elif (len(root.children) is 0) or (len(root.children) is root.children.count(None)):
            return [[root.val]]

        else:
            while qu.qsize() is not 0:
                temp = []
                for i in range(qu.qsize()):  
                    node = qu.get()
                    temp.append(node.val)
                    for i in range(len(node.children)):
                        qu.put(node.children[i])
                answer.append(temp)
            return answer
